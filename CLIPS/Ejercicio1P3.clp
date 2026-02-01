(deftemplate aeronaves
    (slot id)
    (slot compania)
    (slot origen)
    (slot destino)
    (slot velocidad)
    (slot peticion (allowed-values Ninguna Despegue Aterrizaje Emergencia Rumbo))
    (slot estado (allowed-values enTierra Ascenso Crucero Descenso)(default enTierra))
)

(deftemplate aerodromos 
    (slot id)
    (slot ciudad_actual)
    (slot radar (allowed-values ON OFF))
    (slot visibilidad)
    (slot viento)
)

(deftemplate piloto
    (slot id)
    (slot aeronave)
    (slot estado (allowed-values OK SOS Ejecutando Stand-by)(default Stand-by))
)

(deftemplate vuelos
    (slot aerodromo_origen)
    (slot aerodromo_destino)
    (slot distancia)
    (slot velocidad_despegue(default 240))
    (slot velocidad (default 700))
)

(deftemplate meteorologia
    (slot aeropuerto)
    (slot tiempo (allowed-values Lluvia Niebla Nieve VientoHuracanado Despejado))
    (slot restriccion (allowed-values SI NO))
)

(defrule alerta_meteorologia
    (declare (salience 10))
    ?aeronave<-(aeronaves (id ?id)(peticion ?p)(origen ?origen))
    (aerodromos (id ?ae)(ciudad_actual ?origen))
    (meteorologia(aeropuerto ?ae)(restriccion ?r))
    ?piloto<-(piloto (aeronave ?id)(estado ?e))
    (test(eq ?r SI))
    (test(eq ?p Despegue))
    (test (eq ?e Ejecutando))
    =>
    (modify ?aeronave (peticion Ninguna))
    (modify ?piloto (estado Stand-by))
    (println "Alerta: Despegue CANCELADO por condiciones climaticas adversas")
)

(defrule PilotoAsociado
    (declare (salience 8))
    (aeronaves (id ?id)(peticion Despegue)(compania ?c)(origen ?o)(destino ?d))
    (vuelos(aerodromo_origen ?o))
    (aerodromos (id ?aerodromo)(ciudad_actual ?o))
    (exists(piloto (aeronave ?id)(estado OK)))
    =>
    (println "COMPROBACION CORRECTA: La aeronave " ?id " de la compania " ?c " tiene PILOTO asignado para poder realizar el vuelo desde el aerodromo " ?o "con destino" ?d " para realizar un vuelo de los registrados en el aerodromo de origen y la aeronave se encuentra en peticion de Despegue")
)

(defrule PeticionDespegue 
    (declare (salience 6))
    (aeronaves (id ?ae)(estado enTierra)(peticion Despegue)(origen ?o)(destino ?d))
    (piloto (aeronave ?ae)(estado OK))
    (vuelos (aerodromo_origen ?id1)(aerodromo_destino ?id2))
    (aerodromos(id ?id1)(ciudad_actual ?o)(radar ON)(visibilidad ?v)(viento ?vi))
    (aerodromos (id ?id2)(ciudad_actual ?d)(radar ON)(visibilidad ?v)(viento ?vi))
    (meteorologia(aeropuerto ?o)(restriccion NO))
    (test(> ?v 5))
    (test(< ?vi 75))
    (not (Peticion_Autorizada ?ae))
    =>
    (assert ( Peticion_Autorizada ?ae))
    (println "Cofirmada la peticion de la aeronave " ?ae)
)

(defrule Despegar
    ?aeronave<-(aeronaves (id ?ae)(estado enTierra))
    (Peticion_Autorizada ?ae)
    ?p<-(piloto (aeronave ?ae)(estado OK))
    (vuelos (aerodromo_origen ?id1)(aerodromo_destino ?id2)(velocidad_despegue ?vd))
    (aerodromos(id ?id1)(ciudad_actual ?o)(radar ON)(visibilidad ?v)(viento ?vi))
    (aerodromos (id ?id2)(ciudad_actual ?d)(radar ON)(visibilidad ?v)(viento ?vi))
    =>
    (modify ?p(estado Ejecutando))
    (modify ?aeronave(estado Ascenso)(velocidad ?vd)(peticion Ninguna))
    
)

(defrule v_crucero
    ?f1<-(aeronaves (id ?aeronave)(origen ?o)(destino ?d)(estado ?e))
    ?f2<-(piloto (aeronave ?aeronave))
    (vuelos (aerodromo_origen ?o)(aerodromo_destino ?d)(velocidad ?vc))
    (test (eq ?e Ascenso))

    =>
    (modify ?f1 (estado Crucero)(velocidad ?vc))
    (modify ?f2 (estado Stand-by))
)
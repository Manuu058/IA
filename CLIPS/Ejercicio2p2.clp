(deftemplate valvula
    (slot nombre)
    (slot estado(allowed-values abierta cerrada)(default cerrada))
    (slot presion (default 0))
    (slot temperatura_interna (default 0))
    (slot temperatura_externa (default 0))

)
(deffacts hechos-iniciales
    (valvula (nombre Entrada) (temperatura_interna 101) (temperatura_externa 35) (presion 1))
    (valvula (nombre Salida) (temperatura_interna 101) (temperatura_externa 155) (presion 5))
    (valvula (nombre Pasillo1) (temperatura_interna 99) (temperatura_externa 37) (estado cerrada))
)

(deffunction f1 (?p ?t1)
    (while (> ?t1 35)
        (bind ?p (+ ?p 1))
        (bind ?t1 (- ?t1 5))
    
    )
    (return ?p)
)

(deffunction f2 (?t1 ?t2)
    (if (> ?t1 ?t2)
        then (return (- ?t1 ?t2))
        else (return (- ?t2 ?t1))
    )
)


(defrule R1
    ?v<-(valvula (presion ?p)(estado ?e))
    (test (eq ?e abierta))
    (test (eq ?p 5))
    =>
    (modify ?v (presion 0)(estado cerrada))
)

(defrule R2
    ?v<-(valvula (presion ?p)(estado ?e)(temperatura_interna ?t1))
    (test (eq ?e cerrada))
    (test (< ?p 10))
    (test (> ?t1 35))
    =>
    (modify ?v (presion (f1 ?p ?t1))(estado abierta))
)

(defrule R3
    ?v1<-(valvula (presion ?p)(estado ?e)(temperatura_externa ?t2))
    ?v2<-(valvula (presion ?p)(estado ?e)(temperatura_interna ?t1)(temperatura_externa ?t2))
    (test (neq ?v1 ?v2))
    (test (< ?t1 ?t2))
    =>
    (modify ?v1 (estado abierta))
    (modify ?v2 (estado abierta)(temperatura_externa (f2 ?t1 ?t2)))
)


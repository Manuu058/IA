(deftemplate producto
    (slot idproducto)
    (slot nombre)
    (slot pasillo (allowed-values 1 2 3 4 5 6 7 8 9 10 11 12))
    (slot stock)
    (slot precio)
)

(deftemplate pedido 
    (slot idcliente)
    (slot idproducto)
    (slot unidades)
)

(deftemplate carro
    (slot idcliente)
    (slot narticulos (default 0))
    (slot total (default 0))
    (slot pasilloactual (default 1)(allowed-values 1 2 3 4 5 6 7 8 9 10 11 12))
)

(deftemplate nuevo_cliente
    (slot idcliente)
)

(defrule asignar_carro
    ?f0<-(nuevo_cliente (idcliente ?idcliente))
    =>
    (assert (carro (idcliente ?idcliente)))
    (retract ?f0)
)

(defrule mover_carro
    (declare(salience 0))
    ?f0<-(carro (idcliente ?idcliente)(pasilloactual ?pasillo))
    =>
    (bind ?movimiento (accion_carro ?pasillo))
    (modify ?f0 (pasilloactual ?movimiento))
)

(deffunction accion_carro (?pasillo)
   (if (< ?pasillo 12)
       then (return (+ ?pasillo 1))
       else (return 1))
)


(defrule comprar
    (declare (salience 10))
    ?f0<-(carro (idcliente ?idcliente)(pasilloactual ?pasillocarro)(total ?total))
    ?f1<-(producto(idproducto ?idproducto)(pasillo ?pasillocarro)(precio ?precio)(stock ?stock))
    ?f2<-(pedido (idcliente ?idcliente)(idproducto ?idproducto)(unidades ?unidades))
    (test (>= ?stock ?unidades))
    =>
    (bind ?factura (calcular_factura ?precio ?unidades ?total))
    (modify ?f0 (total ?factura))
    (modify ?f1 (stock (- ?stock ?unidades)))
    (retract ?f2)
)

(deffunction calcular_factura (?precio ?unidades ?total)
    (return (+ ?total (* ?precio ?unidades)))
)

(defrule existencias_insuficientes
    (declare(salience 5))
    ?f0<-(carro (idcliente ?idcliente)(pasilloactual ?pasillocarro)(total ?total))
    ?f1<-(producto(idproducto ?idproducto)(pasillo ?pasillocarro)(precio ?precio)(stock ?stock))
    ?f2<-(pedido (idcliente ?idcliente)(idproducto ?idproducto)(unidades ?unidades))
    (test (< ?stock ?unidades))
    =>
    (printout t "No hay existencias disponibles para este pedido" crlf)
    (retract ?f2)
)
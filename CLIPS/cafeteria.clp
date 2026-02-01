(deftemplate personal
    (slot dni (type INTEGER))
    (slot nombre)
    (slot turno (allowed-values mañana tarde ambos))
    (slot totalventas)
    (slot encargado (allowed-values SI NO))
)

(deftemplate producto
    (slot id(type INTEGER))
    (slot nombre)
    (slot stock_cafeteria)
    (slot stock_almacen)
    (slot precio)
    (slot maximo (default 30))
)

(deftemplate venta
    (slot camarero)
    (slot producto)
    (slot unidades)
    (slot pago(allowed-values tarjeta bono efectivo))
)

(defrule AsignarVenta
    (declare (salience 10))

    ?f1<-(personal (dni ?c)(nombre ?nom)(totalventas ?tv))
    ?f2<-(producto(id ?p)(stock_cafeteria ?actual)(precio ?costo))
    ?v<-(venta(camarero ?c)(producto ?p)(unidades ?u))
    (test (< ?u ?actual))
    =>
    (modify ?f1 (totalventas (+ ?tv (* ?costo ?u))))
    (modify ?f2 (stock_cafeteria (- ?u ?actual)))
    (retract(v))
)

(defrule ReponerStock 
    ?f1<-(producto(id ?id)(stock_cafeteria ?sc)(stock_almacen ?sa)(maximo ?m))

    (test (< ?sc 10))
    =>
    (bind ?repuesto (Reposicion(?sa ?m ?sc)))
    (modify ?f1(stock_cafeteria (+ ?repuesto ?sc))(stock_almacen(- ?sa ?repuesto)))
)


(deffunction Reposicion (?almacen ?stock_max ?stock)
    (bind ?total (- ?stock_max ?stock))
    (if(< ?almacen ?total)
        then (return (?almacen))
        else (return (?total))
    )
)
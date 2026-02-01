(deffacts ubicacion
    (ubicacion A Norte D)
    (ubicacion A oeste B)
    (ubicacion B Norte E)
    (ubicacion B oeste C)
    (ubicacion C norte F)
    (ubicacion D Norte G)
    (ubicacion E Norte H)
    (ubicacion F Norte I)
    (ubicacion D oeste E)
    (ubicacion E oeste F)
    (ubicacion G oeste H)
    (ubicacion H oeste I)
)

(defrule sur
    (ubicacion ?x Norte ?y)
    =>(assert(ubicacion ?y sur ?x))
)

(defrule este
    (ubicacion ?x oeste ?y)
    =>(assert(ubicacion ?y este ?x))
)

(defrule transitividad_norte
    (ubicacion ?x Norte ?y)
    (ubicacion ?y norte ?z)
    =>(assert (ubicacion ?x Norte ?z))
);transitividad_norte

(defrule transitividad_oeste
    (ubicacion ?x oeste ?y)
    (ubicacion ?y oeste ?z)
    =>(assert (ubicacion ?x oeste ?z))
);transitividad_oeste

(defrule noreste
    (ubicacion ?x oeste ?y)(ubicacion ?z norte ?y)
    =>(assert(ubicacion ?z noreste ?x))
);noreste

(defrule noroeste
    (ubicacion ?x este ?y)(ubicacion ?z norte ?y)
    =>(assert(ubicacion ?z noroeste ?x))
);noroeste

(defrule sureste
(ciudad ?x oeste ?y)(ciudad ?z sur ?y)
=> (assert (ciudad ?z sureste ?x))
);sureste

(defrule suroeste
(ciudad ?x este ?y)(ciudad ?z sur ?y)
=> (assert (ciudad ?z suroeste ?x))
);suroeste

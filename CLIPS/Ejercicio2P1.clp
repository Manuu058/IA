(deftemplate portal
    (slot cantidad)
    (slot maletero)
    (slot caballos)
    (slot sistemas)
    (slot consumo)
);coche 
(deffacts coches
    (coche
        (modelo Modelo1)
        (precio 12000)
        (maletero Pequeño)
        (CV 65)
        (ABS No)
        (L 4.7))
    (coche
        (modelo Modelo2)
        (precio 12500)
        (maletero Pequeño)
        (CV 80)
        (ABS Si)
        (L 4.9))
    (coche
        (modelo Modelo3)
        (precio 13000)
        (maletero Mediano)
        (CV 100)
        (ABS Si)
        (L 7.8))
    (coche
        (modelo Modelo4)
        (precio 14000)
        (maletero Grande)
        (CV 125)
        (ABS Si)
        (L 6.0))
    (coche
        (modelo Modelo5)
        (precio 15000)
        (maletero Pequeño)
        (CV 147)
        (ABS Si)
        (L 8.5))
);coches

(deftemplate encuesta
    (slot precio (type INTEGER)(default 13000))
    (slot maletero (allowed-values Pequeño Mediano Grande)(default Grande))
    (slot CV (type INTEGER)(default 80))
    (slot ABS (allowed-values No Si)(default Si))
    (slot L (type FLOAT)(default 8.0))
);encuesta

(encuesta (precio ?p)(maletero ?m)(CV ?cv)(ABS ?abs)(L ?l)) ;Comparacion
(coche (modelo ?modelo)(precio ?p_)(maletero ?m_)(CV ?cv_)(ABS ?abs_)(L ?l_)) ;Cojo coche

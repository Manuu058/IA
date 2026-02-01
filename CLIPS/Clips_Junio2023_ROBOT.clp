(deftemplate robot
    (slot fil)
    (slot col)
    (slot orientación (allowed-values Norte Sur Este Oeste))
    (slot tiempo)
)
(deftemplate baldosa
    (slot fil)
    (slot col)
    (slot estado (allowed-values Sucia Limpia)(default Sucia))
)
(deftemplate avance
    (slot orientación (allowed-values Norte Sur Este Oeste))
    (slot df)
    (slot dc)
)
(defglobal FIL_MAX = 3) #La primera Fila es 1.
(defglobal COL_MAX = 2) #La primera Columna es 1.


(defrule 
    (declare (salience 0))
    ?f0<-(baldosa (fil ?fbaldosa)(col ?cbaldosa)(estado Sucia))
    ?f1<-(robot(fil ?fbaldosa)(col ?cbaldosa)(tiempo ?tiempo))
    =>
    (modify ?f0(estado Limipia))
    (modify ?f1(timepo (+ ?tiempo 3)))
)

(defrule Avanzar
    ?f0<-(baldosa (fil ?fbaldosa)(col ?cbaldosa)(estado Limpia))
    ?f1<-(robot(fil ?frobot)(col ?crobot)(tiempo ?tiempo)(orientación ?orientacionrobot))
    a<-(avance (orientación ?ori) (df ?df) (dc ?dc) )
    (test (> ?*FIL_MAX* ?frobot))
    (test (< 1 ?frobot))
    (test (> ?*COL_MAX* ?crobot))
    (test (< 1 ?crobot))
    =>
    (modify ?f1 (fil (+ ?fil ?df) ) (col (+ ?col ?dc) ) )
)

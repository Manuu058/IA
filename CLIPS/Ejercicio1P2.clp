(defglobal ?*anyo* = 2025)
(defglobal ?*limite1* = 900)

(deftemplate usuario
    (slot dni_u)
    (slot pin)
    (slot obtener (default 0))
)

(deftemplate tarjeta
    (slot pin)
    (slot dni_t)
    (slot intentos (default 3))
    (slot limite (default 500))
    (slot expiracion (default 2030))
    (slot validada (allowed-values SI NO) (default NO))
)

(deftemplate cuenta
    (slot dni_c)
    (slot saldo)
    (slot estado (allowed-values enPantalla dineroEntregado Inicial SuperaLimite SinSaldo) (default Inicial))
)


(deffunction resta (?a)
    (bind ?numero (- ?a 1))
    (return ?numero)
)

(deffunction resta2 (?a ?b)
    (bind ?numero (- ?a ?b))
    (return ?numero)
)

(defrule supera_intentos
    (declare (salience 10))
    ?t <- (tarjeta (pin ?pin) (dni_t ?dni) (intentos ?intentos))
    (usuario (dni_u ?dni) (pin ?pin2&~?pin))
    (test (eq ?intentos 0))
    =>
    (println "Superaste los intentos")
    (retract ?t)
)

(defrule pin_invalido
    (declare (salience 8))
    ?t <- (tarjeta (pin ?pin) (dni_t ?dni) (intentos ?intentos))
    ?u <- (usuario (dni_u ?dni) (pin ?pin2))
    (test (neq ?pin ?pin2))
    (test (> ?intentos 0))
    =>
    
    (bind ?resultado (resta ?intentos))
    (modify ?t (intentos ?resultado))
    (retract ?u)
)

(defrule valida_tarjeta
    (declare (salience 6))
    ?t <- (tarjeta (pin ?pin) (dni_t ?dni) (intentos ?intentos) (expiracion ?expiracion) (validada ?validada))
    ?u <- (usuario (dni_u ?dni) (pin ?pin2))
    (test (eq ?pin ?pin2))
    (test (> ?intentos 0))
    (test (< ?*anyo* ?expiracion))
    (test (eq ?validada NO))
    =>
    (modify ?t (validada SI) (intentos 3))
)

(defrule muestra_saldo
    (tarjeta (dni_t ?dni) (validada ?validada))
    (usuario (dni_u ?dni))
    ?c <- (cuenta (dni_c ?dni) (estado ?est))
    (test (eq ?validada SI))
    (test (neq ?est enPantalla))
    =>
    (modify ?c (estado enPantalla))
)

(defrule Sin_Saldo
    (tarjeta (dni_t ?dni) (validada ?validada))
    ?u <- (usuario (dni_u ?dni) (obtener ?o))
    (cuenta (dni_c ?dni) (estado ?est) (saldo ?s))
    (test (> ?o ?s))
    (test (eq ?validada SI))
    (test (eq ?est enPantalla))
    =>
    (println "No tienes saldo")
    (retract ?u)
)

(defrule Comprueba_Limite1
    (tarjeta (dni_t ?dni) (validada ?validada))
    ?u <- (usuario (dni_u ?dni) (obtener ?o))
    ?c <- (cuenta (dni_c ?dni) (estado ?est) (saldo ?s))
    (test (> ?o ?*limite1*))
    (test (eq ?validada SI))
    (test (eq ?est enPantalla))
    =>
    (println "Lo siento se ha superado el limite establecido por el banco")
    (modify ?c (estado SuperaLimite))
    (retract ?u)
)

(defrule Comprueba_Limite2
    (tarjeta (dni_t ?dni) (validada ?validada) (limite ?l))
    ?u <- (usuario (dni_u ?dni) (obtener ?o))
    ?c <- (cuenta (dni_c ?dni) (estado ?est) (saldo ?s))
    (test (> ?o ?l))
    (test (eq ?validada SI))
    (test (eq ?est enPantalla))
    =>
    (println "Lo siento se ha superado el limite establecido por la tarjeta")
    (modify ?c (estado SuperaLimite))
    (retract ?u)
)

(defrule Entrega_Dinero
    (tarjeta (dni_t ?dni) (validada ?validada) (limite ?l))
    ?u <- (usuario (dni_u ?dni) (obtener ?o))
    ?c <- (cuenta (dni_c ?dni) (estado ?est) (saldo ?s))
    (test (<= ?o ?s))
    (test (eq ?est enPantalla))
    (test (eq ?validada SI))
    =>
    (bind ?n (resta2 ?s ?o))
    (modify ?c (saldo ?n) (estado dineroEntregado))
    (retract ?u)
)

(defrule interfaz
    (not (Usuario))
    =>
    (printout t "Escriba su DNI: ")
    (bind ?dni (read))
    (printout t "Escriba su Pin: ")
    (bind ?pin (read))
    (printout t "Escriba el importe que desea retirar: ")
    (bind ?importe (read))
    (assert(usuario(dni_u ?dni)(pin ?pin)(obtener ?importe)));Hacemos un assert con los datos
);interfaz

(deffacts inicio    
    (tarjeta
        (dni_t 123456)
        (pin 1212)
        (intentos 3)
        (limite 500)
        (expiracion 2000));Tarjeta Caducada
    (tarjeta
        (dni_t 456456)
        (pin 4545)
        (intentos 3)
        (limite 1000)
        (expiracion 2026))
    (tarjeta
        (dni_t 000111)
        (pin 0011)
        (intentos 0);Intentos gastados
        (limite 500)
        (expiracion 2026))
    (cuenta
        (dni_c 123456)
        (saldo 5000))
    (cuenta
        (dni_c 456456)
        (saldo 33))
    (cuenta
        (dni_c 000111)
        (saldo 30000))
);inicio
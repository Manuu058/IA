(deftemplate vias
    (slot idvia)
    (slot nombrevia)
    (slot numvehiculos(default 0))
)

(deftemplate semaforo
    (slot idsemaforo (allowed-values A B C D))
    (slot idvia)
    (slot estado (allowed-values Rojo Verde))
    (slot numvehiculos (default 0))
)

(deftemplate sensor
    (slot idcelula (allowed-values 1 2 3))
    (slot idsemaforo)
    (slot estado(allowed-values activada desactivada)(default desactivada))
    (slot matricula)
)

(deftemplate vehiculos
    (slot matricula)
    (slot tipo (allowed-values automovil camion motocicleta bicicleta))
    (slot idsemaforo)
    (slot accion(allowed-values llegando esperando cruzando realizado nada)(default nada))
)

(deffacts iniciales
    (vias (idvia V1)(nombrevia Avenida Constitución))
    (vias (idvia V2)(nombrevia Avenida Falla))
    (semaforo (idsemaforo A)(estado Verde))
    (semaforo (idsemaforo B)(estado Verde))
    (semaforo (idsemaforo D)(estado Rojo))
    (semaforo (idsemaforo C)(estado Rojo))
    (sensor (idcelula 1)(idsemaforo A))
    (sensor (idcelula 2)(idsemaforo A))
    (sensor (idcelula 3)(idsemaforo A))
)

(defrule sensor1_llegar
    ?f0 <- (vias (idvia ?idvia)(nombrevia ?nombrevia))
    ?f1 <- (semaforo (idsemaforo ?idsemaforo)(idvia ?idvia))
    ?f2 <- (sensor (idcelula 1)(idsemaforo ?idsemaforo)
                   (estado desactivada))
    ?f3 <- (activar_sensor 1 ?idsemaforo ?matricula ?tipo)
    =>
    (assert (vehiculos (matricula ?matricula)
                       (tipo ?tipo)
                       (idsemaforo ?idsemaforo)
                       (accion llegando)))

    (printout t "El vehiculo " ?matricula
               " esta llegando al semaforo "
               ?idsemaforo crlf)

    (modify ?f2 (estado activada)(matricula ?matricula))

    (printout t "El sensor 1 del semaforo "
               ?idsemaforo
               " acaba de ser activado por el/la "
               ?tipo " con matricula "
               ?matricula
               " en la via "
               ?nombrevia crlf)

    (retract ?f3)
)

(defrule cambio_rojo
    ?f0<-(cambia_color ?f Rojo)
    ?f1<-(semaforo(idsemaforo ?f)(idvia ?idvia)(estado Verde)(numvehiculos ?nv))
    ?f2<-(vias (idvia ?idvia)(numvehiculos ?nt))
    =>
    (modify ?f2 (numvehiculos (+ ?nv ?nt)))
    (modify ?f1 (estado Rojo)(numvehiculos 0))
    (retract ?f0)
)

(defrule cruzando_vehiculo
    (declare (salience 10))
    ?f0<-(semaforo (idsemaforo ?idsemaforo)(idvia ?idvia)(estado Verde)(numvehiculos ?nv))
    ?f1<-(vehiculos(matricula ?matricula)(idsemaforo ?idsemaforo)(accion llegando|esperando)(tipo ?tipo))
    ?f2<-(vias(idvia ?idvia)(nombrevia ?nombre))
    ?f3<-(vias(idvia ?idvia2)(nombrevia ?nombre2))
    (test (neq ?idvia ?idvia2))
    =>
    (modify ?f1 (accion cruzando))
    (printout t "El/la "
               ?tipo
               " con matricula "
               ?matricula
               " esta cruzando la via "
               ?nombre
               " con la via "
               ?nombre2 crlf)
    (modify ?f0 (numvehiculos (+ 1 ?nv)))
)

(defrule situacion_actual
    ?f0<-(situacion semaforo)
    (vias (idvia ?idvia)(nombrevia ?nombrevia)(numvehiculos ?numvehiculostotal))
    (semaforo(idsemaforo ?idsemaforo)(idvia ?idvia)(numvehiculos ?numvehiculossemaforo))
    (semaforo(idsemaforo ?idsemaforo2&~?idsemaforo)(idvia ?idvia2)(numvehiculos ?numvehiculossemaforo2))
    =>
     (printout t "Semaforos "
               ?idsemaforo
               " y "
               ?idsemaforo2
               " estan en "
               ?estado
               " han pasado "
               ?numvehiculostotal
               " vehiculos por la via "
               ?nombrevia crlf)

    (retract ?f0)
)
import random


class Escoba ():

    def __init__(self):

        self.turno = True

        self.manoJugador = []
        self.manoPC = []

        self.mesa = []

        self.puntajeJugador = 0
        self.puntajePC = 0

        self.cantidadCartasJugador = 0
        self.cantidadCartasPC = 0

        self.cantidadOroJugador = 0
        self.cantidadOroPC = 0

        self.cantidadEscobaJugador = 0
        self.cantidadEscobaPC = 0

        self.cantidadSietesJugador = 0
        self.cantidadSietesPC = 0

        self.el7lotiene = ""

        self.mazo = [(1, "o"),
                     (2, "o"),
                     (3, "o"),
                     (4, "o"),
                     (5, "o"),
                     (6, "o"),
                     (7, "o"),
                     (8, "o"),
                     (9, "o"),
                     (10, "o"),
                     (1, "e"),
                     (2, "e"),
                     (3, "e"),
                     (4, "e"),
                     (5, "e"),
                     (6, "e"),
                     (7, "e"),
                     (8, "e"),
                     (9, "e"),
                     (10, "e"),
                     (1, "c"),
                     (2, "c"),
                     (3, "c"),
                     (4, "c"),
                     (5, "c"),
                     (6, "c"),
                     (7, "c"),
                     (8, "c"),
                     (9, "c"),
                     (10, "c"),
                     (1, "b"),
                     (2, "b"),
                     (3, "b"),
                     (4, "b"),
                     (5, "b"),
                     (6, "b"),
                     (7, "b"),
                     (8, "b"),
                     (9, "b"),
                     (10, "b"),
                     ]

    def sacarCartas(self, cj, cm):
        # Sumo los valores de las cartas
        self.suma = int(cj[0])
        for item in cm:
            self.suma += int(item[0])

        if self.turno:
            # Verifico si saque cartas de la mesa
            if not cm:
                self.manoJugador.remove(cj)  # le saco la carta al jugador
                self.mesa.append(cj)  # Pongo la carta en la mesa
                self.cambiarTurno()  # Termina el turno
                return True

            # Verifico que la carta exista en la mano de el jugador
            # y en la mesa y si sus valores suman 15
            elif (cj in self.manoJugador
                  and all(items in self.mesa for items in cm)
                  and self.suma == 15):
                self.manoJugador.remove(cj)  # le saco la carta al jugador
                for item in cm:  # Saco las cartas de la mesa
                    self.mesa.remove(item)
                self.contarCartas(cj, cm)  # Cuento los puntos que gane
                self.cambiarTurno()  # Termina el turno
                return True
            else:
                return False
        else:
            # Verifico si saque cartas de la mesa
            if not cm:
                self.manoPC.remove(cj)  # le saco la carta al jugador
                self.mesa.append(cj)  # Pongo la carta en la mesa
                self.cambiarTurno()  # Termina el turno
                return True

            # Verifico que la carta exista en la mano de PC
            # y en la mesa y si sus valores suman 15
            elif (cj in self.manoPC
                  and all(items in self.mesa for items in cm)
                  and self.suma == 15):
                self.manoPC.remove(cj)  # le saco la carta a PC
                for item in cm:  # Saco las cartas de la mesa
                    self.mesa.remove(item)
                self.contarCartas(cj, cm)  # Cuento los puntos que gane
                self.cambiarTurno()  # Termina el turno
                return True
            else:
                return False

    def contarCartas(self, cj, cm):

        # Verifico si es el turno de el jugador o no
        if self.turno:

            # Le sumo las cartas que saque de la mesa mas la de mi mano
            self.cantidadCartasJugador += len(cm) + 1

            # Verifico si saque el 7 de oro
            if (7, "o") == cj or (7, "o") in cm:
                self.puntajeJugador += 1
                self.el7lotiene = "j"

            for item in cm:
                # Sumo la cantidad de oros que saque de la mesa
                if item[1] == "o":
                    self.cantidadOroJugador += 1
                # Sumo la cantidad de sietes saque de la mesa
                if item[0] == 7:
                    self.cantidadSietesJugador += 1

            # Si la carta que estaba en mi mano era oro sumo 1
            if cj[1] == "o":
                self.cantidadOroJugador += 1
            # Si la carta que estaba en mi mano era un 7 sumo 1
            if cj[0] == 7:
                self.cantidadSietesJugador += 1

            # Verifico si el jugador saco todas las cartas de la mesa
            if len(self.mesa) == 0:
                self.cantidadEscobaJugador += 1

        # Si no es el turno del jugador
        else:
            # Le sumo las cartas que saco de la mesa mas la de su mano
            self.cantidadCartasPC += len(cm) + 1

            # Verifico si saco el 7 de oro
            if (7, "o") == cj or (7, "o") in cm:
                self.puntajePC += 1

            for item in cm:
                # Sumo la cantidad de oros que saco de la mesa
                if item[1] == "o":
                    self.cantidadOroPC += 1
                # Sumo la cantidad de sietes que saco de la mesa
                if item[0] == 7:
                    self.cantidadSietesPC += 1

            # Si la carta que estaba en su mano era oro sumo 1
            if cj[1] == "o":
                self.cantidadOroPC += 1
            # Si la carta que estaba en su mano era un 7 sumo 1
            if cj[0] == 7:
                self.cantidadSietesPC += 1

            # Verifico si PC saco todas las cartas de la mesa
            if len(self.mesa) == 0:
                self.cantidadEscobaPC += 1

    def repartir(self):

        # Reparto 3 cartas a cada uno y saco esas cartas del mazo
        for i in range(3):
            self.manoJugador.append(self.mazo.pop(random.randint(0, len(self.mazo))-1))
            self.manoPC.append(self.mazo.pop(random.randint(0, len(self.mazo))-1))

        # Si no hay cartas en la mesa agrego 4 y las saco del mazo
        if len(self.mesa) == 0:
            for i in range(4):
                self.mesa.append(self.mazo.pop(random.randint(0, len(self.mazo))-1))
            temp = []
            for item in self.mesa:
                temp.append(item[0])
            if sum(temp) == 15:
                if len(self.mazo) == 30:
                    self.EscobaReal = 2
                else:
                    self.EscobaReal = 1
                if self.turno:
                    self.cantidadPuntosPC += self.EscobaReal
                    self.cantidadCartasPC += len(self.mesa)
                else:
                    self.cantidadPuntosJugador += self.EscobaReal
                    self.cantidadCartasJugador += len(self.mesa)
                self.mesa = []  # Saco todas las cartas de la mesa

    # Cambia de el turno de el jugador al de PC y viceversa
    def cambiarTurno(self):
        if self.turno:
            self.turno = False
        else:
            self.turno = True

    def ganar(self):

        # Si el mazo, la mesa, la mano del jugador y
        # la mano de PC tiene mas de 0 cartas, el juego sigue
        if (len(self.mazo) > 0 or len(self.manoJugador) > 0 or len(self.manoPC) > 0):
            return False

        # Si no hay cartas en el mazo
        else:

            self.contarCartas((0, ""), self.mesa)
            self.mesa = []

            # Sumar un punto al que tenga mas cartas
            if self.cantidadCartasJugador == self.cantidadCartasPC:
                pass
            elif self.cantidadCartasJugador > self.cantidadCartasPC:
                self.puntajeJugador += 1
            else:
                self.puntajePC += 1

            # Sumar un punto por cada escoba
            self.puntajeJugador += self.cantidadEscobaJugador
            self.puntajePC += self.cantidadEscobaPC

            # Sumar un punto al que tenga mas oro
            if self.cantidadOroJugador == self.cantidadOroPC:
                pass
            elif self.cantidadOroJugador > self.cantidadOroPC:
                self.puntajeJugador += 1
            else:
                self.puntajePC += 1

            # Sumar un punto al que tenga mas sietes
            if self.cantidadSietesJugador == self.cantidadSietesPC:
                if self.el7lotiene == "j":
                    self.puntajeJugador += 1
                else:
                    self.puntajePC += 1
            elif self.cantidadSietesJugador > self.cantidadSietesPC:
                self.puntajeJugador += 1
            else:
                self.puntajePC += 1

            return True

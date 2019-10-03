import random
import itertools

from Escoba import Escoba


class Ingresar (Escoba):

    def __init__(self):
        Escoba.__init__(self)

    def validar(self, cj, cm):

        try:
            self.cjugador = (int(cj[:-1]), cj[-1:])
            self.cmesa = []
            for item in cm.split():
                self.cmesa.append((int(item[:-1]), item[-1:]))
            if all(items in self.mesa for items in self.cmesa):
                return True
            else:
                return False
        except:
            return False

    def juegaPC(self):
        while not self.turno:
            self.posiblejugada = []
            self.cartasm = []
            self.cartausada = []
            self.combinaciones = []
            self.listasuma = []

            for i in range(1, len(self.mesa)+1):
                self.combinaciones += list(itertools.combinations(self.mesa, i))
            for i in range(len(self.combinaciones)):
                self.combinaciones[i] = list(self.combinaciones[i])

            for item in self.combinaciones:
                x = 0
                for jtem in item:
                    x += jtem[0]
                self.listasuma.append(x)

            for carta in self.manoPC:
                for i in range(len(self.listasuma)):
                    if carta[0] + self.listasuma[i] == 15:
                        self.posiblejugada.append(self.combinaciones[i])
                        self.cartausada.append(carta)
            if len(self.posiblejugada) > 0:
                self.cartasm = list(max(self.posiblejugada))
                self.cartaspc = self.cartausada[self.posiblejugada.index(max(self.posiblejugada))]
            else:
                self.cartaspc = self.manoPC[random.randint(0, len(self.manoPC))-1]

            if self.sacarCartas(self.cartaspc, self.cartasm):
                if len(self.cartasm) > 0:
                    return "PC saco las cartas {} y uso la carta {}".format(self.cartasm, self.cartaspc)
                else:
                    return "PC dejo la carta {}".format(self.cartaspc)

    def imprimirCartas(self):
        for carta in self.mesa:
            print(carta, end=" ")

        if self.turno:
            for carta in self.manoJugador:
                print("\n", carta, end=" ")
        # else:
        #     for carta in self.manoPC:
        #         print("\n", carta, end=" ")

    def jugar(self):
        while not self.ganar():
            if self.manoJugador == [] and self.manoPC == []:
                self.repartir()
            if self.turno:
                self.imprimirCartas()
                self.cartasj = input("Ingrese su carta   ")
                self.cartasm = input("Ingrese las cartas de la mesa    ")
                print("\n")
                if not (self.validar(self.cartasj, self.cartasm)
                   and self.sacarCartas(self.cjugador, self.cmesa)):
                    print("Ingrese cartas validas\n")
            else:
                self.imprimirCartas()
                print("\n\n", self.juegaPC(), "\n")

        print("\nCantidad de cartas del jugador", self.cantidadCartasJugador)
        print("\nCantidad de cartas de PC", self.cantidadCartasPC)
        print("\n\nCantidad de oro del jugador", self.cantidadOroJugador)
        print("\nCantidad de oro de PC", self.cantidadOroPC)
        print("\n\nCantidad de escobas del jugador", self.cantidadEscobaJugador)
        print("\nCantidad de escobas de PC", self.cantidadEscobaPC)
        print("\n\nCantidad de sietes del jugador", self.cantidadSietesJugador)
        print("\nCantidad de sietes de PC", self.cantidadSietesPC)
        if self.el7lotiene == "j":
            print("\n\nEl Jugador tiene el 7 de oro")
        else:
            print("\nPC tiene el 7 de oro")
        print("\n\nPuntaje Jugador:", self.puntajeJugador, "\n")
        print("Puntaje PC:", self.puntajePC, "\n")


# juego = Ingresar()
# juego.jugar()

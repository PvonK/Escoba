import unittest

from Escoba import Escoba


class TestEscoba(unittest.TestCase):

    def test_Escoba_1(self):
        juego = Escoba()
        juego.mazo = [(7, "o"), (3, "b"), (4, "e"), (7, "b"), (9, "c"), (1, "e")]
        juego.manoJugador = [(3, "c"), (7, "c")]
        juego.manoPC = [(1, "c")]
        juego.mesa = [(2, "o"), (6, "b"), (4, "e")]

        self.assertTrue(juego.sacarCartas((3, "c"), [(2, "o"), (6, "b"), (4, "e")]))

    def test_Escoba_2(self):
        juego = Escoba()
        juego.mazo = [(7, "o"), (3, "b"), (4, "e"), (7, "b"), (9, "c"), (1, "e")]
        juego.manoJugador = [(3, "c"), (7, "c")]
        juego.manoPC = []
        juego.mesa = [(2, "o"), (6, "b"), (4, "e")]

        self.assertFalse(juego.sacarCartas("4c", [(4, "o"), (6, "b"), (4, "e")]))

    def test_Escoba_3(self):
        juego = Escoba()
        juego.mazo = []
        juego.manoJugador = [(1, "o")]
        juego.manoPC = []
        juego.mesa = [(8, "c"), (6, "b")]

        juego.sacarCartas("1o", [(8, "c"), (6, "b")])
        self.assertTrue(juego.ganar())

    def test_Escoba_4(self):
        juego = Escoba()
        juego.mazo = [(7, "o"), (3, "b"), (4, "e"), (7, "b"), (9, "c"), (1, "e")]
        juego.manoJugador = [(3, "c"), (7, "c")]
        juego.manoPC = []
        juego.mesa = [(2, "o"), (6, "b"), (4, "e")]

        juego.sacarCartas("3c", [(2, "o"), (6, "o"), (4, "e")])
        self.assertFalse(juego.ganar())



if __name__ == '__main__':
    unittest.main()

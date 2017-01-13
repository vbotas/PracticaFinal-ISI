from carcassonne import *
import unittest

class Test_basico(unittest.TestCase):

    def test_comprobar_numero_jugadores(self):
        jugadores = ['Paco','Ana']
        expected = True
        self.assertEqual(expected, Partida().num_jug_correcto(jugadores))

    def test_comprobar_numero_jugadores2(self):
        jugadores = ['Paco','Ana','Maria','Jose','Sergio']
        expected = False
        self.assertEqual(expected, Partida().num_jug_correcto(jugadores))

    def test_comprobar_nombres(self):
        jugadores = ['Paco','Ana','Maria']
        expected = True
        self.assertEqual(expected, Partida().nombres_jug_correcto(jugadores))

    def test_comprobar_nombres2(self):
        jugadores = ['Paco','Ana','Maria','Paco']
        expected = False
        self.assertEqual(expected, Partida().nombres_jug_correcto(jugadores))

    def test_inicializar_jugador(self):
        expected = 'Paco'
        jugador1 = Jugador(expected)
        self.assertEqual(expected, jugador1.nombre)

    def test_inicializar_jugador2(self):
        expected = 'Paco'
        jugador2 = Jugador('Ana')
        self.assertNotEqual(expected, jugador2.nombre)

if __name__ == '__main__':
    unittest.main()

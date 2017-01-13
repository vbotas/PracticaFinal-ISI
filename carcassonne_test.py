import unittest
from carcassonne import *


class Test_basico(unittest.TestCase):

    def test_comprobar_numero_jugadores(self):
        jugadores = ['Paco','Ana']
        expected = True
        self.assertEqual(expected, Partida.num_jug_correcto(jugadores))

    def test_comprobar_numero_jugadores(self):
        jugadores = ['Paco','Ana','Maria','Jose','Sergio']
        expected = False
        self.assertEqual(expected, Partida.num_jug_correcto(jugadores))

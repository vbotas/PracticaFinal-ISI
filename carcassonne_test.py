import unittest
from carcassonne import *


class Test_basico(unittest.TestCase):
     
    def test_hay_partida (self):
        ## Test para comprobar que existe la clase Partida
        partida = Partida()
        
    def test_numero_jugadores (self):
        """ Test para comprobar que el número de jugadores es 2, se puede modificar el numero de jugadores en un futuro,
        asumimos que esta partida será de 1vs1 al principio"""
        partida = Partida()
        self.assertEqual(partida.jugadores,2 , "No hay 2 jugadores") 

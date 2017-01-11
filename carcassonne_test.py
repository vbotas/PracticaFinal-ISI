import unittest
from carcassonne import *


class Test_basico(unittest.TestCase):
     
    def setUp(self):
        self.partida = Partida(jugador1='pedro', jugador2='juan')
        
    def test_hay_partida (self):
        ## Test para comprobar que existe la clase Partida
        jug1 = self.partida.jugador1
        jug2 = self.partida.jugador2
        self.assertEqual(jug1, 'pedro', msg="Algo ha fallado al crear al jugador 1")
        self.assertEqual(jug2, 'juan', msg="Algo ha fallado al crear al jugador 2")
        
    def test_numero_jugadores (self):
        numero_jugadores = self.partida.jugadores
        self.assertEqual(numero_jugadores,2 , "No hay 2 jugadores") 
        
    def test_piezas_territorio(self):
        numero_piezas_territorio = self.partida.piezas_territorio
        self.assertEqual(numero_piezas_territorio, 72, msg="No hay las piezas de territorio necesarias para comenzar")
    
    def test_meeples_jugadores(self):
        meeples_por_jugador = self.partida.meeple_jugador
        self.assertEqual(meeples_por_jugador, 8, msg="El numero de meeples por jugador no es correcto")

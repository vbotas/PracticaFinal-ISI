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

    def test_meeples_jugadores(self):
        #test para comprobar que el numero de meeples es correcto al no ser superior a 8
        jugador = Jugador('Paco')
        meeples_jugador = jugador.meeples
        self.assertLessEqual(meeples_jugador, 8, msg="El numero de meeples por jugador no es correcto")
        
    def test_marcador_jugador(self):
        # test para comprobar que el marcador no es negativo
        jugador = Jugador('Paco')
        puntuacion_jug = jugador.puntuacion
        self.assertGreaterEqual(puntuacion_jug, 0, msg="Marcador incorrecto")

if __name__ == '__main__':
    unittest.main()

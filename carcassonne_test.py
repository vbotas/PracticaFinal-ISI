from carcassonne import *
import unittest

class Test_basico(unittest.TestCase):

    # Test que comprueba que el numero de jugadores es correcto
    def test_comprobar_numero_jugadores(self):
        jugadores = ['Paco','Ana']
        expected = True
        self.assertEqual(expected, Partida().num_jug_correcto(jugadores))

    # Test que comprueba que el numero de jugadores es incorrecto
    def test_comprobar_numero_jugadores2(self):
        jugadores = ['Paco','Ana','Maria','Jose','Sergio']
        expected = False
        self.assertEqual(expected, Partida().num_jug_correcto(jugadores))

    # Test que comprueba que el numero de jugadores es incorrecto
    def test_comprobar_numero_jugadores2(self):
        jugadores = ['Paco']
        expected = False
        self.assertEqual(expected, Partida().num_jug_correcto(jugadores))

    # Test que comprueba que los nombres no se repiten
    def test_comprobar_nombres(self):
        jugadores = ['Paco','Ana','Maria']
        expected = True
        self.assertEqual(expected, Partida().nombres_jug_correcto(jugadores))

    # Test que comprueba que los nombres se repiten
    def test_comprobar_nombres2(self):
        jugadores = ['Paco','Ana','Maria','Paco']
        expected = False
        self.assertEqual(expected, Partida().nombres_jug_correcto(jugadores))

    # Test que comprueba que un jugador se inicializa correctamente
    def test_inicializar_jugador(self):
        expected = 'Paco'
        jugador1 = Jugador(expected)
        self.assertEqual(expected, jugador1.nombre)

    # Test que comprueba que un jugador se inicializa correctamente
    def test_inicializar_jugador2(self):
        expected = 'Paco'
        jugador2 = Jugador('Ana')
        self.assertNotEqual(expected, jugador2.nombre)

    # test para comprobar que el numero de meeples es correcto al no ser superior a 8
    def test_meeples_jugadores(self):
        jugador = Jugador('Paco')
        meeples_jugador = jugador.meeples
        self.assertLessEqual(meeples_jugador, 8, msg="El numero de meeples por jugador no es correcto")

    # test para comprobar que el marcador no es negativo
    def test_marcador_jugador(self):
        jugador = Jugador('Paco')
        puntuacion_jug = jugador.puntuacion
        self.assertGreaterEqual(puntuacion_jug, 0, msg="Marcador incorrecto")

    # test que comprueba que los jugadores se inicializan correctamente
    def test_inicializar_jugadores(self):
        jugador1 = 'Paco'
        jugador2 = 'Ana'
        jugadores = Partida().inicializar_jugadores([jugador1,jugador2])
        self.assertEqual(jugador1, jugadores[0].nombre)
        self.assertEqual(jugador2, jugadores[1].nombre)
        

if __name__ == '__main__':
    unittest.main()

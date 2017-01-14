from carcassonne import *
import unittest

class Test_basico(unittest.TestCase):

    # Test que comprueba que el numero de jugadores es correcto
    def test_comprobar_numero_jugadores(self):
        jugadores = ['Paco','Ana']
        self.assertTrue(Partida().num_jug_correcto(jugadores))

    # Test que comprueba que el numero de jugadores es incorrecto
    def test_comprobar_numero_jugadores2(self):
        jugadores = ['Paco','Ana','Maria','Jose','Sergio']
        self.assertFalse(Partida().num_jug_correcto(jugadores))

    # Test que comprueba que el numero de jugadores es incorrecto
    def test_comprobar_numero_jugadores3(self):
        jugadores = ['Paco']
        self.assertFalse(Partida().num_jug_correcto(jugadores))

    # Test que comprueba que los nombres no se repiten
    def test_comprobar_nombres(self):
        jugadores = ['Paco','Ana','Maria']
        self.assertTrue(Partida().nombres_jug_correcto(jugadores))

    # Test que comprueba que los nombres se repiten
    def test_comprobar_nombres2(self):
        jugadores = ['Paco','Ana','Maria','Paco']
        self.assertFalse(Partida().nombres_jug_correcto(jugadores))

    # Test que comprueba que el nombre de un jugador se inicializa correctamente
    def test_inicializar_jugador(self):
        expected = 'Paco'
        jugador1 = Jugador(expected)
        self.assertEqual(expected, jugador1.nombre)

    # Test que comprueba que el nombre de un jugador se inicializa correctamente
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

    # test para comprobar que se instancio correctamente
    def test_instanciar_jugador(self):
        jugador = Jugador('Paco')
        self.assertIsInstance(jugador,Jugador)

    # test que comprueba que los jugadores se inicializan correctamente
    def test_inicializar_jugadores(self):
        jugador1 = 'Paco'
        jugador2 = 'Ana'
        jugadores = Partida().inicializar_jugadores([jugador1,jugador2])
        self.assertEqual(jugador1, jugadores[0].nombre)
        self.assertEqual(jugador2, jugadores[1].nombre)

    # Test para comprobar que la posicion de la pieza de tipo 1 se inicializa correctamente
    def test_inicializar_pieza1(self):
        pieza1 = ['Granja','Granja','Camino','Camino']
        pieza = Pieza_terreno(1)
        self.assertItemsEqual(pieza1, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 2 se inicializa correctamente
    def test_inicializar_pieza2(self):
        pieza2 = ['Camino','Granja','Camino','Granja']
        pieza = Pieza_terreno(2)
        self.assertItemsEqual(pieza2, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 3 se inicializa correctamente
    def test_inicializar_pieza3(self):
        pieza3 = ['Castillo','Camino','Camino','Castillo']
        pieza = Pieza_terreno(3)
        self.assertItemsEqual(pieza3, pieza.posicion)
 
    # Test para comprobar que la posicion de la pieza de tipo 4 se inicializa correctamente
    def test_inicializar_pieza4(self):
        pieza4 = ['Castillo','Granja','Granja','Castillo']
        pieza = Pieza_terreno(4)
        self.assertItemsEqual(pieza4, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 5 se inicializa correctamente
    def test_inicializar_pieza5(self):
        pieza5 = ['Granja','Castillo','Granja','Granja']
        pieza = Pieza_terreno(5)
        self.assertItemsEqual(pieza5, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 6 se inicializa correctamente
    def test_inicializar_pieza6(self):
        pieza6 = ['Castillo','Castillo','Granja','Castillo']
        pieza = Pieza_terreno(6)
        self.assertItemsEqual(pieza6, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 7 se inicializa correctamente
    def test_inicializar_pieza7(self):
        pieza7 = ['Granja','Camino','Camino','Camino']
        pieza = Pieza_terreno(7)
        self.assertItemsEqual(pieza7, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 8 se inicializa correctamente
    def test_inicializar_pieza8(self):
        pieza8 = ['Granja','Granja','Granja','Granja'] ##ESTA FIGURA TIENE UN MONASTERIO EN EL CENTRO
        pieza = Pieza_terreno(8)
        self.assertItemsEqual(pieza8, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 9 se inicializa correctamente
    def test_inicializar_pieza9(self):
        pieza9 = ['Granja','Castillo','Granja','Castillo']
        pieza = Pieza_terreno(9)
        self.assertItemsEqual(pieza9, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 10 se inicializa correctamente
    def test_inicializar_pieza10(self):
        pieza10 = ['Camino','Castillo','Camino','Granja']
        pieza = Pieza_terreno(10)
        self.assertItemsEqual(pieza10, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 11 se inicializa correctamente
    def test_inicializar_pieza11(self):
        pieza11 = ['Camino','Castillo','Camino','Camino']
        pieza = Pieza_terreno(11)
        self.assertItemsEqual(pieza11, pieza.posicion)
 
    # Test para comprobar que la posicion de la pieza de tipo 12 se inicializa correctamente
    def test_inicializar_pieza12(self):
        pieza12 = ['Castillo','Castillo','Camino','Castillo']
        pieza = Pieza_terreno(12)
        self.assertItemsEqual(pieza12, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 13 se inicializa correctamente
    def test_inicializar_pieza13(self):
        pieza13 = ['Castillo','Camino','Camino','Granja']
        pieza = Pieza_terreno(13)
        self.assertItemsEqual(pieza13, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 14 se inicializa correctamente
    def test_inicializar_pieza14(self):
        pieza14 = ['Camino','Castillo','Granja','Camino']
        pieza = Pieza_terreno(14)
        self.assertItemsEqual(pieza14, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 15 se inicializa correctamente
    def test_inicializar_pieza15(self):
        pieza15 = ['Castillo','Granja','Castillo','Granja']
        pieza = Pieza_terreno(15)
        self.assertItemsEqual(pieza15, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 16 se inicializa correctamente
    def test_inicializar_pieza16(self):
        pieza16 = ['Granja','Castillo','Castillo','Granja']
        pieza = Pieza_terreno(16)
        self.assertItemsEqual(pieza16, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 17 se inicializa correctamente
    def test_inicializar_pieza17(self):
        pieza17 = ['Granja','Granja','Camino','Granja'] ## ESTA FIGURA TIENE UN MONASTERIO EN EL CENTRO
        pieza = Pieza_terreno(17)
        self.assertItemsEqual(pieza17, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 18 se inicializa correctamente
    def test_inicializar_pieza18(self):
        pieza18 = ['Camino','Camino','Camino','Camino']
        pieza = Pieza_terreno(18)
        self.assertItemsEqual(pieza18, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 19 se inicializa correctamente
    def test_inicializar_pieza19(self):
        pieza19 = ['Castillo','Castillo','Castillo','Castillo']
        pieza = Pieza_terreno(19)
        self.assertItemsEqual(pieza19, pieza.posicion)

    # Test para comprobar que se inicializan correctamente las coordenadas de cada pieza
    def test_inicializar_coordenadas_pieza(self):
        coordenadas = [None,None]
        pieza = Pieza_terreno(1)
        self.assertItemsEqual(coordenadas, pieza.coordenadas)

    # Test para comprobar que la pieza 1 se repite tantas veces como sea necesario
    def test_repetir_pieza1(self):
        pieza = Pieza_terreno(1)
        repeticion = 9
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 2 se repite tantas veces como sea necesario
    def test_repetir_pieza2(self):
        pieza = Pieza_terreno(2)
        repeticion = 8
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 3 se repite tantas veces como sea necesario
    def test_repetir_pieza3(self):
        pieza = Pieza_terreno(3)
        repeticion = 5
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))
 
    # Test para comprobar que la pieza 4 se repite tantas veces como sea necesario
    def test_repetir_pieza4(self):
        pieza = Pieza_terreno(4)
        repeticion = 5
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 5 se repite tantas veces como sea necesario
    def test_repetir_pieza5(self):
        pieza = Pieza_terreno(5)
        repeticion = 5
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 6 se repite tantas veces como sea necesario
    def test_repetir_pieza6(self):
        pieza = Pieza_terreno(6)
        repeticion = 4
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 7 se repite tantas veces como sea necesario
    def test_repetir_pieza7(self):
        pieza = Pieza_terreno(7)
        repeticion = 4
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 8 se repite tantas veces como sea necesario
    def test_repetir_pieza8(self):
        pieza = Pieza_terreno(8)
        repeticion = 4
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 9 se repite tantas veces como sea necesario
    def test_repetir_pieza9(self):
        pieza = Pieza_terreno(9)
        repeticion = 3
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 10 se repite tantas veces como sea necesario
    def test_repetir_pieza10(self):
        pieza = Pieza_terreno(10)
        repeticion = 3
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 11 se repite tantas veces como sea necesario
    def test_repetir_pieza11(self):
        pieza = Pieza_terreno(11)
        repeticion = 3
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))
 
    # Test para comprobar que la pieza 12 se repite tantas veces como sea necesario
    def test_repetir_pieza12(self):
        pieza = Pieza_terreno(12)
        repeticion = 3
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 13 se repite tantas veces como sea necesario
    def test_repetir_pieza13(self):
        pieza = Pieza_terreno(13)
        repeticion = 3
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 14 se repite tantas veces como sea necesario
    def test_repetir_pieza14(self):
        pieza = Pieza_terreno(14)
        repeticion = 3
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 15 se repite tantas veces como sea necesario
    def test_repetir_pieza15(self):
        pieza = Pieza_terreno(15)
        repeticion = 3
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 16 se repite tantas veces como sea necesario
    def test_repetir_pieza16(self):
        pieza = Pieza_terreno(16)
        repeticion = 2
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 17 se repite tantas veces como sea necesario
    def test_repetir_pieza17(self):
        pieza = Pieza_terreno(17)
        repeticion = 2
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 18 se repite tantas veces como sea necesario
    def test_repetir_pieza18(self):
        pieza = Pieza_terreno(18)
        repeticion = 1
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que la pieza 19 se repite tantas veces como sea necesario
    def test_repetir_pieza19(self):
        pieza = Pieza_terreno(19)
        repeticion = 1
        self.assertEqual(repeticion, len(pieza.repetir_pieza()))

    # Test para comprobar que cada repeticion es una instancia de una pieza
    def test_repetir_pieza_instancia(self):
        pieza = Pieza_terreno(2)
        piezas_repetidas = pieza.repetir_pieza()
        self.assertIsInstance(piezas_repetidas[1],Pieza_terreno)

    # Test que comprueba la longitud de la baraja inicializada
    def test_inicializar_baraja_longitud(self):
        long_baraja = 71
        self.assertEqual(long_baraja, len(Partida().inicializar_baraja()))

    # Test que comprueba que comprueba si las piezas aparecen ordenadas (comprobacion de la primera)
    def test_inicializar_baraja(self):
        baraja = Partida().inicializar_baraja()
        self.assertEqual(1, baraja[0].tipo)

    # Test que comprueba que comprueba si las piezas aparecen ordenadas (comprobacion de la ultima)
    def test_inicializar_baraja(self):
        baraja = Partida().inicializar_baraja()
        self.assertEqual(19, baraja[-1].tipo)



if __name__ == '__main__':
    unittest.main()

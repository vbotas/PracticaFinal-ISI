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
        pieza1 = ['Granja','Granja','Granja','Granja','Camino','Granja','Camino','Granja','']
        pieza = Pieza_terreno(1)
        self.assertItemsEqual(pieza1, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 2 se inicializa correctamente
    def test_inicializar_pieza2(self):
        pieza2 = ['Camino','Granja','Granja','Granja','Camino','Granja','Granja','Granja','']
        pieza = Pieza_terreno(2)
        self.assertItemsEqual(pieza2, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 3 se inicializa correctamente
    def test_inicializar_pieza3(self):
        pieza3 = ['Castillo','Castillo','Camino','Granja','Camino','Castillo','Castillo','Castillo','']
        pieza = Pieza_terreno(3)
        self.assertItemsEqual(pieza3, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 4 se inicializa correctamente
    def test_inicializar_pieza4(self):
        pieza4 = ['Castillo','Castillo','Granja','Granja','Granja','Castillo','Castillo','Castillo','']
        pieza = Pieza_terreno(4)
        self.assertItemsEqual(pieza4, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 5 se inicializa correctamente
    def test_inicializar_pieza5(self):
        pieza5 = ['Granja','Castillo','Castillo','Castillo','Granja','Granja','Granja','Granja','']
        pieza = Pieza_terreno(5)
        self.assertItemsEqual(pieza5, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 6 se inicializa correctamente
    def test_inicializar_pieza6(self):
        pieza6 = ['Castillo','Castillo','Castillo','Castillo','Granja','Castillo','Castillo','Castillo','']
        pieza = Pieza_terreno(6)
        self.assertItemsEqual(pieza6, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 7 se inicializa correctamente
    def test_inicializar_pieza7(self):
        pieza7 = ['Granja','Granja','Camino','Granja','Camino','Granja','Camino','Granja','']
        pieza = Pieza_terreno(7)
        self.assertItemsEqual(pieza7, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 8 se inicializa correctamente
    def test_inicializar_pieza8(self):
        pieza8 = ['Granja','Granja','Granja','Granja','Granja','Granja','Granja','Granja','Monasterio'] ##ESTA FIGURA TIENE UN MONASTERIO EN EL CENTRO
        pieza = Pieza_terreno(8)
        self.assertItemsEqual(pieza8, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 9 se inicializa correctamente
    def test_inicializar_pieza9(self):
        pieza9 = ['Granja','Castillo','Castillo','Castillo','Granja','Castillo','Castillo','Castillo','']
        pieza = Pieza_terreno(9)
        self.assertItemsEqual(pieza9, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 10 se inicializa correctamente
    def test_inicializar_pieza10(self):
        pieza10 = ['Camino','Castillo','Castillo','Castillo','Camino','Granja','Granja','Granja','']
        pieza = Pieza_terreno(10)
        self.assertItemsEqual(pieza10, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 11 se inicializa correctamente
    def test_inicializar_pieza11(self):
        pieza11 = ['Camino','Castillo','Castillo','Castillo','Camino','Granja','Camino','Granja','']
        pieza = Pieza_terreno(11)
        self.assertItemsEqual(pieza11, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 12 se inicializa correctamente
    def test_inicializar_pieza12(self):
        pieza12 = ['Castillo','Castillo','Castillo','Castillo','Camino','Castillo','Castillo','Castillo','']
        pieza = Pieza_terreno(12)
        self.assertItemsEqual(pieza12, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 13 se inicializa correctamente
    def test_inicializar_pieza13(self):
        pieza13 = ['Castillo','Castillo','Camino','Granja','Camino','Granja','Granja','Castillo','']
        pieza = Pieza_terreno(13)
        self.assertItemsEqual(pieza13, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 14 se inicializa correctamente
    def test_inicializar_pieza14(self):
        pieza14 = ['Camino','Castillo','Castillo','Castillo','Granja','Granja','Camino','Granja','']
        pieza = Pieza_terreno(14)
        self.assertItemsEqual(pieza14, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 15 se inicializa correctamente
    def test_inicializar_pieza15(self):
        pieza15 = ['Castillo','Castillo','Granja','Castillo','Castillo','Castillo','Granja','Castillo','']
        pieza = Pieza_terreno(15)
        self.assertItemsEqual(pieza15, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 16 se inicializa correctamente
    def test_inicializar_pieza16(self):
        pieza16 = ['Granja','Castillo','Castillo','Castillo','Castillo','Castillo','Granja','Granja','']
        pieza = Pieza_terreno(16)
        self.assertItemsEqual(pieza16, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 17 se inicializa correctamente
    def test_inicializar_pieza17(self):
        pieza17 = ['Granja','Granja','Granja','Granja','Camino','Granja','Granja','Granja','Monasterio'] ## ESTA FIGURA TIENE UN MONASTERIO EN EL CENTRO
        pieza = Pieza_terreno(17)
        self.assertItemsEqual(pieza17, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 18 se inicializa correctamente
    def test_inicializar_pieza18(self):
        pieza18 = ['Camino','Granja','Camino','Granja','Camino','Granja','Camino','Granja','']
        pieza = Pieza_terreno(18)
        self.assertItemsEqual(pieza18, pieza.posicion)

    # Test para comprobar que la posicion de la pieza de tipo 19 se inicializa correctamente
    def test_inicializar_pieza19(self):
        pieza19 = ['Castillo','Castillo','Castillo','Castillo','Castillo','Castillo','Castillo','Castillo','']
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
    def test_inicializar_baraja_tipo(self):
        baraja = Partida().inicializar_baraja()
        self.assertEqual(1, baraja[0].tipo)

    # Test que comprueba que comprueba si las piezas aparecen ordenadas (comprobacion de la ultima)
    def test_inicializar_baraja_tipo2(self):
        baraja = Partida().inicializar_baraja()
        self.assertEqual(19, baraja[-1].tipo)

    # Test que comprueba la longitud del tablero inicializado sea la correcta
    def test_inicializar_tablero_longitud(self):
        tablero = Partida().inicializar_tablero()
        long_tablero = 1
        self.assertEqual(long_tablero,len(tablero))

    # Test que comprueba si el tipo de la pieza inicial es el correcto
    def test_inicializar_tablero_tipo(self):
        tablero = Partida().inicializar_tablero()
        tipo = 10
        self.assertEqual(tipo,tablero[0].tipo)

    # Test para comprobar que las coordenadas de la pieza inicial son correctas
    def test_inicializar_tablero_coordenadas(self):
        tablero = Partida().inicializar_tablero()
        coordenadas = [0,0]
        self.assertItemsEqual(coordenadas,tablero[0].coordenadas)

    # Test para comprobar que el numero de jugadores es correcto al inicializar la partida
    def test_inicializar_partida_comprobar_num_jugadores(self):
        expected = "Numero de jugadores incorrecto. Solo pueden jugar entre 2 y 4 personas"
        self.assertEqual(expected,Partida().inicializar(['Paco']))

    # Test para comprobar que el numero de jugadores es correcto al inicializar la partida
    def test_inicializar_partida_comprobar_nombre_jugadores(self):
        expected = "No se puede repetir el nombre de dos jugadores"
        self.assertEqual(expected,Partida().inicializar(['Paco','Ana','Paco']))

    # Test para comprobar el numero de jugadores de la partida
    def test_inicializar_partida_comprobar_jugadores_long(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        self.assertEqual(4,len(partida.jugadores))

    # Test para comprobar el numero de piezas en la baraja al inicializar la partida
    def test_inicializar_partida_comprobar_baraja_long(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        self.assertEqual(71,len(partida.baraja))

    # Test para comprobar el numero de piezas en el tablero al inicializar la partida
    def test_inicializar_partida_comprobar_tablero_long(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        self.assertEqual(1,len(partida.tablero))

    # Test para comprobar la instancia de alguno de los jugadores
    def test_inicializar_partida_comprobar_jugadores_instancia(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        self.assertIsInstance(partida.jugadores[2], Jugador)

    # Test para comprobar la instancia de alguna de las piezas
    def test_inicializar_partida_comprobar_baraja_instancia(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        self.assertIsInstance(partida.baraja[16],Pieza_terreno)

    # Test para comprobar la instancia de la pieza del tablero
    def test_inicializar_partida_comprobar_tablero_instancia(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        self.assertIsInstance(partida.tablero[0],Pieza_terreno)

    # Test para comprobar que se inicializa el atributo meeples de una pieza
    def test_inicializar_pieza_add_meeples(self):
        pieza = Pieza_terreno(15)
        self.assertIsNone(pieza.meeples)

    #test para comprobar que se saca de la baraja una pieza correcta.
    def test_long_sacar_pieza(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        pieza = partida.sacar_pieza()
        self.assertEqual(len(pieza.posicion), 9, msg="No tiene la longitud adecuada")

    def test_tipo_sacar_pieza(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        pieza = partida.sacar_pieza()
        self.assertGreaterEqual(pieza.tipo, 0, msg="Tipo erroneo")
        self.assertLessEqual(pieza.tipo, 19, msg="Tipo erroneo")

    # Test para comprobar que tras sacar una pieza la baraja reduce su valor
    def test_long_baraja_sacar_pieza(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        pieza = partida.sacar_pieza()
        self.assertEqual(len(partida.baraja), 70, msg="La baraja no se reduce")

    #Test para actualizar puntuacion
    def test_actualizar_puntuacion(self):
        jugador1 = 'Cristina'
        jugador2 = 'Guillermo'
        jugador3 = 'Adrian'
        jugadores = Partida().inicializar_jugadores([jugador1, jugador2, jugador3])
        puntuacion1 = 90
        puntuacion2 = 120
        puntuacion3 = 110
        jugadores[0].actualizar_puntuacion(puntuacion1)
        jugadores[1].actualizar_puntuacion(puntuacion2)
        jugadores[2].actualizar_puntuacion(puntuacion3)
        self.assertEqual(puntuacion1, jugadores[0].puntuacion)
        self.assertEqual(puntuacion2, jugadores[1].puntuacion)
        self.assertEqual(puntuacion3, jugadores[2].puntuacion)

    #Test para actualizar puntuacion, observando que suma correctamente
    def test_actualizar_puntuacion2(self):
        jugadores = Partida().inicializar_jugadores(['Cristina', 'Guillermo', 'Adrian'])
        puntuacion1 = 90
        puntuacion2 = 120
        puntuacion3 = 110
        jugadores[0].actualizar_puntuacion(puntuacion1)
        jugadores[1].actualizar_puntuacion(puntuacion2)
        jugadores[2].actualizar_puntuacion(puntuacion3)
        jugadores[0].actualizar_puntuacion(50)
        jugadores[1].actualizar_puntuacion(100)
        jugadores[2].actualizar_puntuacion(200)
        self.assertEqual(puntuacion1 + 50, jugadores[0].puntuacion)
        self.assertEqual(puntuacion2 + 100, jugadores[1].puntuacion)
        self.assertEqual(puntuacion3 + 200, jugadores[2].puntuacion)

    #Test para comprobar que se ordenan los jugadores en funcion de su puntuacion
    def test_ordenar_jug_puntos(self):
        jugador1 = 'Paco'
        jugador2 = 'Ana'
        jugador3 = 'Guillermo'
        jugador4 = 'Cristina'
        jugadores = Partida().inicializar_jugadores([jugador1,jugador2,jugador3,jugador4])
        puntuacion1 = 100
        puntuacion2 = 90
        puntuacion3 = 200
        puntuacion4 = 128
        jugadores[0].actualizar_puntuacion(puntuacion1)
        jugadores[1].actualizar_puntuacion(puntuacion2)
        jugadores[2].actualizar_puntuacion(puntuacion3)
        jugadores[3].actualizar_puntuacion(puntuacion4)
        lista_ordenada = Partida().orden_jugadores_ptos(jugadores)
        lista_ordenada_aux = [jugadores[2],jugadores[3],jugadores[0],jugadores[1]]
        self.assertEqual(lista_ordenada_aux[0], lista_ordenada[0])

    def test_ordenar_jug_puntos2(self):
        jugadores = Partida().inicializar_jugadores(['Paco','Ana'])
        puntuacion1 = 100
        puntuacion2 = 190
        jugadores[0].actualizar_puntuacion(puntuacion1)
        jugadores[1].actualizar_puntuacion(puntuacion2)
        lista_ordenada = Partida().orden_jugadores_ptos(jugadores)
        lista_ordenada_aux = [jugadores[1],jugadores[0]]
        self.assertEqual(lista_ordenada_aux[0], lista_ordenada[0])

    #Test para comprobar si se asignan los turnos correctamnete
    def test_asignar_turnos(self):
        jugadores = Partida().inicializar_jugadores(['Pedro', 'Juan', 'Felipe'])
        turnos_jugadores = Partida().asignar_turnos(jugadores)
        i = 0
        while (i < 72):
            self.assertEqual(turnos_jugadores[i].nombre, 'Pedro')
            i = i + 3


  #Test para comprobar si un jugador puede introducir un meeple a una pieza del tablero
    def test_introducir_meeple(self):
        lista_nombres =['Paco','Ana','Laura','Pepe']
        partida = Partida().inicializar(lista_nombres)
        pieza = partida.sacar_pieza()
        turno = 1
        jugador1 = partida.jugadores[turno -1]
        self.assertEqual(True, partida.introducir_meeple(2,jugador1))

  #Test para comprobar si un jugador puede introducir un meeple a una pieza del tablero
    def test_introducir_meeple2(self):
        lista_nombres =['Paco','Ana','Laura','Pepe']
        partida = Partida().inicializar(lista_nombres)
        turno = 1
        pieza = partida.sacar_pieza()
        jugador1 = partida.jugadores[turno -1]
        n_meeples = jugador1.meeples
        partida.introducir_meeple(2,jugador1)
        self.assertEqual(n_meeples - 1,jugador1.meeples)


    #Test para comprobar si un jugador al introducir un meeple en una pieza del
    #tablero se queda con un meeple menos de los que tenia
    def test_introducir_meeple3(self):
        lista_nombres =['Paco','Ana','Laura','Pepe']
        partida = Partida().inicializar(lista_nombres)
        turno = 1
        pieza = partida.sacar_pieza()
        jugador1 = partida.jugadores[turno -1]
        jugador1.meeples = 0
        self.assertEqual(False, partida.introducir_meeple(2,jugador1))

    #Test para comprobar que el numero de monasterios sea correcto
    def test_comprobar_monasterio(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        monasterios = partida.comprobar_cierre_monasterio()
        self.assertGreaterEqual(monasterios, 0, msg="Numero inconrrecto de monasterios")

    # Test que comprueba que la funcion posicion_tipo_terreno_en_pieza devuelve un numero
    # correcto
    def test_comprobar_long_num_caminos_en_pieza(self):
        pieza = Pieza_terreno(7)
        self.assertEqual(3, len(pieza.posicion_tipo_terreno_en_pieza("Camino")))

    # Test que comprueba que la funcion posicion_tipo_terreno_en_pieza devuelve las posiciones
    # correctas
    def test_comprobar_posiciones_num_caminos_en_pieza(self):
        pieza = Pieza_terreno(12)
        posiciones = [0, 2, 6]
        self.assertItemsEqual(posiciones, pieza.posicion_tipo_terreno_en_pieza("Castillo"))

    # Test que comprueba que la funcion buscar_ind_jugador funciona correctamente
    def test_comprobar_indice_jugador(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        jugador = Jugador('Ana')
        indice_jugador = partida.buscar_ind_jugador(jugador.nombre)
        self.assertEqual(1, indice_jugador) 

    # Test que comprueba si la funcion jugadores_con_mas_meeples funciona bien
    def test_jugador_con_mas_meeples(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        pieza1 = Pieza_terreno(11)
        pieza1.jugador = partida.jugadores[0]
        pieza2 = Pieza_terreno(11)
        pieza2.jugador = partida.jugadores[1]
        pieza3 = Pieza_terreno(11)
        pieza3.jugador = partida.jugadores[2]
        pieza2.meeples = 0
        jugadores = partida.jugadores_con_mas_meeples([pieza1,pieza2,pieza3],"Camino")
        self.assertEqual('Ana',jugadores[0].nombre)

    # Test que comprueba si la funcion jugador_con_mas_meeples funciona bien
    def test_jugador_con_mas_meeples2(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        pieza1 = Pieza_terreno(11)
        pieza1.jugador = partida.jugadores[2]
        pieza2 = Pieza_terreno(11)
        pieza2.jugador = partida.jugadores[1]
        pieza3 = Pieza_terreno(11)
        pieza3.jugador = partida.jugadores[2]
        pieza1.meeples = 0
        pieza2.meeples = 0
        pieza3.meeples = 0
        jugadores = partida.jugadores_con_mas_meeples([pieza1,pieza2,pieza3],"Camino")
        self.assertEqual('Maria',jugadores[0].nombre)

    # Test que comprueba si la funcion jugador_con_mas_meeples funciona bien
    def test_jugador_con_mas_meeples3(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        pieza1 = Pieza_terreno(11)
        pieza1.jugador = partida.jugadores[2]
        pieza2 = Pieza_terreno(11)
        pieza2.jugador = partida.jugadores[1]
        pieza1.meeples = 0
        pieza2.meeples = 0
        jugadores = partida.jugadores_con_mas_meeples([pieza1,pieza2],"Camino")
        self.assertEqual('Ana',jugadores[0].nombre)
        self.assertEqual('Maria',jugadores[1].nombre)

    # Comprueba la puntuacion para una secuencia concreta de camino
    def test_comprobar_cierre_camino(self):
        partida = Partida().inicializar(['Paco','Ana','Maria','Pepe'])
        pieza1 = Pieza_terreno(11)
        pieza2 = Pieza_terreno(11)
        partida.poner_pieza(pieza1, [0,1])
        partida.poner_pieza(pieza2, [0,-1])
        partida.introducir_meeple(4,partida.jugadores[1])
        partida.comprobar_cierre_camino()
        self.assertEqual(3, partida.jugadores[1].puntuacion)


if __name__ == '__main__':
    unittest.main()

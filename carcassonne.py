import random
import collections

class Partida:

    # Comprueba que el numero de jugadores sea correcto
    def num_jug_correcto(self, nombres_jugadores):
        num_maximo_jugadores = 4
        num_minimo_jugadores = 2
        num_jugadores = len(nombres_jugadores)
        if num_jugadores > num_maximo_jugadores or num_jugadores < num_minimo_jugadores:
            return False
        else:
            return True

    # Comprueba que el nombre de los jugadores sea correcto
    def nombres_jug_correcto(self, nombres_jugadores):
        # Cuento la frecuencia de repeticion de los nombres
        freq = collections.Counter(nombres_jugadores).values()
        if max(freq) > 1:
            return False
        else:
            return True

    # Inicializa la lista de jugadores
    def inicializar_jugadores(self, nombres_jugadores):
        lista_jugadores = []
        for nombre in nombres_jugadores:
            lista_jugadores.append(Jugador(nombre))
        return lista_jugadores

    # Inicializa la baraja
    def inicializar_baraja(self):
        numero_tipos_pieza = 19
        baraja = []
        for i in range(numero_tipos_pieza):
            baraja += Pieza_terreno(i+1).repetir_pieza()
        return baraja

    # Inicializa el tablero
    def inicializar_tablero(self):
        tipo_pieza_inicial = 10
        pieza_inicial = Pieza_terreno(tipo_pieza_inicial)
        pieza_inicial.coordenadas = [0, 0]
        tablero = [pieza_inicial]
        return tablero

    #Asignar turnos a los jugadores
    def asignar_turnos(self, jugadores):
        turno = 1
        i = 1
        turnos_jugador = []
        numero_turnos = 72
        numero_jugadores = len(jugadores)
        while (turno < numero_turnos):
            turnos_jugador.append(jugadores[i-1])
            if i == numero_jugadores:
                i = 0
            turno = turno + 1
            i = i + 1
        return turnos_jugador

    # Inicializacion de la partida
    def inicializar(self, nombres_jugadores):
        if not self.num_jug_correcto(nombres_jugadores):
            return "Numero de jugadores incorrecto. Solo pueden jugar entre 2 y 4 personas"
        if not self.nombres_jug_correcto(nombres_jugadores):
            return "No se puede repetir el nombre de dos jugadores"
        self.turno = 0
        self.jugadores = self.inicializar_jugadores(nombres_jugadores)
        self.baraja = self.inicializar_baraja()  # baraja = fichas que aun se pueden jugar
        random.shuffle(self.baraja)  # aleatorizo la baraja
        self.tablero = self.inicializar_tablero()  # tablero = fichas que ya se han jugado
        self.caminos_encontrados = []  # lista con los caminos que se completaron
        self.monasterios_encontrados = []  # lista con los caminos ya completados
        self.lista_turnos = self.asignar_turnos(self.jugadores)  # orden de los turnos de los jugadores
        return self

    # Busca el indice en el que se encuentra el jugador que se pasa en self.jugadores
    def buscar_ind_jugador(self, jugador_buscado):
        indice = None
        for i in range(len(self.jugadores)):
            if self.jugadores[i].nombre == jugador_buscado:
                indice = i
        return indice

    # Suma uno al turno de la partida y devuelve el jugador que juega ese turno
    def jugador_turno(self):
        self.turno += 1
        jugador_buscado = self.lista_turnos[self.turno-1]
        jugador = self.jugadores[self.buscar_ind_jugador(jugador_buscado.nombre)]
        return jugador

    # Saca una pieza de la baraja
    def sacar_pieza(self):
        pieza_sacada= []
        pieza_sacada = self.baraja[self.turno-1]
        self.baraja.pop(self.turno-1)
        return pieza_sacada

   #Funcion para obtener cual es la pieza que ya esta en el tablero
    def ver_pieza_tablero (self, coords):
        tablero = self.tablero
        for j in range(len(tablero)):
            if coords == tablero[j].coordenadas:
                pieza_tablero = tablero[j]
                break
            else:
                pieza_tablero = []
        return pieza_tablero

    def se_puede_poner_norte (self, pieza_norte, pieza_colocar):
        if (pieza_norte == []):
            return True
        elif (pieza_norte.posicion[4] == pieza_colocar.posicion[0]):
            return True
        else:
            return False

    def se_puede_poner_este (self, pieza_este, pieza_colocar):
        if (pieza_este == []):
            return True
        elif (pieza_este.posicion[6] == pieza_colocar.posicion[2]):
            return True
        else:
            return False

    def se_puede_poner_sur(self, pieza_sur, pieza_colocar):
        if (pieza_sur == []):
            return True
        elif (pieza_sur.posicion[0] == pieza_colocar.posicion[4]):
            return True
        else:
            return False
    def se_puede_poner_oeste(self, pieza_oeste, pieza_colocar):
        if (pieza_oeste == []):
            return True
        elif (pieza_oeste.posicion[2] == pieza_colocar.posicion[6]):
            return True
        else:
            return False

    # Funcion para comprobar si se puede colocar una pieza en la posicion requerida o no.
    def poner_pieza (self, pieza_colocar, coordenadas_colocar):
        coord_x = coordenadas_colocar[0]
        coord_y = coordenadas_colocar[1]
        pieza_norte = self.ver_pieza_tablero([coord_x, coord_y+1])
        pieza_oeste = self.ver_pieza_tablero([coord_x-1, coord_y])
        pieza_sur = self.ver_pieza_tablero([coord_x, coord_y-1])
        pieza_este = self.ver_pieza_tablero([coord_x+1, coord_y])
        comprobar_pieza = self.ver_pieza_tablero([coord_x,coord_y])
        if comprobar_pieza != []:
            return False
        elif (self.se_puede_poner_norte(pieza_norte, pieza_colocar) and self.se_puede_poner_este(pieza_este, pieza_colocar) and self.se_puede_poner_sur(pieza_sur, pieza_colocar) and self.se_puede_poner_oeste(pieza_oeste, pieza_colocar)) and (pieza_norte != [] or pieza_este !=[] or pieza_sur !=[] or pieza_oeste !=[]):
            pieza_colocar.jugador = self.jugadores[self.turno % len(self.jugadores)-1]
            pieza_colocar.coordenadas = coordenadas_colocar
            self.tablero.append(pieza_colocar)
        else:
            return False

    #Introducir meeple en la ultima ficha del tablero
    def introducir_meeple(self,posicion_meeple):
        jugador = self.jugadores[self.turno % len(self.jugadores)-1]
        if jugador.meeples > 0:
            self.tablero[-1].meeples = posicion_meeple
            jugador.meeples -= 1
            self.jugadores[self.turno % len(self.jugadores)-1] = jugador
            return True
        else:
            return False

    # Busca las piezas que tienen un tipo determinado en alguno de sus lados
    def buscar_tipo_en_tablero(self, tipo):
        tablero = self.tablero
        piezas_tipo = []
        for k in range(len(tablero)):
            if tipo in tablero[k].posicion:
                piezas_tipo.append(tablero[k])
        return piezas_tipo


    def comprobar_cierre_monasterio(self):
        monasterios = self.buscar_tipo_en_tablero("Monasterio")
        self.sumar_puntos_monasterio(monasterios)

    # Suma los puntos en el caso de que se haya completado un monasterio que se pasa como argumento
    def sumar_puntos_monasterio(self, piezas_monasterio):
        puntos = 0
        for mon in range(len(piezas_monasterio)):
            if not (piezas_monasterio[mon] in self.monasterios_encontrados):
                nombre_jugador = piezas_monasterio[mon].jugador.nombre
                ind_jugador = self.buscar_ind_jugador(nombre_jugador)
                jugador_monasterio = self.jugadores[ind_jugador]
                coorx = piezas_monasterio[mon].coordenadas[0]
                coory = piezas_monasterio[mon].coordenadas[1]
                if(self.ver_pieza_tablero([coorx,coory-1]) != [] and self.ver_pieza_tablero([coorx,coory+1]) != [] and self.ver_pieza_tablero([coorx-1,coory]) != [] and self.ver_pieza_tablero([coorx+1,coory]) != []):
                    # Suma 9 puntos por tener un monasterio completo
                    puntos = 9
                    jugador_monasterio.actualizar_puntuacion(puntos)
                    self.jugadores[ind_jugador] = jugador_monasterio
                    self.monasterios_encontrados.append(piezas_monasterio[mon])

    # Devuelve el/los jugador/es que mas meeples tienen en una lista de piezas que se le pasa
    def jugadores_con_mas_meeples(self, piezas, tipo_terreno):
        jugadores = []
        nombres_jugadores = [] # array con los nombres de los jugadores con meeple (se pueden repetir)
        for pieza in piezas:
            posiciones = pieza.posicion_tipo_terreno_en_pieza(tipo_terreno)
            if pieza.meeples in posiciones:
                nombres_jugadores.append(pieza.jugador.nombre)
        if len(nombres_jugadores) > 1:
            # Si hay mas de un jugador con meeples me quedo con el que mas tenga
            freq = collections.Counter(nombres_jugadores).values()
            max_freq = max(freq)
            total = freq.count(max_freq)
            mas_comun = collections.Counter(nombres_jugadores).most_common(total)
            nombres_jugadores = [elem[0] for elem in mas_comun] # ahora ya no estan repetidos
        # Introduzco el objeto de cada jugador en jugadores
        for nombre in nombres_jugadores:
            ind_jugador = self.buscar_ind_jugador(nombre)
            jugadores.append(self.jugadores[ind_jugador])
        return jugadores

    # Funcion que busca la pieza conectada a la que se pasa como argumento de un tipo de terreno concreto
    def evaluar_siguiente(self,pieza_actual,posicion_actual,tipo_terreno):
        pieza_siguiente = []
        num_pos_siguiente = None
        posicion_siguiente = None
        coord_x = pieza_actual.coordenadas[0]
        coord_y = pieza_actual.coordenadas[1]
        if posicion_actual == 0:
            coord_y += 1
            tmp = 4 # posicion de la siguiente a la que se conecta la actual
        elif posicion_actual == 2:
            coord_x += 1
            tmp = 6 # si es Este se conecta a la siguiente por Oeste
        elif posicion_actual == 4:
            coord_y -= 1
            tmp = 0
        elif posicion_actual == 6:
            coord_x -= 1
            tmp = 2
        else:
            return pieza_siguiente, num_pos_siguiente, posicion_siguiente
        pieza_siguiente = self.ver_pieza_tablero([coord_x,coord_y])
        if pieza_siguiente != []:
            posiciones_siguiente = pieza_siguiente.posicion_tipo_terreno_en_pieza("Camino")
            num_pos_siguiente = len(posiciones_siguiente)
            # Me quedo con la posicion del otro lado en el caso de que dos lados sean Camino
            if num_pos_siguiente == 2:
                for posicion in posiciones_siguiente:
                    if posicion != tmp:
                        posicion_siguiente = posicion
        return pieza_siguiente, num_pos_siguiente, posicion_siguiente


    # Funcion que busca si una pieza del camino forma parte de un camino cerrado
    def buscar_caminos_cerrados(self, pieza):
        posiciones = pieza.posicion_tipo_terreno_en_pieza("Camino")
        max_caminos_posibles = [1, 1, 3, 4]
        caminos = []
        for ind_camino in range(max_caminos_posibles[len(posiciones)-1]):
            piezas_camino = []  # piezas que forman el camino
            terminaciones = []  # piezas que terminan el camino
            pieza_actual = pieza
            num_pos_actual = len(posiciones)
            posicion_actual = posiciones[ind_camino]
            while pieza_actual != []:
                piezas_camino.append(pieza_actual)
                if num_pos_actual != 2:
                    terminaciones.append(pieza_actual)
                if len(terminaciones) < 2:
                    pieza_actual,num_pos_actual,posicion_actual = self.evaluar_siguiente(pieza_actual,posicion_actual,"Camino")
                else:
                    break;
            if len(terminaciones)==2:
                piezas_camino.sort(key=lambda x: (x.coordenadas[0],x.coordenadas[1]))
                caminos.append(piezas_camino)
        return caminos

    # Comprueba si algun camino se ha cerrado
    def comprobar_cierre_camino(self):
        caminos = self.buscar_tipo_en_tablero("Camino")
        for pieza_camino in caminos:
            # Para cada pieza de camino compruebo si participa en algun camino ya cerrado
            piezas_caminos = self.buscar_caminos_cerrados(pieza_camino) # devuelve lista de caminos cerrados
            for piezas_camino in piezas_caminos:
                # Para cada camino cerrado, si no estaba ya contado lo introduzco y sumo la puntuacion
                if (piezas_camino != []) and not (piezas_camino in self.caminos_encontrados):
                    self.caminos_encontrados.append(piezas_camino)
                    jugadores = self.jugadores_con_mas_meeples(piezas_camino,"Camino")
                    for jugador in jugadores:
                        # A cada jugador le sumo la puntuacion y le devuelvo los meeples
                        ind_jugador = self.buscar_ind_jugador(jugador.nombre)
                        self.jugadores[ind_jugador].actualizar_puntuacion(len(piezas_camino))
                        self.jugadores[ind_jugador].meeples += 1

    #Metodos para buscar castillos cerrados(recursivo)
    def es_castillo(self,pieza):
        #posibles_castillos = self.buscar_tipo_en_tablero("Castillo")
        pieza_siguiente = None
        encontrado = False
        castillo = False
        posiciones = pieza.posicion_tipo_terreno_en_pieza2("Castillo")
        coord_x = pieza.coordenadas[0]
        coord_y = pieza.coordenadas[1]
        piezas_totales = []
        piezas_castillos = []
        if posiciones == []:
            return False
        else:
            piezas_totales.append(pieza)
            for i in posiciones:
                pieza_inicio = pieza
                if i == 1:
                    #inicio == 1
                    coord_x2 = coord_x +1
                    pieza_siguiente = self.ver_pieza_tablero([coord_x2,coord_y])
                    coord_y2 = coord_y +1
                    pieza_siguiente2 = self.ver_pieza_tablero([coord_x,coord_y2])
                    if pieza_siguiente != []:
                        piezas_totales,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente,piezas_totales)

                    if pieza_siguiente2 != []:
                        piezas_totales,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente2,piezas_totales)
                    else:
                        if pieza.tipo != 9:
                            if pieza.tipo !=15:
                                castillo = False
                                break


                if i == 3:
                    coord_x2 = coord_x +1
                    pieza_siguiente = self.ver_pieza_tablero([coord_x2,coord_y])
                    coord_y2 = coord_y -1
                    pieza_siguiente = self.ver_pieza_tablero([coord_x,coord_y2])
                    if pieza_siguiente != []:
                        piezas_totales,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente,piezas_totales)

                    elif pieza_siguiente != []:
                        piezas_totales,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente2,piezas_totales)
                    else:

                        if pieza.tipo != 9:
                            if pieza.tipo !=15:
                                castillo = False
                                break
                if i == 5:
                    coord_x2 = coord_x - 1
                    pieza_siguiente = self.ver_pieza_tablero([coord_x2,coord_y])
                    coord_y2 = coord_y -1
                    pieza_siguiente2 = self.ver_pieza_tablero([coord_x,coord_y2])
                    if pieza_siguiente != []:
                        piezas_totales,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente,piezas_totales)

                    elif pieza_siguiente2 != []:
                        piezas_totales,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente2,piezas_totales)
                    else:
                        a=1


                        if pieza.tipo != 9:
                            if pieza.tipo !=15:
                                castillo = False
                                break
                if i == 7:
                    #inicio == 7
                    coord_x2 = coord_x - 1
                    pieza_siguiente = self.ver_pieza_tablero([coord_x2,coord_y])
                    coord_y2 = coord_y +1
                    pieza_siguiente = self.ver_pieza_tablero([coord_x,coord_y2])
                    if pieza_siguiente != []:
                        piezas_totales,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente,piezas_totales)

                    elif pieza_siguiente2 != []:
                        piezas_totales,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente2,piezas_totales)
                    else:
                        a=1

                        if pieza.tipo != 9:
                            if pieza.tipo !=15:
                                castillo = False
                                break

                if castillo == True: #Castillo cerrado
                    numero_piezas = len(piezas_totales)
                    self.piezas_castillos = piezas_totales
                    break
            return castillo,(piezas_totales)



    def buscar_castillos(self,pieza_inicio,pieza,piezas):
        posiciones = pieza.posicion_tipo_terreno_en_pieza2("Castillo")
        castillo = False
        if posiciones == []:
            return False
        else:
            for m,k in enumerate(piezas):
                if (k!= pieza) & (len(piezas)-1 == m) :
                    piezas.append(pieza)
            for j,i in enumerate(posiciones):
                piezas, castillo, pieza_inicio =self.casos(pieza,piezas,i,pieza_inicio,j)
            return piezas,castillo,pieza_inicio


    def casos(self,pieza,piezas,i,pieza_inicio,j):
        posiciones = pieza.posicion_tipo_terreno_en_pieza2("Castillo")
        analizar = True
        castillo = False
        coord_x = pieza.coordenadas[0]
        coord_y = pieza.coordenadas[1]
        if i == 1:
            #inicio == 1
            coord_x2 = coord_x +1
            pieza_siguiente = self.ver_pieza_tablero([coord_x2,coord_y])
            coord_y2 = coord_y +1
            pieza_siguiente2 = self.ver_pieza_tablero([coord_x,coord_y2])
            if pieza_siguiente != []:
                for k in piezas:
                    if k== pieza_siguiente:
                        analizar = False
                        if (k == pieza_inicio) & (len(posiciones)-1 ==j):
                            castillo= True
                if analizar == True:
                    piezas.append(pieza)
                    piezas,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente,piezas)

            if pieza_siguiente2 != []:
                for k in piezas:
                    if k== pieza_siguiente2:
                        analizar = False
                        if (k == pieza_inicio) & (len(posiciones)-1 ==j):
                            castillo= True
                if analizar == True:
                    piezas,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente2,piezas)
            else:
                castillo = False

        if i == 3:

            coord_x2 = coord_x +1
            pieza_siguiente = self.ver_pieza_tablero([coord_x2,coord_y])
            coord_y2 = coord_y -1
            pieza_siguiente2 = self.ver_pieza_tablero([coord_x,coord_y2])
            if pieza_siguiente != []:
                for k in piezas:
                    if k== pieza_siguiente:
                        analizar = False
                        if (k == pieza_inicio) & (len(posiciones)-1 ==j):
                            castillo= True
                if analizar == True:
                    piezas,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente,piezas)

            elif pieza_siguiente2 != []:
                for k in piezas:
                    if k== pieza_siguiente2:
                        analizar = False
                        if (k == pieza_inicio) & (len(posiciones)-1 ==j):
                            castillo= True
                if analizar == True:
                    piezas,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente2,piezas)
            else:
                castillo = False
        if i == 5:
            coord_x2 = coord_x - 1
            pieza_siguiente = self.ver_pieza_tablero([coord_x2,coord_y])
            coord_y2 = coord_y -1
            pieza_siguiente2 = self.ver_pieza_tablero([coord_x,coord_y2])
            if pieza_siguiente != []:
                for k in piezas:
                    if k== pieza_siguiente:
                        analizar = False
                        if (k == pieza_inicio) & (len(posiciones)-1 ==j):
                            castillo= True
                if analizar == True:
                    piezas,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente,piezas)

            if pieza_siguiente2 != []:
                for k in piezas:
                    if k== pieza_siguiente2:
                        analizar = False
                        if (k == pieza_inicio) & (len(posiciones)-1 ==j):
                            castillo= True
                if analizar == True:
                    piezas,castillo,pieza_inicio = self.buscar_castillos(pieza_inicio,pieza_siguiente2,piezas)
            else:
                castillo = False
        if (j == 7):
            #inicio == 7
            coord_x2 = coord_x - 1
            pieza_siguiente = self.ver_pieza_tablero([coord_x2,coord_y])
            coord_y2 = coord_y +1
            pieza_siguiente2 = self.ver_pieza_tablero([coord_x,coord_y2])
            if pieza_siguiente != []:
                for k in piezas:
                    if k== pieza_siguiente:
                        analizar = False
                        if (k == pieza_inicio) & (len(posiciones)-1 ==j):
                            castillo= True
                if analizar == True:
                    piezas,castillo,pieza_inicio = self.buscar_castillos(pieza_siguiente,piezas)

            elif pieza_siguiente2 != []:
                for k in piezas:
                    if k== pieza_siguiente2:
                        analizar = True
                        if (k == pieza_inicio) & (len(posiciones)-1 ==j):
                            castillo= True
                if analizar == False:
                    piezas,castillo,pieza_inicio = self.buscar_castillos(pieza_siguiente2,piezas)
            else:
                castillo = False
        return piezas, castillo, pieza_inicio


    #Contabilizar puntos por castillos cerrados
    def puntuacion_castillos(self,piezas,castillo):
        jugadores = []
        jugadores1 = []
        if castillo == True:
            for pieza in piezas:
                if pieza.meeples != None:
                    jugadores.append(pieza.jugador)
            if len(jugadores) == 1:
                if len(piezas)>2:
                    puntos = 2*len(piezas)
                else:
                    puntos = 2
                jugadores[0].actualizar_puntuacion(puntos)
                jugadores[0].meeples += 1
            else:
                j_mas_meeples = jugadores_con_mas_meeples(piezas, 'Castillo')
                if len(j_mas_meeples)>1:
                    for jugadores in j_mas_meeples:
                        jugadores.actualizar_puntuacion(10)
                        jugadores.meeples += 1
                else:
                    if len(piezas)>2:
                        puntos = 2*len(piezas)
                    else:
                        puntos = 2
                        jugadores[0].actualizar_puntuacion(puntos)
                        jugadores.meeples += 1


    # Comprueba los cierres de los distintos tipos de terreno al final de cada turno
    def comprobar_cierres(self):
        self.comprobar_cierre_monasterio()
        self.comprobar_cierre_camino()

    # Comprueba el/los jugador/es con mas meeples en granjas y le suma diez puntos
    def comprobar_cierre_granjas(self):
        jugadores = self.jugadores_con_mas_meeples(self.tablero, "Granja")
        for jugador in jugadores:
            ind_jugador = self.buscar_ind_jugador(jugador.nombre)
            self.jugadores[ind_jugador].actualizar_puntuacion(10)

    # Ordenar los jugadores en funcion de la puntuacion de cada uno de ellos
    def orden_jugadores_ptos(self,lista_jugadores):
        lista_jugadores_aux = sorted(lista_jugadores, key = lambda objeto: objeto.puntuacion, reverse = True)
        return lista_jugadores_aux

class Jugador:

    # Inicializa la clase jugador
    def __init__(self, nombre):
        self.nombre = nombre
        self.meeples = 8  # meeples disponibles
        self.puntuacion = 0


    #Actualizar puntuacion
    def actualizar_puntuacion(self, puntos):
        self.puntuacion += puntos
        return self


class Pieza_terreno:

    # Devuelve los indices de posicion en los que coincide el tipo de terreno
    # que se pasa como argumento
    def posicion_tipo_terreno_en_pieza(self,tipo_terreno):
        indices_posicion = []
        # Elimino las esquinas en el caso del camino
        if tipo_terreno == "Granja":
            posicion = self.posicion[0:7]
            for i in range(len(posicion)):
                if posicion[i] == tipo_terreno:
                    indices_posicion.append(i)
        else:
            posicion = self.posicion[0:7:2]
            for i in range(len(posicion)):
                if posicion[i] == tipo_terreno:
                    indices_posicion.append(i*2)
        # Me quedo con aquellos indices en los que coincida el tipo de terreno
        return indices_posicion

    # Devuelve todos los indices de posicion en los que coincide el tipo de terreno
    # que se pasa como argumento
    def posicion_tipo_terreno_en_pieza2(self,tipo_terreno):
        # Elimino las esquinas
        posicion = self.posicion
        # Me quedo con aquellos indices en los que coincida el tipo de terreno
        indices_posicion = []
        for i in range(len(posicion)):
            if posicion[i] == tipo_terreno:
                indices_posicion.append(i)
        return indices_posicion


    # Repite cada pieza el numero de veces que aparezca en el juego original
    def repetir_pieza(self):
        if self.tipo == 1:
            pieza_repetida = 9*[self]
        elif self.tipo == 2:
            pieza_repetida = 8*[self]
        elif self.tipo == 3:
            pieza_repetida = 5*[self]
        elif self.tipo == 4:
            pieza_repetida = 5*[self]
        elif self.tipo == 5:
            pieza_repetida = 5*[self]
        elif self.tipo == 6:
            pieza_repetida = 4*[self]
        elif self.tipo == 7:
            pieza_repetida = 4*[self]
        elif self.tipo == 8:
            pieza_repetida = 4*[self]
        elif self.tipo == 9:
            pieza_repetida = 3*[self]
        elif self.tipo == 10:
            pieza_repetida = 3*[self]
        elif self.tipo == 11:
            pieza_repetida = 3*[self]
        elif self.tipo == 12:
            pieza_repetida = 3*[self]
        elif self.tipo == 13:
            pieza_repetida = 3*[self]
        elif self.tipo == 14:
            pieza_repetida = 3*[self]
        elif self.tipo == 15:
            pieza_repetida = 3*[self]
        elif self.tipo == 16:
            pieza_repetida = 2*[self]
        elif self.tipo == 17:
            pieza_repetida = 2*[self]
        elif self.tipo == 18:
            pieza_repetida = 1*[self]
        elif self.tipo == 19:
            pieza_repetida = 1*[self]
        return pieza_repetida

    # Asigna los distintos tipos de territorios al atributo posicion. El array se
    # corresponderia con la parte ['Norte','Noreste','Este','Sureste','Sur','Suroeste','Oeste','Noroeste','Centro'] de la pieza
    def asignar_posicion(self, tipo):
        if tipo == 1:
            posicion = ['Granja','Granja','Granja','Granja','Camino','Granja','Camino','Granja','']
        elif tipo == 2:
            posicion = ['Camino','Granja','Granja','Granja','Camino','Granja','Granja','Granja','']
        elif tipo == 3:
            posicion = ['Castillo','Castillo','Camino','Granja','Camino','Castillo','Castillo','Castillo','']
        elif tipo == 4:
            posicion = ['Castillo','Castillo','Granja','Granja','Granja','Castillo','Castillo','Castillo','']
        elif tipo == 5:
            posicion = ['Granja','Castillo','Castillo','Castillo','Granja','Granja','Granja','Granja','']
        elif tipo == 6:
            posicion = ['Castillo','Castillo','Castillo','Castillo','Granja','Castillo','Castillo','Castillo','']
        elif tipo == 7:
            posicion = ['Granja','Granja','Camino','Granja','Camino','Granja','Camino','Granja','']
        elif tipo == 8:
            posicion = ['Granja','Granja','Granja','Granja','Granja','Granja','Granja','Granja','Monasterio']
        elif tipo == 9:
            posicion = ['Granja','Castillo','Castillo','Castillo','Granja','Castillo','Castillo','Castillo','']
        elif tipo == 10:
            posicion = ['Camino','Castillo','Castillo','Castillo','Camino','Granja','Granja','Granja','']
        elif tipo == 11:
            posicion = ['Camino','Castillo','Castillo','Castillo','Camino','Granja','Camino','Granja','']
        elif tipo == 12:
            posicion = ['Castillo','Castillo','Castillo','Castillo','Camino','Castillo','Castillo','Castillo','']
        elif tipo == 13:
            posicion = ['Castillo','Castillo','Camino','Granja','Camino','Granja','Granja','Castillo','']
        elif tipo == 14:
            posicion = ['Camino','Castillo','Castillo','Castillo','Granja','Granja','Camino','Granja','']
        elif tipo == 15:
            posicion = ['Castillo','Castillo','Granja','Castillo','Castillo','Castillo','Granja','Castillo','']
        elif tipo == 16:
            posicion = ['Granja','Castillo','Castillo','Castillo','Castillo','Castillo','Granja','Granja','']
        elif tipo == 17:
            posicion = ['Granja','Granja','Granja','Granja','Camino','Granja','Granja','Granja','Monasterio']
        elif tipo == 18:
            posicion = ['Camino','Granja','Camino','Granja','Camino','Granja','Camino','Granja','']
        elif tipo == 19:
            posicion = ['Castillo','Castillo','Castillo','Castillo','Castillo','Castillo','Castillo','Castillo','']
        return posicion

    # Inicializa la clase pieza territorio
    def __init__(self, tipo):
        self.tipo = tipo
        # Posicion = ['Norte','Noreste','Este','Sureste','Sur','Suroeste','Oeste','Noroeste','Centro']
        self.posicion = self.asignar_posicion(tipo)
        # Coordenada X y coordenada Y
        self.coordenadas = [None,None]
        # Si no hay ningun meeple colocado, self.meeples = None. Si lo hay,
        # self.meeples toma el valor de la parte en la que se coloca:
        # 0: norte, 1: noreste, 2: este, 3:sureste, 4: sur, 5: suroeste, 6: oeste, 7: noroeste, 8: Centro
        self.meeples = None
        # Jugador que ha colocado la pieza
        self.jugador = None

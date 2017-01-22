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

    # Inicializacion de la partida
    def inicializar(self, nombres_jugadores):
        if not self.num_jug_correcto(nombres_jugadores):
            return "Numero de jugadores incorrecto. Solo pueden jugar entre 2 y 4 personas"
        if not self.nombres_jug_correcto(nombres_jugadores):
            return "No se puede repetir el nombre de dos jugadores"
        turno = 1
        self.jugadores = self.inicializar_jugadores(nombres_jugadores)
        self.baraja = self.inicializar_baraja()  # baraja = fichas que aun se pueden jugar
        random.shuffle(self.baraja)  # aleatorizo la baraja
        self.tablero = self.inicializar_tablero()  # tablero = fichas que ya se han jugado

        return self

    # Ordenar los jugadores en funcion de la puntuacion de cada uno de ellos
    def orden_jugadores_ptos(self,lista_jugadores):
        lista_jugadores_aux = sorted(lista_jugadores, key = lambda objeto: objeto.puntuacion, reverse = True)
        return lista_jugadores_aux

    # Saca una pieza de la baraja
    def sacar_pieza(self):
        pieza_sacada= []
        turno = len(self.tablero)
        pieza_sacada = self.baraja[turno-1]
        self.baraja.pop(turno-1)
        return pieza_sacada

   #Funcion para obtener cual es la pieza que ya esta en el tablero
    def ver_pieza_tablero (self, coords):
        tablero = self.tablero
        for j in len(tablero):
            if coords == tablero[j].coordenadas:
                pieza_tablero = tablero[j].posicion
            else:
                pieza_tablero = []
        return pieza_tablero
    
    # Funcion para comprobar si se puede colocar una pieza en la posicion requerida o no.        
    def poner_pieza (self, pieza_colocar, coordenadas_colocar):
        coord_x = coordenadas_colocar[0]
        coord_y = coordenadas_colocar[1]
        pieza_norte = self.ver_pieza_tablero([coord_x, coord_y-1])
        pieza_oeste = self.ver_pieza_tablero([coord_x+1, coord_y])
        pieza_sur = self.ver_pieza_tablero([coord_x, coord_y +1])
        pieza_este = self.ver_pieza_tablero([coord_x-1, coord_y])
        comprobar_pieza = self.ver_pieza_tablero([coord_x,coord_y])
        if comprobar_pieza != []:
            return False
        elif (pieza_norte.posicion[2] == pieza_colocar.posicion[0] and pieza_oeste.posicion[3] == pieza_colocar.posicion[1] and pieza_sur.posicion[0] == pieza_colocar.posicion[2] and pieza_este.posicion[1] == pieza_colocar.posicion[3]) and (pieza_norte ==[] or pieza_oeste == [] or pieza_sur==[] or pieza_este==[]):
            pieza_colocar.jugador = self.jugadores[self.turno % len(self.jugadores)-1]
            pieza_colocar.coordenadas = coordenadas_colocar
            self.tablero.append(pieza_colocar)
        else:
            return False
    
    #Introducir meeple en una ficha del tablero
    def introducir_meeple(self,pieza,posicion_meeple,jugador):
        if jugador.meeples > 0:
            pieza.meeple = posicion_meeple
            jugador.meeples -= 1
            return True
        else:
            return False
        
    def comprobar_cierre_monasterio(self):
        num_monast = self.buscar_monaterios_en_tablero()
        numero_monasterios = len(num_monast)
        return numero_monasterios


    def buscar_monaterios_en_tablero(self):
        tablero = self.tablero
        monasterios = []
        for k in range(len(tablero)):
            if tablero[k].posicion[8] == 'Monasterio':
                pieza_monasterio = tablero[k]
                monasterios.append(pieza_monasterio)
            else:
                pass
        return monasterios

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
    # corresponderia con la parte ['Norte','Este','Sur','Oeste'] de la pieza
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
            posicion = ['Granja','Granja','Granja','Granja','Granja','Granja','Granja','Granja','Monasterio']  ## ESTA FIGURA TIENE UN MONASTERIO EN EL CENTRO
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
            posicion = ['Granja','Granja','Granja','Granja','Camino','Granja','Granja','Granja','Monasterio']  ## ESTA FIGURA TIENE UN MONASTERIO EN EL CENTRO
        elif tipo == 18:
            posicion = ['Camino','Granja','Camino','Granja','Camino','Granja','Camino','Granja','']
        elif tipo == 19:
            posicion = ['Castillo','Castillo','Castillo','Castillo','Castillo','Castillo','Castillo','Castillo','']
        return posicion

    # Inicializa la clase pieza territorio
    def __init__(self, tipo):
        self.tipo = tipo
        # Posicion = ['Norte','Este','Sur','Oeste']
        self.posicion = self.asignar_posicion(tipo)
        # Coordenada X y coordenada Y
        self.coordenadas = [None,None]
        # Si no hay ningun meeple colocado, self.meeples = None. Si lo hay,
        # self.meeples toma el valor de la parte en la que se coloca:
        # 0: norte, 1: noreste, 2: este, 3:sureste, 4: sur, 5: suroeste, 6: oeste, 7: noroeste
        self.meeples = None
        # Jugador que ha colocado la pieza
        self.jugador = None

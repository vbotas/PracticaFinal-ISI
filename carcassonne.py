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
        import collections
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

class Jugador:

    # Inicializa la clase jugador
    def __init__(self, nombre):
        self.nombre = nombre
        self.meeples = 8
        self.puntuacion = 0

class Pieza_terreno:

    def asignar_posicion(self, tipo):
        if tipo == 1:
            posicion = ['Granja','Granja','Camino','Camino']
        elif tipo == 2:
            posicion = ['Camino','Granja','Camino','Granja']
        elif tipo == 3:
            posicion = ['Castillo','Camino','Camino','Castillo']
        elif tipo == 4:
            posicion = ['Castillo','Granja','Granja','Castillo']
        elif tipo == 5:
            posicion = ['Granja','Castillo','Granja','Granja']
        elif tipo == 6:
            posicion = ['Castillo','Castillo','Granja','Castillo']
        elif tipo == 7:
            posicion = ['Granja','Camino','Camino','Camino']
        elif tipo == 8:
            posicion = ['Granja','Granja','Granja','Granja']  ## ESTA FIGURA TIENE UN MONASTERIO EN EL CENTRO
        elif tipo == 9:
            posicion = ['Granja','Castillo','Granja','Castillo']
        elif tipo == 10:
            posicion = ['Camino','Castillo','Camino','Granja']
        elif tipo == 11:
            posicion = ['Camino','Castillo','Camino','Camino']
        elif tipo == 12:
            posicion = ['Castillo','Castillo','Camino','Castillo']
        elif tipo == 13:
            posicion = ['Castillo','Camino','Camino','Granja']
        elif tipo == 14:
            posicion = ['Camino','Castillo','Granja','Camino']
        elif tipo == 15:
            posicion = ['Castillo','Granja','Castillo','Granja']
        elif tipo == 16:
            posicion = ['Granja','Castillo','Castillo','Granja']
        elif tipo == 17:
            posicion = ['Granja','Granja','Camino','Granja']  ## ESTA FIGURA TIENE UN MONASTERIO EN EL CENTRO
        elif tipo == 18:
            posicion = ['Camino','Camino','Camino','Camino']
        elif tipo == 19:
            posicion = ['Castillo','Castillo','Castillo','Castillo']
        return posicion
    
    # Inicializa la clase pieza territorio
    def __init__(self, tipo):
        self.posicion = self.asignar_posicion(tipo)
        self.coordenadas = [None,None]

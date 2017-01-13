import random

class Partida(object):
    jugadores = 2
    piezas_territorio = 72
    ##meeple_jugador = 8
    
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
    
    

class Jugador (object):
    marcador = 0
    meeples = 8
    def __init__(self):
        pass

class Pieza_Territorio(object):
    pieza = [0,0,0,0]
    def __init__(self):
        parte_pieza = 0
        while parte_pieza < len(self.pieza):
            num_aleat = random.randint(0,4)
            if num_aleat >= 0 and num_aleat < 1:
                self.pieza[parte_pieza] = "Monasterio"
                parte_pieza+=1
            elif num_aleat >= 1 and num_aleat < 2:
                self.pieza[parte_pieza] = "Castillo"
                parte_pieza+=1
            elif num_aleat >= 2 and num_aleat < 3:
                self.pieza[parte_pieza] = "Camino"
                parte_pieza+=1
            else:
                self.pieza[parte_pieza] = "Granja"
                parte_pieza+=1
        print (self.pieza)
        


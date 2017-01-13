

class Partida(object):

    def __init__(self, nombres_jugadores):
        

'''import random

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
    pieza1 = ['Granja','Granja','Camino','Camino']
    pieza2 = ['Camino','Granja','Camino','Granja']
    pieza3 = ['Castillo','Camino','Camino','Castillo']
    pieza4 = ['Castillo','Granja','Granja','Castillo']
    pieza5 = ['Granja','Castillo','Granja','Granja']
    pieza6 = ['Castillo','Castillo','Granja','Castillo']
    pieza7 = ['Granja','Camino','Camino','Camino']
    pieza8 = ['Granja','Granja','Granja','Granja'] ##ESTA FIGURA TIENE UN MONASTERIO EN EL CENTRO
    pieza9 = ['Granja','Castillo','Granja','Castillo']
    pieza10 = ['Camino','Castillo','Camino','Granja']
    pieza11 = ['Camino','Castillo','Camino','Camino']
    pieza12 = ['Castillo','Castillo','Camino','Castillo']
    pieza13 = ['Castillo','Camino','Camino','Granja']
    pieza14 = ['Camino','Castillo','Granja','Camino']
    pieza15 = ['Castillo','Granja','Castillo','Granja']
    pieza16 = ['Granja','Castillo','Castillo','Granja']
    pieza17 = ['Granja','Granja','Camino','Granja'] ## ESTA FIGURA TIENE UN MONASTERIO EN EL CENTRO
    pieza18 = ['Camino','Camino','Camino','Camino']
    pieza19 = ['Castillo','Castillo','Castillo','Castillo']
        

##Partida('juan','javier')
##jugador()
##Pieza_Territorio()   

'''     

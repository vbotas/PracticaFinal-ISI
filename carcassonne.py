class Partida(object):
    jugadores = 2
    piezas_territorio = 72
    meeple_jugador = 8
    
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2

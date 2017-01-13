class Partida:

    def num_jug_correcto(self, nombres_jugadores):
        num_maximo_jugadores = 4
        num_jugadores = len(nombres_jugadores)
        if num_jugadores > num_maximo_jugadores:
            return False
        else:
            return True
        

class Partida:

    def num_jug_correcto(self, nombres_jugadores):
        num_maximo_jugadores = 4
        num_jugadores = len(nombres_jugadores)
        if num_jugadores > num_maximo_jugadores:
            return False
        else:
            return True

    def nombres_jug_correcto(self, nombres_jugadores):
        import collections
        # Cuento la frecuencia de repeticion de los nombres
        freq = collections.Counter(nombres_jugadores).values()
        if max(freq) > 1:
            return False
        else:
            return True

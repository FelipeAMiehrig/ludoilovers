import random
__all__ = ['Dado']
class Dado:

    def __init__(self):
        self.ultimo_resultado = 0
        self.resultado = 0
        self.num_jogadas = 0

    def jogar(self):
        self.ultimo_resultado = self.resultado
        self.resultado = random.randint(1,6)
        self.num_jogadas += 1
        return self.resultado
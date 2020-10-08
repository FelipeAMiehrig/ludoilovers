import random
__all__ = ['atual_resultado', 'numero_jogadas', 'jogar_dado', 'jogadas']

atual_resultado = -1
numero_jogadas = 0

jogadas = list()


def jogar_dado():
    return random.randint(1, 6)


def get_jogada(indice):
    return jogadas[indice]


def get_ultima_jogada():
    return jogadas[-1]

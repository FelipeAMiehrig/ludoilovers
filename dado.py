import random
__all__ = ['jogar_dado',  'get_jogada']



jogadas = list()


def jogar_dado():
    jogadas.append(random.randint(1, 6))
    return 0


def get_jogada():
    return jogadas[-1]



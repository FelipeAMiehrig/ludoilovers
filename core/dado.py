import random
__all__ = ['jogar_dado',  'consulta_jogada', 'consulta_numero_jogadas']
jogadas = list()


def jogar_dado():
    jogadas.append(random.randint(1, 6))
    return 0


def consulta_jogada():
    return jogadas[-1]


def consulta_numero_jogadas():
    return len(jogadas)


def gera_lista_jogadas():
    return jogadas.copy()



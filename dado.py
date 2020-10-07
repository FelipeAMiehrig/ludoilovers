import random
__all__ = ['ultimo_resultado', 'atual_resultado', 'numero_jogadas', 'jogar_dado']

ultimo_resultado = -1
atual_resultado = -1
numero_jogadas = 0


def jogar_dado():
    return random.randint(1, 6)

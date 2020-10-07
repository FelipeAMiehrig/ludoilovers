__all__ = ['cria_jogador']


def cria_jogador(nome, cor, numero):
    return {'Nome': nome, 'Cor': cor, 'Numero': numero, 'Placar': 0, 'Pinos na Base': 4}

__all__ = ['cria_jogador', 'get_jogador', 'scored']

jogadores = []

def cria_jogador(nome, cor, numero, base):
    jogador = {'Nome': nome,
               'Cor': cor,
               'Numero': numero,
               'Placar': 0,
               'Base': base}
    jogadores.append(jogador)
    return 0

def get_jogador(numero):
    for jogador in jogadores:
        if jogador["Numero"] == numero:
            return jogador.copy()
    return 1

def scored(numero):
    for jogador in jogadores:
        if jogador["Numero"] == numero:
            jogador["Placar"] += 1
            return 0
    return 1



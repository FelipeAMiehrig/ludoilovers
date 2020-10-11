from pino import *
from casa import *
from jogador import *
from dado import *
from listacircular import ListaCircular
from cor import Cor
from itertools import cycle

CASAS_FALTANDO_ANDAR = 0
NUMERO_CASAS_TABULEIRO = 52
NUMERO_CASAS_BASE = 16
NUMERO_JOGADORES = 4
CASAS_CEU = 5

tabuleiro = None
pinos = list()
ceu = list()

lista_bases = list()

nomes_jogadores = list()
cores_jogadores = list()

nomes_jogadores = ['Isabella', 'Felipe', 'Miguel', 'Sergio']
cores_jogadores = [Cor(125, 255, 100), Cor(100, 50, 70), Cor(20, 55, 100), Cor(10, 80, 0)]


def cria_tabuleiro(casas):
    return cycle(casas)


def cria_casas():
    casas = list()
    for numero_casa in range(NUMERO_CASAS_TABULEIRO):
        casas.append(cria_casa(0, 0, False))
    return casas


tabuleiro = ListaCircular(cria_casas())


def inicializa_lista_bases():
    for numero_pino in range(NUMERO_PINOS // 4):
        lista_bases.append(list())


def cria_pinos():
    for pino in range(NUMERO_PINOS):
        cria_pino()


def inicializa_pinos(cores):
    inicializa_lista_bases()
    for numero_pino in range(NUMERO_PINOS // 4):
        lista_bases[0].append(cria_pino(cores[0], numero_pino, CASAS_PARA_ANDAR))
        lista_bases[1].append(cria_pino(cores[1], numero_pino, CASAS_PARA_ANDAR))
        lista_bases[2].append(cria_pino(cores[2], numero_pino, CASAS_PARA_ANDAR))
        lista_bases[3].append(cria_pino(cores[3], numero_pino, CASAS_PARA_ANDAR))


def inicializa_jogadores(nomes, cores, bases):
    for numero_jogador in range(len(nomes_jogadores)):
        cria_jogador(nomes[numero_jogador], cores[numero_jogador], numero_jogador, bases[numero_jogador])


def pino_sai_base(cor, numero_pino):
    for jogador in range(get_len_jogadores()):
        if get_jogador(jogador)['Cor'] == cor:
            pino = get_jogador(jogador)['Base'][numero_pino]
            get_jogador(jogador)['Base'][numero_pino] = None
            tabuleiro[13 * get_jogador(jogador)['Numero']]['Pinos'].append(pino)


def move_pino(casa, cor, numero_pino, quantidade_casas):
    for pino in tabuleiro[casa]['Pinos']:
        if pino['Cor'] == cor and pino['Numero'] == numero_pino:
            pino_em_movimento = tabuleiro[casa]['Pinos'].pop(tabuleiro[casa]['Pinos'].index(pino))
            tabuleiro.set_indice_atual(casa)
            for movimento in range(quantidade_casas):
                tabuleiro.next()
                # Update da interface no futuro
            # Se a casa nao for segura checa para colisoes
            if tabuleiro[casa]['Segura'] is False:
                checa_colisoes(tabuleiro[tabuleiro.get_indice_atual()]['Pinos'], cor)
            # Se for para o ceu
            if pino_em_movimento['Casas Restantes'] - quantidade_casas <= 0:
                pino_em_movimento['Casas Restantes'] = pino_em_movimento['Casas Restantes'] - quantidade_casas + CASAS_CEU
                ceu.append(pino_em_movimento)
            # Se estiver andando no tabuleiro normalmente
            else:
                pino_em_movimento['Casas Restantes'] = pino_em_movimento['Casas Restantes'] - quantidade_casas
                tabuleiro[tabuleiro.get_indice_atual()]['Pinos'].append(pino_em_movimento)


def checa_colisoes(pinos_na_casa, cor_pino):
    for pino in pinos_na_casa:
        if cor_pino != pino['Cor']:
            pinos_na_casa.pop(pinos_na_casa.index(pino))
            for jogador_atual in range(get_len_jogadores()):
                if get_jogador(jogador_atual)['Cor'] == pino['Cor']:
                    pino['Casas Restantes'] = 51
                    get_jogador(jogador_atual)['Base'][pino['Numero']] = pino
                    break


inicializa_pinos(cores_jogadores)
inicializa_jogadores(nomes_jogadores, cores_jogadores, lista_bases)

pino_sai_base(cores_jogadores[0], 0)
pino_sai_base(cores_jogadores[1], 0)
pino_sai_base(cores_jogadores[2], 0)
pino_sai_base(cores_jogadores[3], 0)
pino_sai_base(cores_jogadores[3], 1)

for jogador in range(get_len_jogadores()):
    print(get_jogador(jogador)['Base'])

print(tabuleiro)
move_pino(39, get_jogador(3)['Cor'], 0, 6)
print(tabuleiro)
move_pino(45, get_jogador(3)['Cor'], 0, 7)
print(tabuleiro)

for jogador in range(get_len_jogadores()):
    print(get_jogador(jogador)['Base'])

move_pino(0, get_jogador(3)['Cor'], 0, 37)
print(tabuleiro)

for jogador in range(get_len_jogadores()):
    print(get_jogador(jogador)['Base'])

print(ceu)

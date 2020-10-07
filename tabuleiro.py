from pino import *
from casa import *
from jogador import *
from dado import *
from cor import Cor
from itertools import cycle

CASAS_FALTANDO_ANDAR = 0
NUMERO_CASAS_TABULEIRO = 52
NUMERO_CASAS_BASE = 16
NUMERO_JOGADORES = 4

tabuleiro = cycle()
pinos = list()
jogadores = list()

base_1 = list()
base_2 = list()
base_3 = list()
base_4 = list()

nomes_jogadores = list()
cores_jogadores = list()

nomes_jogadores = ['Isabella', 'Felipe', 'Miguel', 'Sergio']
cores_jogadores = [Cor(125, 255, 100), Cor(100, 50, 70), Cor(20, 55, 100), Cor(10, 80, 0)]


def cria_tabuleiro(casas):
    return cycle(casas)


def cria_casas():
    casas = list()
    for numero_casa in range(0, 52):
        casas[numero_casa] = cria_casa(0, 0, False)
    return casas


tabuleiro = cria_tabuleiro(cria_casas())


def inicializa_pinos(cores):
    for numero_pino in range(NUMERO_PINOS / 4):
        base_1[numero_pino] = cria_pino(cores[numero_pino + 0], numero_pino, CASAS_PARA_ANDAR)
        base_2[numero_pino] = cria_pino(cores[numero_pino + 1], numero_pino, CASAS_PARA_ANDAR)
        base_3[numero_pino] = cria_pino(cores[numero_pino + 2], numero_pino, CASAS_PARA_ANDAR)
        base_4[numero_pino] = cria_pino(cores[numero_pino + 3], numero_pino, CASAS_PARA_ANDAR)


def inicializa_jogadores(nomes, cores):
    for numero_jogador in range(len(nomes_jogadores)):
        jogadores.append(cria_jogador(nomes[numero_jogador], cores[numero_jogador], numero_jogador))


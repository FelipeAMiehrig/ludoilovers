from pino import *
from casa import *
from jogador import *
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
    for numero_jogador in range(consulta_tamanho_jogadores()):
        if consulta_jogador(numero_jogador)['Cor'] == cor:
            pino = consulta_jogador(numero_jogador)['Base'][numero_pino]
            consulta_jogador(numero_jogador)['Base'][numero_pino] = None
            tabuleiro[13 * consulta_jogador(numero_jogador)['Numero']]['Pinos'].append(pino)


# Nao sei se e neceesario o argumento casa aqui que representa em qual casa o pino esta
def move_pino(cor, numero_pino, quantidade_casas, casa=0):
    # Procura o pino no tabuleiro
    for pino in tabuleiro[casa]['Pinos']:
        # Achou o pino no tabuleiro
        if pino['Cor'] == cor and pino['Numero'] == numero_pino:
            # Tira o pino da casa onde ele está atualmente e avança na lista circular
            pino_em_movimento = tabuleiro[casa]['Pinos'].pop(tabuleiro[casa]['Pinos'].index(pino))
            tabuleiro.set_indice_atual(casa)
            for movimento in range(quantidade_casas):
                tabuleiro.next()
                # Update da interface no futuro
            # Se a casa nao for segura checa para colisoes
            if tabuleiro[casa]['Segura'] is False:
                checa_colisoes(tabuleiro[tabuleiro.get_indice_atual()]['Pinos'], cor)
            # Se a quantidade de casas andadas faz ele ir para o ceu
            if pino_em_movimento['Casas Restantes'] - quantidade_casas <= 0:
                pino_em_movimento['Casas Restantes'] = pino_em_movimento['Casas Restantes'] - quantidade_casas + CASAS_CEU
                ceu.append(pino_em_movimento)
                return
            # Se a quantidade de casas andadas nao fizer ele ir para o ceu
            else:
                pino_em_movimento['Casas Restantes'] = pino_em_movimento['Casas Restantes'] - quantidade_casas
                tabuleiro[tabuleiro.get_indice_atual()]['Pinos'].append(pino_em_movimento)
                return
    # Procura o pino no ceu
    for pino in ceu:
        # Achou o pino no ceu
        if pino['Cor'] == cor and pino['Numero'] == numero_pino:
            # O dono do pino pode pontuar com aquele pino
            if quantidade_casas == pino['Casas Restantes']:
                # O jogador pontua com aquele pino
                for numero_jogador in range(consulta_tamanho_jogadores()):
                    if pino['Cor'] == consulta_jogador(numero_jogador)['Cor']:
                        pontuou(numero_jogador)
                        ceu.pop(ceu.index(pino))
            # O dono do pino não pode pontuar com aquele pino
            else:
                # Checa se nao vai extrapolar o ceu, movimento nao permitido pelas regras do jogo
                if pino['Casas Restantes'] - quantidade_casas >= 0:
                    # Anda no ceu
                    pino['Casas Restantes'] -= quantidade_casas
                else:
                    # Nao da para andar, feedback de interface entra aqui
                    pass


def checa_colisoes(pinos_na_casa, cor_pino):
    for pino in pinos_na_casa:
        if cor_pino != pino['Cor']:
            pinos_na_casa.pop(pinos_na_casa.index(pino))
            for jogador_atual in range(consulta_tamanho_jogadores()):
                if consulta_jogador(jogador_atual)['Cor'] == pino['Cor']:
                    pino['Casas Restantes'] = 51
                    consulta_jogador(jogador_atual)['Base'][pino['Numero']] = pino
                    break


inicializa_pinos(cores_jogadores)
inicializa_jogadores(nomes_jogadores, cores_jogadores, lista_bases)

pino_sai_base(cores_jogadores[0], 0)
pino_sai_base(cores_jogadores[1], 0)
pino_sai_base(cores_jogadores[2], 0)
pino_sai_base(cores_jogadores[3], 0)
pino_sai_base(cores_jogadores[3], 1)

for numero_jogador_atual in range(consulta_tamanho_jogadores()):
    print(consulta_jogador(numero_jogador_atual)['Base'])

print(tabuleiro)
move_pino(consulta_jogador(3)['Cor'], 0, 6, 39)
print(tabuleiro)
move_pino(consulta_jogador(3)['Cor'], 0, 7, 45)
print(tabuleiro)
move_pino(consulta_jogador(3)['Cor'], 0, 38, 0)
print(tabuleiro)

print(ceu)
move_pino(consulta_jogador(3)['Cor'], 0, 1)
print(ceu)
move_pino(consulta_jogador(3)['Cor'], 0, 1)
print(ceu)
move_pino(consulta_jogador(3)['Cor'], 0, 1)
print(ceu)
move_pino(consulta_jogador(3)['Cor'], 0, 1)
print(ceu)
move_pino(consulta_jogador(3)['Cor'], 0, 1)
print(ceu)

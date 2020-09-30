import numpy as np
import itertools
__all__ = ['Pino']

class Pino:

    cores = ["vermelho", "azul", "amarelo", "verde"]

    # placeholder para coordenadas de pinos no tabuleiro
    # parte do tabuleiro recursiva
    casas_rec = [(i, i) for i in np.arange(0,52)]
    # casas base
    casas_base = [(i*100, i*100) for i in np.arange(1,17)]
    n_pinos = 0

    @staticmethod  # função que devolve o indice real da lista para recursão
    def cycle(k):
        return k % len(Pino.casas_rec)

    def __init__(self):
        # número da cor
        self.n_cor = int(np.floor(Pino.n_pinos/4))
        # número do pino na lista de pinos (0:15)
        self.n_pino = Pino.n_pinos
        # número do pino do jogador (1:4)
        self.n_pino_jogador = Pino.n_pinos % 4 + 1
        self.cor = Pino.cores[self.n_cor]
        self.coord = Pino.casas_base[Pino.n_pinos]
        # contador de casas andadas
        self.cont = 0
        # iterador da lista recursiva
        self.i = self.n_cor*13 - 1

        Pino.n_pinos += 1

    # andar "n" casas conforme o dado
    def anda(self, n):
        self.cont += n
        self.i += n
        self.i = Pino.cycle(self.i)
        self.coord = Pino.casas_rec[self.i]

    # voltar a base caso seja "comido"
    def volta_base(self):
        # casa especifica do pino
        self.coord = Pino.casas_base[self.n_pino]
        self.cont = 0
        # iterador especifico da cor
        self.i = self.n_cor * 13 - 1

    # sair da base caso caia 6 no dado
    def sai_base(self):
        self.cont += 1
        self.i += 1
        self.coord = Pino.casas_rec[self.i]


    def __str__(self):
        return "cor: '{}', n_pino_jogador: {}, coord: {}, cont: {}, i: {}".format(self.cor, self.n_pino_jogador, self.coord, self.cont, self.i)


# teste com lista de pinos
lista_pinos = [Pino() for i in range(0,16)]



print(str(lista_pinos[14]))
lista_pinos[14].sai_base()
print(str(lista_pinos[14]))
lista_pinos[14].anda(6)

print(str(lista_pinos[14]))

lista_pinos[14].anda(6)
print(str(lista_pinos[14]))

lista_pinos[14].anda(6)
print(str(lista_pinos[14]))

lista_pinos[14].anda(6)
print(str(lista_pinos[14]))

lista_pinos[14].volta_base()
print(str(lista_pinos[14]))










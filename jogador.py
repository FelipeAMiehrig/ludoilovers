__all__ = ['Jogador']


class Jogador:

    cores = ["vermelho", "azul", "amarelo", "verde"]
    n_jogadores = 0

    def __init__(self, nome):
        self.nome = nome
        self.cor = Jogador.cores[Jogador.n_jogadores]
        self.score = 0
        self.pinos_base = 4

        Jogador.n_jogadores += 1

    def scored(self):
        self.score +=1

    def ganhou(self):
        if self.score == 4:
            return 1
        else:
            return 0

# nao sei se esses sao necessarios

    def sair_base(self):
        if self.pinos_base > 0:
            self.pinos_base -= 1

    def voltar_base(self):
        self.pinos_base += 1

    def __repr__(self):
        return "Jogador('{}')".format(self.nome)

    def __str__(self):
        return "nome: '{}', cor: '{}', score: {}, pinos_base: {}".format(self.nome, self.cor, self.score, self.pinos_base)




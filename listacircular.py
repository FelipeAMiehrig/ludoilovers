from itertools import cycle
import sys


class ListaCirular:
    def __init__(self, lista):
        self.tamanho = len(lista)
        self.lista_circular = lista
        self.indice_atual = 0

    def next(self):
        if self.indice_atual != self.tamanho - 1:
            self.indice_atual += 1
        else:
            self.indice_atual = 0
        return self.lista_circular[self.indice_atual]

    def set_indice_atual(self, indice):
        self.indice_atual = indice

    def __getitem__(self, indice):
        return self.lista_circular[self.indice_atual]

    def __setitem__(self, indice, valor):
        self.lista_circular[indice] = valor
        return

    def __str__(self):
        string = ''
        for elemento in self.lista_circular:
            string = f'{string}{elemento}'
            if elemento != self.tamanho - 1:
                string = f'{string}\n'
        return string


lista = [{'A': 5}, {'B': 8}, {'C': 2}, {'D': 0}, {'E': 0}, {'F': 18}]
lista_circular = ListaCirular(lista)

print(lista_circular)
lista_circular[2] = {'Z': 5}
# print(lista_circular)
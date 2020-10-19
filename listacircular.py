class ListaCircular:
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

    def get_indice_atual(self):
        return self.indice_atual

    def __getitem__(self, indice):
        return self.lista_circular[indice]

    def __setitem__(self, indice, valor):
        self.lista_circular[indice] = valor
        return

    def __repr__(self):
        self.set_indice_atual(0)
        string = ''
        for elemento in self.lista_circular:
            string = f'{string}{self.indice_atual} -> {elemento}'
            if elemento != self.tamanho - 1:
                string = f'{string}\n'
            self.next()
        return string

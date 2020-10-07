from dado import *
from jogador import *
from itertools import cycle


def main():
    lista_circular = cycle(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    print(next(lista_circular))

    pass

if __name__ == "__main__":
    main()


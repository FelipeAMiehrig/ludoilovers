__all__ = ['cria_pino', 'CASAS_PARA_ANDAR', 'NUMERO_PINOS', 'get_pino']

NUMERO_PINOS = 16
CASAS_PARA_ANDAR = 51

lista_pinos = list()


def cria_pino(cor, numero, casas_restantes):
    return {'Cor': cor, 'Numero': numero, 'Casas Restantes': casas_restantes}


def get_pino(indice):
    return lista_pinos[indice]


def get_pinos():
    return lista_pinos

__all__ = ['cria_pino', 'CASAS_PARA_ANDAR', 'NUMERO_PINOS', ]

NUMERO_PINOS = 16
CASAS_PARA_ANDAR = 51




def cria_pino(cor, numero, casas_restantes):
    return {'Cor': cor, 'Numero': numero, 'Casas Restantes': casas_restantes}

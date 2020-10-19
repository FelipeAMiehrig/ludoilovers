import numpy as np

__all__ = ['NUMERO_CASAS_TABULEIRO', 'cria_casa']

NUMERO_CASAS_TABULEIRO = 52
NUMERO_CASAS_CEU = 6


def cria_casa(coordenada_x, coordenada_y, segura):
    return {'Coordenada X': coordenada_x, 'Coordenada Y': coordenada_y, 'Segura': segura, 'Pinos': list()}

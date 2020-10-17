from casa import *
import unittest

def test_01_criar_casa_ok_criacao_com_sucesso(self):
    print("Caso de Teste 01 - Criação com sucesso")
    retorno_esperado = cria_casa(0,0,True)
    self.assertEqual(resultado_esperado, {'Coordenada X': 0,
                     'Coordenada Y': 0, 'Segura': True,
                     'Pinos': list()})
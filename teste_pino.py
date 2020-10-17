from pino import *
import unittest

def test_01_criar_pino_ok_criado_com_sucesso(self):
    print("Caso de Teste 01 - Criar com sucesso")
    retorno_esperado = cria_pino("vermelho", 1, 23)
    self.assertIn({'Cor': "vermelho",
                   'Numero': 1,
                   'Casas Restantes': 23},
                   retorno_esperado)

def test_02_get_pino_ok_get_com_sucesso(self):
    print("Caso de Teste 02 - Consulta pino com sucesso")
    retorno_esperado = get_pino(1)
    self.assertIn(retorno_esperado, lista_pinos)

def test_03_get_pinos_ok_get_com_sucesso(self):
    print("Caso de Teste 03 - Consulta pinos com sucesso")
    retorno_esperado = get_pinos()
    self.assertEqual(retorno_esperado, lista_pinos)

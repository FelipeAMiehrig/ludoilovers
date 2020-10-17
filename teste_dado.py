from dado import *
import unittest

def test_01_jogar_dado_ok_condicao_retorno(self):
    print("Caso de Teste 01 - jogada com sucesso")
    retorno_esperado = jogar_dado()
    self.assertEqual(retorno_esperado, 0)

def test_02_jogar_dado_ok_jogadas_registradas(self):
    print("Caso de Teste 02 - jogada com sucesso")
    jogar_dado()
    jogar_dado()
    retorno_esperado = consulta_numero_jogadas()
    self.assertEqual(retorno_esperado, 3)

def test_03_consulta_jogada_ok_consulta_com_sucesso(self):
    print("Caso de Teste 03 - consulta bem sucedida")
    retorno_esperado = consulta_jogada()
    self.assertIn(retorno_esperado, [1, 2, 3, 4, 5, 6])




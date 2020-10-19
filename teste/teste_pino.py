from core.pino import *
import unittest


class TestesPino(unittest.TestCase):
    def test_01_criar_pino_ok_criado_com_sucesso(self):
        print("Caso de Teste 01 - Criar com sucesso")
        retorno_esperado = cria_pino("vermelho", 0, 23)
        self.assertEqual({'Cor': "vermelho",
                          'Numero': 0,
                          'Casas Restantes': 23}, retorno_esperado)

from jogador import *
import unittest

def test_01_criar_jogador_ok_condicao_retorno(self):
    print("Caso de Teste 01 - Criar com sucesso")
    retorno_esperado = cria_jogador("Daniel", "vermelho", 1, (0,0))
    self.assertEqual(retorno_esperado, 0)

def test_02_criar_jogador_ok_criado_com_sucesso(self):
    print("Caso de Teste 02 - Verifica criação")
    self.assertIn({'Nome': "Daniel", 'Cor': "vermelho",
                   'Numero': 1, 'Placar': 0,
                   'Base': (0,0)}, gera_relacao_jogadores())

def test_03_criar_jogador_nok_nome_vazio(self):
    print("Caso de Teste 03 - Impede a criação caso o nome" +
          "do jogador seja vazio")
    retorno_esperado = cria_jogador("", "vermelho", 1, (0,0))
    self.assertEqual(retorno_esperado, 1)

def test_04_criar_jogador_nok_mais_que_quatro_jogadores(self):
    print("Caso de Teste 04 - Impede a criação de um jogador" +
          "caso o numero de jogadores exceda 4")
    cria_jogador("Rafael", "verde", 2, (0, 0))
    cria_jogador("Maria", "amarelo", 3, (0, 0))
    cria_jogador("Antonia", "azul", 4, (0, 0))
    retorno_esperado = cria_jogador("Errado", "roxo", 5, (0,0))
    self.assertEqual(retorno_esperado, -1)

def test_05_consulta_jogador_ok_consulta_com_sucesso(self):
    print("Caso de teste 05 - Verifica consulta")
    retorno_esperado = consulta_jogador(2)
    self.assertEqual({'Nome': "Rafael", 'Cor': "verde",
                   'Numero': 2, 'Placar': 0,
                   'Base': (0,0)}, retorno_esperado)

def test_06_consulta_jogador_nok_consulta_mal_sucedida(self):
    print("Caso de teste 06 - Consulta falha")
    retorno_esperado = consulta_jogador(5)
    self.assertEqual(retorno_esperado, 1)

def test_07_pontuou_ok_condicao_retorno(self):
    print("Caso de teste 07 - pontua jogador")
    retorno_esperado = pontuou(1)
    self.assertEqual(retorno_esperado, 0)

def test_08_pontuou_ok_pontuacao_bem_sucedida(self):
    print("Caso de teste 08 - pontuação bem sucedida")
    jogador = consulta_jogador(1)
    pontos = jogador["Placar"]
    self.assertEqual(pontos, 1)

def test_09_pontuou_nok_pontuacao_mal_sucedida(self):
    print("Caso de Teste 09- pontuação mal sucedida")
    retorno_esperado = pontuou(5)
    self.assertEqual(retorno_esperado, 1)

def test_10_consulta_tamanho_jogadores_ok_consulta_bem_sucedida(self):
    print("Caso de teste 10 - consulta bem sucedida")
    retorno_esperado = consulta_tamanho_jogadores()
    self.assertEqual(retorno_esperado,4)

def test_11_gera_relacao_jogadores(self):
    print("Caso teste 11 - gera relação jogadores")
    retorno_esperado = gera_relacao_jogadores()
    self.assertEqual([{'Nome': "Daniel", 'Cor': "vermelho",
                   'Numero': 1, 'Placar': 1,
                   'Base': (0,0)},
                   {'Nome': "Rafael", 'Cor': "verde",
                    'Numero': 2, 'Placar': 0,
                    'Base': (0, 0)},
                   {'Nome': "Maria", 'Cor': "amarelo",
                    'Numero': 3, 'Placar': 0,
                    'Base': (0, 0)},
                   {'Nome': "Antonia", 'Cor': "azul",
                    'Numero': 4, 'Placar': 0,
                    'Base': (0, 0)}], retorno_esperado)








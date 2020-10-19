import unittest
from core.tabuleiro import *

inicializa_pinos(cores_jogadores)
inicializa_jogadores(nomes_jogadores, cores_jogadores, lista_bases)


class TestesTabuleiro(unittest.TestCase):
    def teste_01_sai_com_pino_jogador_01(self):
        print('Teste 1 - OK')
        pino_saiu = consulta_jogador(0)['Base'][0]
        pino_sai_base(cores_jogadores[0], 0)
        self.assertEqual(tabuleiro[0]['Pinos'][0], pino_saiu)

    def teste_02_sai_com_pino_jogador_02(self):
        print('Teste 2 - OK')
        pino_saiu = consulta_jogador(1)['Base'][0]
        pino_sai_base(cores_jogadores[1], 0)
        self.assertEqual(tabuleiro[13]['Pinos'][0], pino_saiu)

    def teste_03_sai_com_pino_jogador_03(self):
        print('Teste 3 - OK')
        pino_saiu = consulta_jogador(2)['Base'][0]
        pino_sai_base(cores_jogadores[2], 0)
        self.assertEqual(tabuleiro[26]['Pinos'][0], pino_saiu)

    def teste_04_sai_com_pino_jogador_04(self):
        print('Teste 4 - OK')
        pino_saiu_0 = consulta_jogador(3)['Base'][0]
        pino_saiu_1 = consulta_jogador(3)['Base'][1]
        pino_sai_base(cores_jogadores[3], 0)
        pino_sai_base(cores_jogadores[3], 1)
        self.assertEqual(tabuleiro[39]['Pinos'][0], pino_saiu_0)
        self.assertEqual(tabuleiro[39]['Pinos'][1], pino_saiu_1)

    def teste_05_bases_com_none(self):
        print('Teste 5 - OK')
        for numero_jogador_atual in range(consulta_tamanho_jogadores()):
            self.assertIsNone(consulta_jogador(numero_jogador_atual)['Base'][0])
        self.assertIsNone(consulta_jogador(3)['Base'][1], None)

    def teste_06_movimentacao_padrao(self):
        print('Teste 6 - OK')
        pino_movimento = tabuleiro[39]['Pinos'][0]
        move_pino(consulta_jogador(3)['Cor'], 0, 6, 39)
        self.assertEqual(tabuleiro[45]['Pinos'][0], pino_movimento)

    def teste_07_lista_circular_voltando_inicio(self):
        print('Teste 7 - OK')
        pino_movimento = tabuleiro[45]['Pinos'][0]
        move_pino(consulta_jogador(3)['Cor'], 0, 7, 45)
        self.assertEqual(tabuleiro[0]['Pinos'][0], pino_movimento)

    def teste_08_pino_comeu_pino(self):
        print('Teste 8 - OK')
        self.assertIsNotNone(consulta_jogador(0)['Base'][0])

    def teste_09_vai_pro_ceu(self):
        print('Teste 9 - OK')
        pino_movimento = tabuleiro[0]['Pinos'][0]
        move_pino(consulta_jogador(3)['Cor'], 0, 38, 0)
        self.assertEqual(tabuleiro[38]['Pinos'], [])
        self.assertEqual(ceu[0], pino_movimento)

    def teste_10_movimento_ceu(self):
        print('Teste 10 - OK')
        pino_movimento = ceu[0]
        move_pino(consulta_jogador(3)['Cor'], 0, 1)
        pino_movimento['Casas Restantes'] = 4
        self.assertEqual(ceu[0], pino_movimento)

    def teste_11_pontuacao_jogador(self):
        print('Teste 11 - OK')
        move_pino(consulta_jogador(3)['Cor'], 0, 1)
        move_pino(consulta_jogador(3)['Cor'], 0, 1)
        move_pino(consulta_jogador(3)['Cor'], 0, 1)
        move_pino(consulta_jogador(3)['Cor'], 0, 1)
        self.assertEqual(gera_relacao_jogadores()[3]['Placar'], 1)

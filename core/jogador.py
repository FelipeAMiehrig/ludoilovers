__all__ = ['cria_jogador', 'consulta_jogador', 'pontuou', 'consulta_tamanho_jogadores', 'gera_relacao_jogadores']

jogadores = []


def cria_jogador(nome, cor, numero, base):
    if len(jogadores) == 4:
        return -1
    elif nome == '':
        return 1
    jogador = {'Nome': nome,
               'Cor': cor,
               'Numero': numero,
               'Placar': 0,
               'Base': base}
    jogadores.append(jogador)
    return 0


def consulta_jogador(numero):
    for jogador in jogadores:
        if jogador["Numero"] == numero:
            return jogador.copy()
    return 1


def consulta_tamanho_jogadores():
    return len(jogadores)


def pontuou(numero):
    for jogador in jogadores:
        if jogador["Numero"] == numero:
            jogador["Placar"] += 1
            return 0
    return 1

def gera_relacao_jogadores():
    return jogadores.copy()

try:
	connection = mysql.connector.connect(host = 'localhost', database = 'ludo', user ='root', password = 'root')
	sql = ("""INSERT INTO jogador (nome, pontuacao, pinos_base, cor) VALUES (%s, %d, %d, %s)""", nome, placar, base, cor)
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	print(cursor.rowcount, "Registro inserido")
	cursor.close()
except Error as e:
	print("Erro de conexão", e)
finally:
	if (connection.is_connected()):
		cursor.close()
		connection.close()
		print("Conexão encerrada")
import random
import mysql.connector
from mysql.connector import Error

__all__ = ['jogar_dado',  'consulta_jogada', 'consulta_numero_jogadas']
jogadas = list()


def jogar_dado():
    jogadas.append(random.randint(1, 6))
    return 0


def consulta_jogada():
    return jogadas[-1]


def consulta_numero_jogadas():
    return len(jogadas)


def gera_lista_jogadas():
    return jogadas.copy()

try:
	connection = mysql.connector.connect(host = 'localhost', database = 'ludo', user = 'root', password = 'root')
	sql = ("""INSERT INTO dado (numero) VALUES (%d)""", jogadas[-1])
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

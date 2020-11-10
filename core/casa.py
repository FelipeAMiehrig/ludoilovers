import numpy as np

__all__ = ['NUMERO_CASAS_TABULEIRO', 'cria_casa']

NUMERO_CASAS_TABULEIRO = 52
NUMERO_CASAS_CEU = 6


def cria_casa(coordenada_x, coordenada_y, segura):
    return {'Coordenada X': coordenada_x, 'Coordenada Y': coordenada_y, 'Segura': segura, 'Pinos': list()}

try:
	connection = mysql.connector.connect(host = 'localhost', database = 'ludo', user ='root', password = 'root')
	sql = ("""INSERT INTO casa (segura) VALUES (%s)""", segura)
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
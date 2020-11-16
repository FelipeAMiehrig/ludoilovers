__all__ = ['cria_pino', 'CASAS_PARA_ANDAR', 'NUMERO_PINOS', ]

NUMERO_PINOS = 16
CASAS_PARA_ANDAR = 51




def cria_pino(cor, numero, casas_restantes):
    return {'Cor': cor, 'Numero': numero, 'Casas Restantes': casas_restantes}

try:
	connection = mysql.connector.connect(host = 'localhost', database = 'ludo', user ='root', password = 'root')
	sql = ("""INSERT INTO pino (casas_restantes, cor) VALUES (%d, %s)""", casas_restantes, cor)
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
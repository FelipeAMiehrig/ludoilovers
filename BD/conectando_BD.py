import mysql.connector
from mysql.connector import Error

try:
	connection = mysql.connector.connect(host='localhost', database='ludo', user='root', password='root')
	if connection.is_connected():
		db_Info = connection.get_server_info()
		print("Conectado ao MySQL Server versão ", db_Info)
		cursor = connection.cursor()
		cursor.execute("select database()")
		record = cursor.fetchone()
		print("Conectado ao banco de dados ", record)
except Error as e:
	print("Erro de conexão", e)
finally:
	if (connection.is_connected()):
		cursor.close()
		connection.close()
		print("Conexão encerrada")
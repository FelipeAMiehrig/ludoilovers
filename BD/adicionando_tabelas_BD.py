import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root",
  database = "ludo  "
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE jogador (nome VARCHAR(30), pontuacao INT, pinos_base INT, cor VARCHAR(30) AUTO_INCREMENT PRIMARY KEY)")
mycursor.execute("CREATE TABLE pino (casas_restantes INT, cor VARCHAR(30) AUTO_INCREMENT FOREIGN KEY)")
mycursor.execute("CREATE TABLE jogo (cor VARCHAR(30) AUTO_INCREMENT FOREIGN KEY)")
mycursor.execute("CREATE TABLE dado (numero INT AUTO_INCREMENT PRIMARY KEY)")
mycursor.execute("CREATE TABLE casa (segura VARCHAR(30) AUTO_INCREMENT PRIMARY KEY)")
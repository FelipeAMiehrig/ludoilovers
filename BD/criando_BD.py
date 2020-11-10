import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE ludo")

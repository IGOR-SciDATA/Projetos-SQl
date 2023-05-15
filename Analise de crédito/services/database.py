import sqlite3

connection = sqlite3.connect('clientes.db',check_same_thread=False)
cursor = connection.cursor()
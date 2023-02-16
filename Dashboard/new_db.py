import sqlite3

# Criando ou fazendo conexão no Banco de Dados
connection = sqlite3.connect('Empregado.db')
print("Conectando..")

# Criando o objeto cursor para executar as consultas na tabela
cursor = connection.cursor()

#Dropa a tabela caso já exista
cursor.execute("DROP TABLE IF EXISTS empregados")

# Definição de tabela
create_table = '''CREATE TABLE empregados(
                person_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR2(40),
                idade NUMBER(2),
                emprego VARCHAR2(20));
                '''
  
# Criando tabela no Banco de Dados
cursor.execute(create_table)
print("Banco Criado com Sucesso!!")
# Importando as Bibliotecas necessarias
import sqlite3
import csv

# Criando ou fazendo conexão no Banco de Dados
connection = sqlite3.connect('Clientes.db')
print("Conectando..")

# Criando o objeto cursor para executar as consultas na tabela
cursor = connection.cursor()

#Dropa a tabela caso já exista
cursor.execute("DROP TABLE IF EXISTS clientes")

# Definição de tabela
create_table = '''CREATE TABLE clientes(
                person_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR2(50) NOT NULL,
                cpf VARCHAR2(14),
                tel VARCHAR2(30),
                email VARCHAR2(50),
                salario NUMBER(5,3),
                score NUMBER(4));
                '''
  
# Criando tabela no Banco de Dados
cursor.execute(create_table)
print("Banco Criado com Sucesso!!")

# Abrindo arquivo dados.csv file
file = open('dados.csv')
  
# Lendo o conteudo do arquivo dados.csv
contents = csv.reader(file)

# Query SQL para inserir os dados na tabela
insert_records = "INSERT INTO clientes (nome,cpf,tel,email,salario,score) VALUES(?,?,?,?,?,?)"
  
# Importando os conteudos do arquivo para a tabela
cursor.executemany(insert_records, contents)

# Comitando os dados inseridos
connection.commit()
print("Dados Inseridos!")
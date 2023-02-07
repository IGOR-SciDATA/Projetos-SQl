# Importando as Bibliotecas necessarias
import sqlite3
import csv

# Criando ou fazendo conexão no Banco de Dados
connection = sqlite3.connect('Energia_Brazil.db')
print("Conectando..")

# Criando o objeto cursor para executar as consultas na tabela
cursor = connection.cursor()

#Dropa a tabela caso já exista
cursor.execute("DROP TABLE IF EXISTS energia")

# Definição de tabela
create_table = '''CREATE TABLE energia(
                date data,
                hora VARCHAR2(8),
                demanda_mwhora REAL);
                '''
  
# Criando tabela no Banco de Dados
cursor.execute(create_table)
print("Banco Criado com Sucesso!!")

# Abrindo arquivo dados.csv file
file = open('dados.csv')
  
# Lendo o conteudo do arquivo dados.csv
contents = csv.reader(file)

# Query SQL para inserir os dados na tabela
insert_records = "INSERT INTO energia (date,hora,demanda_mwhora) VALUES(?,?,?)"
  
# Importando os conteudos do arquivo para a tabela
cursor.executemany(insert_records, contents)

# Comitando os dados inseridos
connection.commit()
print("Dados Inseridos!")
import services.database as db;
import Controllers.ClientController as ClientController

#Insere os dados
def inserir(id,nome,idade,emprego):
    db.cursor.execute("""
    INSERT INTO empregados (nome,idade,emprego)
    VALUES ('%s','%s','%s')
    """ % (nome,idade,emprego))
    db.connection.commit()

#Consulta os dados
def SelectTodos():
    db.cursor.execute("SELECT * FROM empregados") 
    
    recset = db.cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows

#Exclui o dado
def excluir (id):
    db.cursor.execute("""
            DELETE FROM empregados WHERE person_id = '%s'
    """ % (id))
    db.connection.commit()

#Função para dar Select em apenas um dado do BD
def selecionar_id (id):
    db.cursor.execute("""
            SELECT * FROM empregados WHERE person_id = '%s'
    """ % (id))
    recset = db.cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows

# função que altera dados e commita a atualização no BD
def alterar (nome, idade, emprego, id):
    db.cursor.execute("""
            UPDATE empregados SET (nome, idade, emprego) = ('%s', '%s', '%s')  WHERE person_id = '%s'
    """ % (nome, idade, emprego, id))
    db.connection.commit()
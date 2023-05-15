import services.database as db;
import Controllers.ClientController as ClientController

#Insere os dados
def inserir(id,input_name,input_cpf,input_tel,input_email,
                               input_salario,input_score):
    db.cursor.execute("""
    INSERT INTO clientes (nome,cpf,tel,email,salario,score)
    VALUES ('%s','%s','%s','%s','%s','%s')
    """ % (input_name,input_cpf,input_tel,input_email,
                               input_salario,input_score))
    db.connection.commit()

#Consulta os dados
def SelectTodos():
    db.cursor.execute("SELECT * FROM clientes") 
    
    recset = db.cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows

#Exclui o dado
def excluir (id):
    db.cursor.execute("""
            DELETE FROM clientes WHERE person_id = '%s'
    """ % (id))
    db.connection.commit()

#Função para dar Select em apenas um dado do BD
def selecionar_cpf (input_reg):
    db.cursor.execute("""
            SELECT * FROM clientes WHERE cpf = '%s'
    """ % (input_reg))
    recset = db.cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows

def selecionar_id (id):
    db.cursor.execute("""
            SELECT * FROM clientes WHERE person_id = '%s'
    """ % (id))
    recset = db.cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows

# função que altera dados e commita a atualização no BD
def alterar (update_name, update_cpf, update_tel,update_email,update_sal,update_sc, id):
    db.cursor.execute("""
            UPDATE clientes SET (nome,cpf,tel,email,salario,score) = ('%s', '%s', '%s','%s','%s','%s')  WHERE person_id = '%s'
    """ % (update_name, update_cpf, update_tel,update_email,update_sal,update_sc, id))
    db.connection.commit()
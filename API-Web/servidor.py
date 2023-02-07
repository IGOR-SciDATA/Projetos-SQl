from flask import Flask, request, Response, g
import sqlite3

#Cria a aplicação
app = Flask(__name__)

DB_URL = "Energia_Brazil.db"

@app.before_request
def before_request():
    print("Conectando ao banco!")
    conn = sqlite3.connect(DB_URL)
    g.conn = conn

@app.teardown_request
def after_request(exception):
    if g.conn is not None:
        g.conn.close()
        print("Desconectado!")

def query_dict_ENERGIA(conn, query):
    cursor = conn.cursor()
    cursor = cursor.execute(query)

    energia_dict = [{'date':row[0],'hora':row[1],'demanda_mwhora':row[2]}
                     for row in cursor.fetchall()]
    return energia_dict

@app.route("/")
def home():
	return "<h1>Dados ENERGIA BRAZIL</h1>"

@app.route("/energia")
def get_energia():
    
    query = """
          SELECT * from energia;    
    """
    energia_dict = query_dict_ENERGIA(g.conn, query)
    return {'energia':energia_dict}

@app.route("/energia/<date>")
def get_energia_date(date):
	
	query = """
          SELECT date,hora,demanda_mwhora
		  FROM energia
		  WHERE "date" = "{}";    
    """.format(date)
    
	energia_dict = query_dict_ENERGIA(g.conn, query)
    
	return {'energia': energia_dict}

@app.route("/energia/<info>/<value>")
def get_energia_info(info, value):
	
	if value.isnumeric():
		value = float(value)

	query = """
        SELECT date,hora,demanda_mwhora
		FROM energia
		WHERE "{}" = "{}";    
    """.format(info, value)
    
	energia_dict = query_dict_ENERGIA(g.conn, query)
					
	return {'energia': energia_dict}

if __name__ == "__main__":
	app.run(debug=True)

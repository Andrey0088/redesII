import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="meubanco", # Nome do serviço do banco de dados no docker-compose
            database=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD")
        )
        return conn
    except psycopg2.OperationalError as e:
        return f"Erro ao conectar no banco de dados: {e}"

@app.route('/')
def index():
    conn = get_db_connection()
    if isinstance(conn, str):
        return conn

    # Apenas para testar, vamos pegar a versão do PostgreSQL
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()

    return f"<h1>Conexão com o Banco de Dados bem-sucedida!</h1><p>Versão do PostgreSQL: {db_version[0]}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
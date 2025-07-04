import sqlite3

class Database:
    def __init__(self, db_name="clientes.db"):
        self.connection = sqlite3.connect(db_name) # {connection} Conexão com o Banco de Dados 
        self.cursor = self.connection.cursor() # {cursor} Garçom que leva e trás pédidos
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        self.connection.commit() # {commit} Salvar permanente

    def execute(self, query, params=None):
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self, query, params=None):
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def fetchone(self, query, params=None):
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        return self.cursor.fetchone()
    
    def close(self):
        self.connection.close()

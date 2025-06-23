from database import Database

class Cliente:
    def __init__(self):
        self.db = Database()

    def adicionar_cliente(self, nome, email):
        query = "INSERT INTO clientes (nome, email) VALUES (?, ?)"
        try:
            self.db.execute(query, (nome, email))
            print(f"Cliente '{nome}' adicionado com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar cliente: {e}")

    def listar_clientes(self):
        query = "SELECT * FROM clientes"
        clientes = self.db.fetchall(query)
        if clientes:
            for cliente in clientes:
                print(cliente)
        else:
            print("Nenhum cliente encontrado")

    def atualizar_cliente(self, cliente_id, novo_nome, novo_email):
        query = "UPDATE clientes SET nome = ?, email = ? WHERE id = ?"
        try:
            self.db.execute(query, (novo_nome, novo_email, cliente_id))
            print(f"Cliente id {cliente_id} com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")

    def deletar_cliente(self, cliente_id):
        query = "DELETE FROM clientes WHERE id = ?"
        try:
            self.db.execute(query, (cliente_id,))
            print(f"Cliente id {cliente_id} deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar o cliente: {e}")

    def buscar_cliente_por_id(self, cliente_id,):
        query = "SELECT * FROM clientes WHERE id = ?"
        cliente = self.db.fetchone(query, (cliente_id,))
        if cliente:
            print(f"Cliente encontrado: {cliente}")
        else:
            print(f"Cliente com ID {cliente_id} não encontrado.")
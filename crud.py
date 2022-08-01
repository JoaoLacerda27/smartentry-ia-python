import conexao

class Carro():
    def __init__(self):
        conexao.Connection.__init__(self)

    def insert(self, *args):
        try:
            sql = "INSERT INTO"
            self.execute(sql)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)

    def delete(self, id):
        try:
            sql_search = "SELECT"

            if not self.query(sql_search):
                return "Registro não encontrado para delete"
            sql_delete = f"DELETE FROM"

            self.execute(sql_delete)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)

    def update(self, id, *args):
        try:
            sql = f"UPDATE %s -> argumento"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)

    def search(self, *args, type_s="placa"):
        sql = f"SELECT * FROM Carro WHERE placa LIKE %s"
        data = self.query(sql, args)
        if data:
            return data
        return  "Registro não encontrado"





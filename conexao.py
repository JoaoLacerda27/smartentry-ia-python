import psycopg2 as db

class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user" : "root",
                "password" : "Ciencia2022",
                "host" : "smartentryhomol.cjgzoxlh8rpz.sa-east-1.rds.amazonaws.com",
                "port" : "5432",
                "database" : "postgres"
            }
        }

class Connection(Config):
    def __init__(self):
        Config.__init__(self)

        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro na conexão: ", e)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cursos.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursos.execute(sql, params or ())
        return self.fetchall()






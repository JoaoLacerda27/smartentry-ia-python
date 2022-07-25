import psycopg2

class Conexao(object):
    _db=None

    def __init__(self, mhost, db, usr, passwd):
        self._db = psycopg2.connect(
            host = mhost,
            database = db,
            user = usr,
            password = passwd
        )

    def inserir (self, sql):
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()

        except:
            return False
        return True




import conexao

con = conexao.Conexao('smartentryhomol.cjgzoxlh8rpz.sa-east-1.rds.amazonaws.com',
'postgres', 'root', 'Ciencia2022')

sql = "INSERT INTO ECARRO VALUES (default , 'BR5-FJHG', 1)"

if con.inserir(sql):
    print("inserido com sucesso!")
else:
    print("Fail")


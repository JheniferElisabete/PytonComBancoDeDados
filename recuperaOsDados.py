import pymysql.cursors
conexao = pymysql.connect(
    # Fazendo a passagem de parametros
    #Ip de onde esta passando o banco de dados
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

with conexao.cursor() as cursor:
    cursor.execute('select * from cadastros')
    #para cada linha cria um dicionario
    resultado = cursor.fetchall()
print(resultado)
#for limita as buscas
for dado in resultado:
    #mostra cada linha separada
    print(dado)
#mostra apenas uma dado
for dado in resultado:
    #mostra apenas do nome e endereço
    print(dado['nome'], dado['endereco'])

for dado in resultado:
    #mostra formatado
    print('o nome é {} e mora no endereço {}'.format(dado['nome'], dado['endereco']))
#outra forma fazendo direto do sql
with conexao.cursor() as cursor:
    cursor.execute('select nome from cadastros')
    resultado = cursor.fetchall()
print(resultado)
# ou
for dado in resultado:
    #mostra dicionarios como se fosse dados unicos
    print(dado)

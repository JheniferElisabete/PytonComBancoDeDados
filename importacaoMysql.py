'''importando a biblioteca
'''
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
cursor = conexao.cursor()
#executa os codigos em SQL
##cursor.execute('create table pessoas(nome varchar(30), idade int, endereco varchar(100)) ;')
#passando para uma variavel
##x = 'drop table pessoas'
##cursor.execute(x)

#fecha o arquivo
##conexao.close()
##cursor.close()
#para não ter que ficar abrindo e fechando cursor
y = 'create table teste (nome varchar(10));'
with conexao.cursor() as cursor:
    cursor.execute(y)
#aqui ele fechou o cursor automaticamente
#inserindo dado na tabela
a = input('Digite seu nome ')
with conexao.cursor() as cursor:
    cursor.execute('insert into teste values("Jhenifer");')
    #Salva os dados na tabela do banco de dados, sempre que executar ele vai inserir os dados em baixo do outro
    #outro mode de fazer é
    cursor.execute('insert into teste values("{}");'.format('Camila'))
    #Ou passando como variavel
    cursor.execute('insert into teste values("{}");'.format(a))
    conexao.commit()
#Criando uma tabela mais complexa
with conexao.cursor() as cursor:
    cursor.execute('create table cadastros (id int primery key auto_increment, nome varchar(10) not null, endereco varchar (300));')
    conexao.commit()
    #inserir dado na tabela
b = input('Digite seu nome')
c = input('Digite seu endereco')
with conexao.cursor() as cursor:
    cursor.execute('insert into cadastros (nome, endereco) values ("{`}","{`}")'.format(b, c))
    conexao.commit()
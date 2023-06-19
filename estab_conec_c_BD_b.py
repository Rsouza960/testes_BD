from mysql.connector import connect

con = connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd = '123456'

)

print(type(con))

# aqui é onde vamos fazer as operações
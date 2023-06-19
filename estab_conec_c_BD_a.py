import sqlite3

con = sqlite3.connect('empresa.db')

print(type(con))

#é aqui que vamos fazer realizar as operacoes com BD

con.close()
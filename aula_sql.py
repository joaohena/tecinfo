import sqlite3

# Conectando ao banco de dados (caso não exista, será criado)
conn = sqlite3.connect('BolsaValores.db')

# Executando um comando SQL para criar uma tabela
# conn.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)')

# Inserindo um novo usuário na tabela
# conn.execute("INSERT INTO usuarios (nome, idade) VALUES ('João', 25)")

# Realizando uma consulta para recuperar todos os usuários com idade maior que 20
consulta = conn.execute("SELECT * FROM usuarios WHERE idade > 20")

# Percorrendo os resultados da consulta
for row in consulta:
    print(row)
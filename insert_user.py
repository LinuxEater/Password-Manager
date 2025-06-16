import sqlite3
import os

# Verifica se o banco original existe
db_path = 'data_base.db'
alt_db_path = 'main_users.db'

if not os.path.exists(db_path):
    print(f"Atenção: '{db_path}' não encontrado. Usando banco alternativo '{alt_db_path}'.")
    db_path = alt_db_path
else:
    print(f"Banco de dados encontrado: '{db_path}'")

# Conecta ao banco
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Cria a tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usermaindb (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Dados do usuário
username = 'Moises'
password = 'moises.4002'

try:
    cursor.execute("INSERT INTO usermaindb (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    print(f"Usuário '{username}' inserido com sucesso no banco '{db_path}'!")
except sqlite3.IntegrityError:
    print(f"Erro: o usuário '{username}' já existe no banco '{db_path}'.")

conn.close()

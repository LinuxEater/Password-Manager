import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('data_base.db')
cursor = conn.cursor()

# Selecionar os 40 primeiros IDs existentes
cursor.execute('SELECT id FROM users ORDER BY id ASC LIMIT 40')
ids_para_deletar = cursor.fetchall()

# Deleta cada um
for id_tuple in ids_para_deletar:
    id = id_tuple[0]
    cursor.execute('DELETE FROM users WHERE id = ?', (id,))
    print(f"Deletado usuário com id: {id}")

# Finaliza
conn.commit()
conn.close()

print("Deleção concluída.")
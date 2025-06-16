import sqlite3
import os
import crud
from tkinter import *
from tkinter import messagebox

# Verifica qual banco usar
db_path = 'usermaindb.db'
fallback_db = 'main_users.db'

if not os.path.exists(db_path):
    print(f"Atenção: '{db_path}' não encontrado. Usando '{fallback_db}' como alternativa.")
    db_path = fallback_db

# Conexão com o banco escolhido
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Janela de login
login_window = Tk()
login_window.title("Login")
login_window.geometry("300x200")
login_window.resizable(False, False)

# Função de login
def login():
    username = entry_user.get()
    password = entry_pass.get()

    try:
        cursor.execute("SELECT * FROM usermaindb WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", f"Welcome, {username}!")
            login_window.destroy()
            # Aqui você pode abrir a janela principal do app
            # import crud
            crud.main()
            
        else:
            messagebox.showerror("Error", "Invalid username or password.")
    except sqlite3.OperationalError as e:
        messagebox.showerror("Database Error", f"Error: {str(e)}\nIs the 'usermaindb' table created?")

# Layout da interface
Label(login_window, text="Username:").pack(pady=5)
entry_user = Entry(login_window)
entry_user.pack()

Label(login_window, text="Password:").pack(pady=5)
entry_pass = Entry(login_window, show="*")
entry_pass.pack()

Button(login_window, text="Login", command=login).pack(pady=10)

login_window.mainloop()

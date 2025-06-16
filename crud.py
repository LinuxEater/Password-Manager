import sqlite3
from tkinter import messagebox, Menu
from tkinter import *

# Conexão com o banco
connection = sqlite3.connect('data_base.db')
cursor = connection.cursor()

# Criação da tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        site_link TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
connection.commit()

#create login window


password = Tk()

def export_to_csv():
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()
    with open('./users.csv', 'w') as f:
        for user in users:
            f.write(','.join(map(str, user)) + '\n')
    messagebox.showinfo("Export Notification", "Data exported to users.csv successfully")
    print('Data exported to users.csv successfully')

def showing():
    def reset():
        for cell in password.winfo_children():
            cell.destroy()
        header()
        showing()
    
    def clear_entry(event):
        event.widget.delete(0, 'end')

    def insert_user():
        cursor.execute('''INSERT INTO users(email, password, site_link) VALUES(?,?,?)''', 
                       (email_txt.get(), passes_txt.get(), link_txt.get()))
        connection.commit()
        messagebox.showinfo("Pass Notification", "User Inserted Successfully")
        print('User inserted successfully')
        reset()
    
    def delete_user():
        cursor.execute('''DELETE FROM users WHERE id = ?''', (user_delete.get(),))
        connection.commit()
        messagebox.showinfo("Pass Notification", "User Deleted Successfully")
        print('User deleted successfully')
        reset()
    
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()
    row_count = 1
    for user in users:
        Label(password, text=user[0], bg="#FFFFFF", fg="black", font="Helvetica 16 bold", padx="5", pady="5", 
              borderwidth=2, relief="groove").grid(row=row_count, column=0, sticky=N+S+E+W)
        Label(password, text=user[1], bg="#FFFFFF", fg="black", font="Helvetica 16 bold", padx="5", pady="5", 
              borderwidth=2, relief="groove").grid(row=row_count, column=1, sticky=N+S+E+W)
        Label(password, text=user[2], bg="#FFFFFF", fg="black", font="Helvetica 16 bold", padx="5", pady="5", 
              borderwidth=2, relief="groove").grid(row=row_count, column=2, sticky=N+S+E+W)
        Label(password, text=user[3], bg="#FFFFFF", fg="black", font="Helvetica 16 bold", padx="5", pady="5", 
              borderwidth=2, relief="groove").grid(row=row_count, column=3, sticky=N+S+E+W)
        Label(password, text=user[4], bg="#FFFFFF", fg="black", font="Helvetica 16 bold", padx="5", pady="5", 
              borderwidth=2, relief="groove").grid(row=row_count, column=4, sticky=N+S+E+W)
        row_count += 1

    global email_txt, passes_txt, link_txt, user_delete
    email_txt = Entry(password, borderwidth=2, relief="groove")
    email_txt.insert(0, "Email")
    email_txt.bind("<FocusIn>", clear_entry)
    email_txt.grid(row=row_count + 1, column=1, sticky=N+S+E+W)

    passes_txt = Entry(password, borderwidth=2, relief="groove")
    passes_txt.insert(0, "Password")
    passes_txt.bind("<FocusIn>", clear_entry)
    passes_txt.grid(row=row_count + 1, column=2, sticky=N+S+E+W)

    link_txt = Entry(password, borderwidth=2, relief="groove")
    link_txt.insert(0, "Link")
    link_txt.bind("<FocusIn>", clear_entry)
    link_txt.grid(row=row_count + 1, column=3, sticky=N+S+E+W)

    Button(password, text="Add", bg="green", fg="white", command=insert_user,
           font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove").grid(row=row_count + 1, column=4, sticky=N+S+E+W)

    user_delete = Entry(password, borderwidth=2, relief="groove")
    user_delete.insert(0, "Id")
    user_delete.bind("<FocusIn>", clear_entry)
    user_delete.grid(row=row_count + 2, column=3, sticky=N+S+E+W)

    Button(password, text="Delete", bg="red", fg="white", command=delete_user,
           font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove").grid(row=row_count + 2, column=4, sticky=N+S+E+W)

    Button(password, text="Refresh", bg="blue", fg="white", command=reset,
           font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove").grid(row=row_count + 3, column=4, sticky=N+S+E+W)

    Button(password, text="Export to CSV", bg="orange", fg="white", command=export_to_csv,
           font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove").grid(row=row_count + 4, column=4, sticky=N+S+E+W)

def fetch():
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()
    for user in users:
        print(user)

def header():
    password.title("Password Manager")
    Label(password, text="ID", bg="#142E54", fg="white", font="Helvetica 16 bold",
          padx="5", pady="5", borderwidth=2, relief="groove").grid(row=0, column=0, sticky=N+S+E+W)
    Label(password, text="Email", bg="#142E54", fg="white", font="Helvetica 16 bold",
          padx="5", pady="5", borderwidth=2, relief="groove").grid(row=0, column=1, sticky=N+S+E+W)
    Label(password, text="Password", bg="#142E54", fg="white", font="Helvetica 16 bold",
          padx="5", pady="5", borderwidth=2, relief="groove").grid(row=0, column=2, sticky=N+S+E+W)
    Label(password, text="Link/Url", bg="#142E54", fg="white", font="Helvetica 16 bold",
          padx="5", pady="5", borderwidth=2, relief="groove").grid(row=0, column=3, sticky=N+S+E+W)
    Label(password, text="Created At", bg="#142E54", fg="white", font="Helvetica 16 bold",
          padx="5", pady="5", borderwidth=2, relief="groove").grid(row=0, column=4, sticky=N+S+E+W)

# Executa a interface
header()
showing()
password.mainloop()
connection.commit()
connection.close()

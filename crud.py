import sqlite3
from tkinter import messagebox,Menu
from tkinter import *

connection = sqlite3.connect('data_base.db')
cursor = connection.cursor()

password = Tk()

def showing():
    def reset():
        for cell in password.winfo_children():
            cell.destroy()
        header()
        showing()
    
    def clear_entry(event):
        event.widget.delete(0, 'end')

    def insert_user():
        cursor.execute('''INSERT INTO users(email, password, site_link) VALUES(?,?,?)''',(email_txt.get(), passes_txt.get(),link_txt.get()))
        connection.commit()
        messagebox.showinfo("Pass Notification", "User Inserted Successfully")
        print('User inserted successfully')
        reset()
    
    def delete_user():
        cursor.execute('''DELETE FROM users WHERE id = ?''',(user_delete.get(),))
        connection.commit()
        messagebox.showinfo("Pass Notification", "User Deleted Successfully")
        print('User deleted successfully')
        reset()
    
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()
    row_count = 1
    for user in users:
        id = Label(password, text=user[0], bg="#FFFFFF",fg="black", font="Helvetica 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
        id.grid(row=row_count, column=0, sticky=N+S+E+W)
    
        email = Label(password, text=user[1], bg="#FFFFFF",fg="black", font="Helvetica 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
        email.grid(row=row_count, column=1, sticky=N+S+E+W)

        passes = Label(password, text=user[2], bg="#FFFFFF",fg="black", font="Helvetica 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
        passes.grid(row=row_count, column=2, sticky=N+S+E+W)

        link = Label(password, text=user[3], bg="#FFFFFF",fg="black", font="Helvetica 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
        link.grid(row=row_count, column=3, sticky=N+S+E+W)

        created_at = Label(password, text=user[4], bg="#FFFFFF",fg="black", font="Helvetica 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
        created_at.grid(row=row_count, column=4, sticky=N+S+E+W)
        row_count += 1
        
    global email_txt, passes_txt, link_txt, user_delete  # Declare as global
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
    
    btn_add = Button(password, text="Add", bg="green",fg="white", command=insert_user, font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    btn_add.grid(row=row_count + 1, column=4, sticky=N+S+E+W)
    
    
    #deleting data
    user_delete = Entry(password, borderwidth=2, relief="groove")
    user_delete.insert(0, "Id")
    user_delete.bind("<FocusIn>", clear_entry)
    user_delete.grid(row=row_count + 2, column=3, sticky=N+S+E+W)
    
    delete = Button(password, text="Delete", bg="red",fg="white", command=delete_user, font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    delete.grid(row=row_count + 2, column=4, sticky=N+S+E+W)

    restart = Button(password, text="Refresh", bg="Blue",fg="white", command=reset, font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    restart.grid(row=row_count + 3, column=4, sticky=N+S+E+W)
def fetch():
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()
    for user in users:
        print(user)

def header():
    password.title("Password Manager")
    #adding a header with 8 columns
    id = Label(password, text="ID", bg="#142E54",fg="white", font="Helvetica 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    id.grid(row=0, column=0, sticky=N+S+E+W)
    
    email = Label(password, text="Email", bg="#142E54",fg="white", font="Helvetica 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    email.grid(row=0, column=1, sticky=N+S+E+W)

    passes = Label(password, text="Password", bg="#142E54",fg="white", font="Helvetica 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    passes.grid(row=0, column=2, sticky=N+S+E+W)

    link = Label(password, text="Link/Url", bg="#142E54",fg="white", font="Helvetica 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    link.grid(row=0, column=3, sticky=N+S+E+W)

    created_at = Label(password, text="Created At", bg="#142E54",fg="white", font="Helvetica 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    created_at.grid(row=0, column=4, sticky=N+S+E+W)

header()
showing()
password.mainloop()
connection.commit()
connection.close()
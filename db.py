from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
def insert():
    name=e_name.get();
    if(name ==""):
        MessageBox.showinfo("Insert status","Все поля должны быть заполнены")
    else:
        con= mysql.connect(host="localhost", user="root", password="root", database="autocatalog", port="3316")
        
        create_users = "INSERT INTO `category`(`name`) VALUES ('{name}')".format(name=name)

        execute_query(con, create_users) 
        

window =Tk()
window.geometry('600x600')
window.title("Проба базы данных. Основные функции")

name=Label(window,text="Название категории")
name.place(relx=0.5, rely=0.5, anchor=S)


e_name = Entry()
e_name.place(relx=0.5, rely=0.55, anchor=S)

insert = Button(window, text="Добавить категорию", command=insert)
insert.place(relx=0.5,rely=0.7, anchor=S)


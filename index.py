from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter import ttk

# создание рабочей области , выше модули и библиотеки       
window = Tk()  
window.title("Автокаталог")  
window.geometry('1920x1080')

con= mysql.connect(host="localhost", user="root", password="root", database="vocabulary", port="3316")

# фоновое фото
img = Image.open('C:/Users/yesb/Desktop/учеба какие-то файлы/Курсовая работа Программирование/bcg.jpg')
width = 1926
ratio = (width / float(img.size[0]))
height = int((float(img.size[1]) * float(ratio)))
imag = img.resize((width, height), Image.Resampling.LANCZOS)
image = ImageTk.PhotoImage(imag)
panel = Label(window, image=image)
panel.pack(side="top", fill="both", expand="no")

#проверка подключения базы данных
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
#функция вывода на экран из бд
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

#функция добавления каталога
def create_catalog():
      window_create = Toplevel()
      window_create.title("Создать новый каталог")  
      window_create.geometry('300x300')
      window_create.resizable(False,False)
      window_create.configure(bg="white")
      window_create.grab_set()
      
      new_cat = Label(window_create, text="ИМЯ КАТАЛОГА " , font=('Advent Pro',14), bg="white")  
      new_cat.place(relx=0.5, rely=0.15,anchor=N) 
      new_cat_name = Entry(window_create,width=20, relief="groove")  
      new_cat_name.place(relx=0.5, rely=0.37,anchor=CENTER)
      insert = Button(window_create, fg="#ffbf1f",bg="white", text="ДОБАВИТЬ", font=('Advent Pro',14), command= lambda: insert(new_cat_name.get()))
      insert.place(relx=0.5,rely=0.60, anchor=S)
      def insert(name):
          
          if(name ==""):
              MessageBox.showinfo("Insert status","Все поля должны быть заполнены")
          else:
              con= mysql.connect(host="localhost", user="root", password="root", database="autocatalog", port="3316")
              create_cat = "INSERT INTO `category`(`name`) VALUES ('{name}')".format(name=name)
              execute_query(con, create_cat)
              MessageBox.showinfo("Insert status","Новый каталог создан")
              new_cat_name.delete(0,END)
#функция редактирования 
def edit():
      window_edit = Toplevel()
      window_edit.title("РЕДАКТОР КАТЕГОРИЙ")  
      window_edit.geometry('400x500')
      window_edit.configure(bg="white")
      window_edit.resizable(False,False)
      window_edit.grab_set()

      con= mysql.connect(host="localhost", user="root", password="root", database="autocatalog", port="3316")
      select_terms = "SELECT `name` from `category` "
      terms = execute_read_query(con, select_terms)
      option=[None]*(len(terms))
      for row in range(0,len(terms)):
          option[row]=terms[row]

      var = StringVar()
      combobox = ttk.Combobox(window_edit, textvariable = var, font=('Advent Pro',16))
      combobox['values'] = option
      combobox['state'] = 'readonly'
      combobox.pack(fill='x',padx= 3, pady=3)

      warning=Label(window_edit, text="ВНИМАНИЕ! ПРИ УДАЛЕНИЕ КАТАЛОГА, \n ВСЕ АВТО В ЭТО КАТАЛОГЕ УДАЛЯТСЯ АВТОМАТИЧЕСКИ. \n ВО ИЗБЕЖАНИЕ ЭТОГО, ОТРЕДАКТИРУЙТЕ КАТАЛОГИ В АВТО",
                    fg="red",bg="white",font=('Advent Pro',10))
      warning.place(relx=0.1, rely=0.1)
      delete_but = Button(window_edit,width=20, height=0 , fg="#ffbf1f",bg="white", text="УДАЛЕНИЕ", font=('Advent Pro',14), command=lambda: delete_cat(var.get()))  
      delete_but.place(relx=0.3, rely=0.3)
      edit_but = Button(window_edit,width=20, height=0 , fg="#ffbf1f",bg="white",text="РЕДАКТИРОВАНИЕ", font=('Advent Pro',14,), command= lambda: update_car(var.get()))  
      edit_but.place(relx=0.3, rely=0.7)

      def delete_cat(name):
            if(name ==""):
              MessageBox.showinfo("Insert status","Выберите каталог для удаления")
            else:
              con= mysql.connect(host="localhost", user="root", password="root", database="autocatalog", port="3316")
              create_cat = "DELETE FROM `category` WHERE `name`='{name}'".format(name=name)
              #каскадное удаление машин 
              execute_query(con, create_cat)
              MessageBox.showinfo("Insert status","Каталог удален")
              
      def delete_car(sql_car,sql_pas):
              con= mysql.connect(host="localhost", user="root", password="root", database="autocatalog", port="3316")
              #каскадное удаление машин 
              execute_query(con, sql_car)
              execute_query(con,sql_pas)
              MessageBox.showinfo("Insert status","Каталог удален")
      def edit_car(id_car):
          print(id_car)
          
      def update_car(catalog):
            if(catalog ==""):
              MessageBox.showinfo("Insert status","Выберите каталог для редактирования")
            else:
                window_update = Toplevel()
                window_update.title("РЕДАКТОР АВТО")  
                window_update.geometry('800x800')
                window_update.configure(bg="white")
                window_update.resizable(False,False)
                window_update.grab_set()
                
                  
                con= mysql.connect(host="localhost", user="root", password="root", database="autocatalog", port="3316")
                id_catalog = " SELECT car.id_pas,`marka`,`model`,car.gosnomer,`vin`,`type_car`,`type_cat`,`power`,`photo`, car.id_car FROM `car` inner join `pasport` on car.id_pas=pasport.id_pasport where `id_cat`= (SELECT `id_cat` FROM `category` where `name`='{catalog}')".format(catalog=catalog)
                cars=execute_read_query(con,id_catalog)

                header=['Марка: ','Модель: ','Госномер: ','Год выпуска: ','№ объявления: ']

                siderow=1
                for row in range(len(cars)):
                    
                    text = Text(window_update, width=50, height=5, font=('Open Sans Condensed Light', 14))
                    text.grid(row=siderow, column=0)
                    
                    btn_params_id_car=cars[row][4]
                    
                    for column in range(0,5,1):
                        #e = Label(window, width=10, fg='blue', text=cars[row][column], anchor=CENTER)
                        
                        #e.grid(row=(row+1), column=(column+1), pady=5)
                        #print(header[column],': ' ,cars[row][column], end='\n')
                        '''
                        headers = Label(window, width=10, fg='red', text=header[column])
                        headers.grid(row=column)
                        e = Label(window, width=10, fg='blue', text=(cars[row]), anchor=CENTER)
                        e.grid(row=(column), column=1, pady=10)
                        '''
                       # img = PhotoImage(file='bcg.png')
                        text.insert(END,header[column])
                        text.insert(END, " ")
                        text.insert(END, cars[row][column])
                        text.insert(END,'\n')

                        photo = PhotoImage(file = r"edit.png")
  
                        
                        #Button(root, text = 'Click Me !', image = photo).pack(side = TOP)
                          
                        editbutton=Button(window_update,image=photo, width=50, height=50, command=lambda: edit_car(cars[row][9]))
                        editbutton.grid(row=siderow, column=5)
                        
                        delbutton=Button(window_update,text="Удалить", command= lambda: delete_car("DELETE FROM `car` WHERE `id_car` = '{id_car}'".format(id_car=cars[row][9]), "DELETE FROM `pasport` WHERE `id_pasport`='{id_pas}'".format(id_pas=cars[row][0])))
                        delbutton.grid(row=siderow, column=7)
                        
                    siderow=siderow+2

                
    
#кнопки на главном экране
open_cat = Button(window,width=20, height=0 , fg="#ffbf1f",bg="white", text="ОТКРЫТЬ", font=('Advent Pro',14))  
open_cat.place(relx=0.025, rely=0.8)

new_cat = Button(window,width=20, height=0 , fg="#ffbf1f",bg="white",text="НОВЫЙ", font=('Advent Pro',14), command=create_catalog)  
new_cat.place(relx=0.15, rely=0.8)

edit_cat = Button(window,width=20, height=0 , fg="#ffbf1f",bg="white", text="РЕДАКТОР", font=('Advent Pro',14), command=edit)  
edit_cat.place(relx=0.275, rely=0.8)


mainloop()

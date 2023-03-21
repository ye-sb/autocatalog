from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk, Image
from tkinter import filedialog
window =Tk()
window.geometry('900x1000')
window.title("Вывод авто")

con= mysql.connect(host="localhost", user="root", password="root", database="autocatalog", port="3316")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def anketa(id_ca,con):
    new_window = Toplevel(window)
    new_window.title(id_ca)  
    new_window.geometry('500x800')
    new_window.configure(bg="white")

    x = 'C:/Users/yesb/Desktop/учеба какие-то файлы/Курсовая работа Программирование/bcg.jpg'
    img = Image.open(x)
    img = img.resize((250,250),Image.LANCZOS)
    img =ImageTk.PhotoImage(img)
    panel = Label(new_window,image=img)
    panel.image=img
    panel.place(relx=0.2, rely=0)

    select_cars = "SELECT car.id_pas,`marka`,`model`,car.gosnomer,`vin`,`type_car`,`type_cat`,`power` ,`photo` FROM `car` inner join `pasport` on car.id_pas=pasport.id_pasport where `id_car`='{id_ca}'".format(id_ca=id_ca)
    cars = execute_read_query(con, select_cars)
    header=['№ПТС','Марка: ','Модель: ','Госномер: ','Vin: ','Тип ТС: ','Категория ТС: ','Мощность']


    for row in range(len(cars)):
        
        text = Text(new_window, height=10, font=('Open Sans Condensed Light', 14))
        text.place(relx=0,rely=0.3)

        for column in range(0,8,1):

            text.insert(END,header[column])
            text.insert(END, " ")
            text.insert(END, cars[row][column])
            text.insert(END,'\n')
     
def photo(photo):
    x = 'C:/Users/yesb/Desktop/учеба какие-то файлы/Курсовая работа Программирование/{photo}'.format(photo=photo)
    img = Image.open(x)
    img = img.resize((250,250),Image.LANCZOS)
    img =ImageTk.PhotoImage(img)
    panel = Label(window,image=img)
    panel.image=img
    panel.place(relx=0.2, rely=0)
select_cars = "SELECT car.id_pas,`marka`,`model`,car.gosnomer,`vin`,`type_car`,`type_cat`,`power` ,`photo` FROM `car` inner join `pasport` on car.id_pas=pasport.id_pasport "
cars = execute_read_query(con, select_cars)
header=['№ПТС','Марка: ','Модель: ','Госномер: ','Vin: ','Тип ТС: ','Категория ТС: ','Мощность']


sidecolumn=0
for row in range(len(cars)):
    photo(cars[row][8])
    text = Text(width=20,height=10, font=('Open Sans Condensed Light', 20))
    text.grid(row=sidecolumn, column=3)
    
   
    for column in range(0,8,1):

        text.insert(END,header[column])
        text.insert(END, " ")
        text.insert(END, cars[row][column])
        text.insert(END,'\n')
        
        
        
    sidecolumn=sidecolumn+1



  
'''
Уточнить, как сделать вывод как в консоли, только в окне, так как двумерный массив в лейбл не выводится
виджет текст меня не устраивает, либо найти атрибут который запрещает редактироват текст в виджете ТЕКСТ

Идея следующая: в цикле вывод краткой информации по авто, и при нажатии кнопки на конкретной анкете будет открываться окн с полным описанием авто.  в кнопке будет передаваться id машины
запрос есть в блокноте .Либо если я не смогу этого сделать, то просто в цикл выше кину все данные и сделаю кнопку избранное 
'''


   
        



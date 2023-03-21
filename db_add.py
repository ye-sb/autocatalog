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
    marka=emarka.get()
    model=emodel.get()
    gosnomer=egosnomer.get()
    pasport=epasport.get()
    vin=evin.get()
    type_car=etype.get()
    type_cat=ecarcateg.get()
    year=eyear.get()
    power=epower.get()


    
    
    
    if(marka =="" or model =="" or gosnomer=="" or pasport=="" or type_car=="" or type_cat=="" ):
        MessageBox.showinfo("Insert status","Все поля со * должны быть заполнены")
    else:
        con= mysql.connect(host="localhost", user="root", password="root", database="autocatalog", port="3316")
        
        insert_pasport = "INSERT INTO `pasport`(`id_pasport`, `vin`, `type_car`, `type_cat`, `year_car`, `gosnomer`, `power`)VALUES('{pasport}','{vin}','{type_car}','{type_cat}','{year}','{gosnomer}','{power}')".format(pasport=pasport,vin=vin,type_car=type_car,type_cat=type_cat,year=year,gosnomer=gosnomer,power=power)
        insert_car = "INSERT INTO `car`(`id_cat`, `id_pas`, `marka`, `model`, `gosnomer`) VALUES ('3','{pasport}','{marka}','{model}','{gosnomer}')".format(pasport=pasport,marka=marka,model=model,gosnomer=gosnomer)

        execute_query(con, insert_pasport)
        execute_query(con, insert_car)
        

        

window =Tk()
window.geometry('900x1000')
window.title("Добавление авто")


marka=Label(window,text="Марка *")
marka.place(relx=0.5, rely=0.1, anchor=S)
emarka = Entry()
emarka.place(relx=0.5, rely=0.15, anchor=S)

model=Label(window,text="Модель *")
model.place(relx=0.5, rely=0.2, anchor=S)
emodel = Entry()
emodel.place(relx=0.5, rely=0.25, anchor=S)

gosnomer=Label(window,text="Госномер *")
gosnomer.place(relx=0.5, rely=0.3, anchor=S)
egosnomer = Entry()
egosnomer.place(relx=0.5, rely=0.35, anchor=S)

pasport=Label(window,text="№ ПТС *")
pasport.place(relx=0.5, rely=0.4, anchor=S)
epasport = Entry()
epasport.place(relx=0.5, rely=0.45, anchor=S)

vin=Label(window,text="VIN")
vin.place(relx=0.5, rely=0.5, anchor=S)
evin = Entry()
evin.place(relx=0.5, rely=0.55, anchor=S)

cartype=Label(window,text="Тип *")
cartype.place(relx=0.5, rely=0.6, anchor=S)
etype = Entry()
etype.place(relx=0.5, rely=0.65, anchor=S)

carcateg=Label(window,text="Категория *")
carcateg.place(relx=0.5, rely=0.7, anchor=S)
ecarcateg = Entry()
ecarcateg.place(relx=0.5, rely=0.75, anchor=S)

year=Label(window,text="Год выпуска ТС")
year.place(relx=0.5, rely=0.8, anchor=S)
eyear = Entry()
eyear.place(relx=0.5, rely=0.85, anchor=S)

power=Label(window,text="Мощность (л.с)")
power.place(relx=0.5, rely=0.9, anchor=S)
epower = Entry()
epower.place(relx=0.5, rely=0.95, anchor=S)



insert = Button(window, text="Добавить авто", command=insert)
insert.place(relx=0.2,rely=0.5, anchor=S)


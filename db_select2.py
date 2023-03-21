from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

def openfn():
    filename=filedialog.askopenfilename(title="open")
    print(filename)
    return filename

x = 'C:/Users/yesb/Desktop/учеба какие-то файлы/Курсовая работа Программирование/bcg.jpg'
img = Image.open(x)
img = img.resize((250,250),Image.LANCZOS)
img =ImageTk.PhotoImage(img)
panel = Label(root,image=img)
panel.image=img
panel.pack()
#btn = Button(root, text="Open img", command=open_img).pack()
 

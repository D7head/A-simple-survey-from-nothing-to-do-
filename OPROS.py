from tkinter import * 
from tkinter import messagebox 
import random 

name = input("Как вас зовут: ")

def no():
    messagebox.showinfo('  ', f"Спасибо, {name}! Ваш голос учтен!")
    quit()


def motionMouse(event):
    btnYes.place(x=random.randint(0, 900), y=random.randint(0, 900))
    



root = Tk()
root.geometry('1000x1000')
root.title('Опрос')
root.resizable(width=False, height=False)
root['bg'] = 'white'

Label = Label(root, text=f"{name}, ты хочешь стать богатым?", font='Arial 20 bold', bg='white').pack()
btnYes = Button(root, text='ДАА', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text='НЕЕЕТТ', font='Arial 20 bold', command=no ).place(x=350, y=100)


root.mainloop()
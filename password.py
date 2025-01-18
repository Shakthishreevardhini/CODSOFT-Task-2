from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import string
import secrets
import random
import pyperclip

def generator():
    textDelete = passwordField
    textDelete.delete(0, 'end')
    upper=list(string.ascii_uppercase)
    lower=list(string.ascii_lowercase)
    digits=list(string.digits)
    punctuation=list(string.punctuation)

    all=upper+lower+digits+punctuation
    password_len=int(length_Box.get())
    part1=round(password_len*(30/100))
    part2=round(password_len*(20/100))
    password=""
    for i in range(part1):
        password+=secrets.choice(upper)
        password+=secrets.choice(lower)
    for i in range(part2):
        password+=secrets.choice(punctuation)
        password+=secrets.choice(lower)
    passwordField.insert(0,password)

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)
def clear():
    text=passwordField
    text.delete(0,'end')

root=Tk()
root.geometry("220x220")
myColor='#FFF4E6'
fontColor='#1D4C6B'
root.config(bg=myColor)
choice=IntVar()

passwordLabel=Label(root,text='Password Generator', font=('Times', 18, 'bold'), bg=myColor,fg=fontColor)
passwordLabel.grid(pady=10)

lengthLabel=Label(root,text="Passowrd Length",font=('cairo',13,'bold'),bg=myColor,fg=fontColor)
lengthLabel.grid()

length_Box=Spinbox(root,from_=8,to_=32,font=Font,width=5,wrap=True)
length_Box.grid()

generateButton=Button(root,text='Generate',font=(Font,10,'bold'),bg=myColor,command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=20,bd=2,font=Font)
passwordField.grid()

copyButton=Button(root,text='Copy to Clipboard',font=(Font,10,'bold'),bg=myColor,command=copy)
copyButton.grid(pady=5)

butClear=Button(root,text='Clear', font=(Font,10,'bold'),bg=myColor, command=clear)
butClear.grid(pady=5)


root.mainloop()
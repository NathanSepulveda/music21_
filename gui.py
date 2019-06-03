
from tkinter import *
 
from tkinter import messagebox
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
window.configure(background='blue')
window.geometry('350x200')
current = 0
lbl = Label(window, text="Hello", fg="blue")
lbl.configure(background='red')
 
lbl.grid(column=2, row=0)
def clicked():
    global current
    current += 1
    print(current)
    print(txt.get())
    if current == 0:
        lbl.configure(text="zero")
    else: lbl.configure(text=current)

def minus():
    global current
    current += -1
    print(current)
    
    
    if current == 0:
        lbl.configure(text="zero")
    else: lbl.configure(text=current)
    # messagebox.showinfo('Message title', 'Message content')
 
btn = Button(window,text='+', command=clicked)
btn2 = Button(window,text='-', command=minus)
txt = Entry(window,width=10)
txt.grid(column=6,row=1)
txt.configure(background='yellow')
 
btn.grid(column=0,row=0)
btn2.grid(column=5,row=0)


 
window.mainloop()
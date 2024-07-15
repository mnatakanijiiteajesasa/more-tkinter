from tkinter import *


def click():
    print("I am him")
    new_text = textbox1.get()
    label1.config(text=new_text)


label1["text"]= "I ate her")
label1.pack()

window = Tk()
window.wm_minsize(width=600, height=400)

textbox1 = Entry(width=20)
textbox1.pack()

button1 = Button(text="Press Me", command=click)
button1.pack()

# textbox1 = Entry(width=20)


window.mainloop()







from tkinter import *


def add_on():
    number = enter_text.get()
    number = int(number)
    answer = output_text["text"]
    answer = int(answer)
    total = number + answer
    output_text["text"] = total


def reset():
    total = 0
    output_text["text"] = 0
    enter_text.delete(0, END)
    enter_text.focus()


total = 0
num = 0

window = Tk()
window.title("adding together")
window.geometry("450x100")

enter_label = Label(text="Enter a number: ")
enter_label.place(x=50, y=20, width=100, height=25)

enter_text = Entry.text = 0
enter_text.place(x=150, y=20, width=100, height=25)
enter_text["justify"] = "center"
enter_text.focus()

add_button = Button(text="Add", command=add_on)
add_button.place(x=300, y=20, width=50, height=25)

output_label = Label(text="answer=")
output_label.place(x=50, y=50, width=100, height=25)

output_text = Message(text=0)
output_text.place(x=150, y=50, width=100, height=25)
output_text["bg"] = "blue"
output_text["relief"] = "sunken"


clear_button = Button(text="Clear", command="relief")
clear_button.place(x=300, y=50, width=50, height=25)

window.mainloop()




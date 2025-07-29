# TKinter

import tkinter


def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    my_label.config(text=new_text)


# window

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = tkinter.Label(text="I am a Label", font=("Roboto", 12, "normal"))
# my_label.pack(side="left")
my_label.grid(column=0, row=0)

# button

my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

# Entry

input = tkinter.Entry(width=20)
input.grid(column=2, row=2)

my_label2 = tkinter.Label(text="Luke X", font=("Roboto", 12, "normal"))
my_label2.grid(column=2, row=5, sticky="w")






window.mainloop()

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

# Label

my_label = tkinter.Label(text="I am a Label", font=("Roboto", 12, "normal"))
my_label.pack(padx=16, pady=16)

# button

my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.pack(padx=16)

# Entry

input = tkinter.Entry(width=20)
input.pack()





window.mainloop()

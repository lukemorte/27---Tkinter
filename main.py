import tkinter


def button_clicked():
    result = round(float(entry.get()) * 1.6, 1)
    converted_num.config(text=result)


window = tkinter.Tk()
window.title("Miles to km converter")
window.config(padx=20, pady=20)


# row 1

entry = tkinter.Entry()
entry.grid(column=1, row=0)

miles_units = tkinter.Label()
miles_units.grid(column=2, row=0)
miles_units.config(text="Miles")

# row 2

info_text = tkinter.Label()
info_text.grid(column=0, row=1)
info_text.config(text="is equal to")

converted_num = tkinter.Label()
converted_num.grid(column=1, row=1)
converted_num.config(text="0")

km_units = tkinter.Label()
km_units.grid(column=2, row=1)
km_units.config(text="km")

# row 3

calculate_btn = tkinter.Button(command=button_clicked)
calculate_btn.grid(column=1, row=2)
calculate_btn.config(text="Calculcate")


window.mainloop()

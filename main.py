import tkinter

window = tkinter.Tk()
window.title("Unit Converter")
window.config(padx=20, pady=20)


# Miles to km
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    in_km.config(text=f"{km}")


# Text input
miles_input = tkinter.Entry(width=7)
miles_input.grid(row=0, column=1)

# Label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

in_km = tkinter.Label(text="0")
in_km.grid(row=1, column=1)

km_label = tkinter.Label(text="Kilometers")
km_label.grid(row=1, column=2)

# Button
calculate_btn = tkinter.Button(text="Convert", padx=10, pady=3, command=miles_to_km)
calculate_btn.grid(row=2, column=1)


window.mainloop()

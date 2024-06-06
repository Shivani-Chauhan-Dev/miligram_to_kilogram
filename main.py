from tkinter import *

def miligram_to_kg():
    miligram = eval(input_entry.get())
    kg = miligram*1/1000000
    kilogram_result_label.config(text = f"{kg}")




window = Tk()
window.title("Miligram to Kilogram")
window.config(padx = 30,pady = 60)

input_entry = Entry(width = 8)
input_entry.grid(column=1 ,row=0)


miligram_label = Label(text="Miligram")
miligram_label.grid(column=2 ,row=0)


is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0 ,row=1)


kilogram_result_label = Label(text ="0")
kilogram_result_label.grid(column=1 ,row=1)


kilogram_label = Label(text="Kg")
kilogram_label.grid(column=2 ,row=1)


calculate_button = Button(text="calculate",command =miligram_to_kg)
calculate_button.grid(column=1 ,row=2)


window.mainloop()























window.mainloop()
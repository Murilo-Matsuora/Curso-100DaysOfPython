from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

# Label
# my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# # my_label.pack(side="left")
# # my_label.place(x=100, y=200)
# my_label.grid(column=0, row=0)
# my_label.config(padx=15,pady=15)
#
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
#
#
# # Button
#
# def button_clicked():
#     print("I got clicked")
#     my_label.config(text="Button got clicked")
#     message = entry.get()
#     my_label.config(text=message)
#
#
# button = Button(text="Click Me", command=button_clicked)
# # button.pack()
# button.grid(column=1, row=1)
#
# button2 = Button(text="Click Me", command=button_clicked)
# button2.grid(column=2, row=0)
#
#
# # Entry
#
# entry = Entry(width=10)
# # entry.pack()
# entry.grid(column=3, row=2)

def convert_miles_to_km():
    converted_value = 1.60934 * float(entry.get())
    label3.config(text=str(converted_value))

entry = Entry(width=10)
entry.grid(row=0, column=1)

label1 = Label(text="miles")
label1.grid(row=0, column=2)
label2 = Label(text="is equal to")
label2.grid(row=1, column=0)
label3 = Label(text="0")
label3.grid(row=1, column=1)
label4 = Label(text="km")
label4.grid(row=1, column=2)

btn = Button(text="Calculate", command=convert_miles_to_km)
btn.grid(row=2, column=1)


window.mainloop()

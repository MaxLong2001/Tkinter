import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("200x200")

entry = tk.Entry(window, show="*")
entry.pack()


def insert_point():
    var = entry.get()
    text.insert("insert", var)


def insert_end():
    var = entry.get()
    text.insert("end", var)


buttonInsert = tk.Button(window, text="Insert", width=15, height=2, command=insert_point)
buttonInsert.pack()

buttonEnd = tk.Button(window, text="End", width=15, height=2, command=insert_end)
buttonEnd.pack()

text = tk.Text(window, height=2)
text.pack()

window.mainloop()

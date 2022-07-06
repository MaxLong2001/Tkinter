import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("500x300")

var1 = tk.StringVar()

label = tk.Label(window, bg="yellow", width=10, height=2, textvariable=var1)
label.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
listBox = tk.Listbox(window, listvariable=var2)

listItems = [1, 2, 3, 4]
for item in listItems:
    listBox.insert("end", item)

listBox.insert(1, "first")
listBox.insert(2, "second")
listBox.delete(2)
listBox.pack()


def print_selection():
    value = listBox.get(listBox.curselection())
    var1.set(value)


buttonPrint = tk.Button(window, text="print", width=15, height=2, command=print_selection)
buttonPrint.pack();

window.mainloop()

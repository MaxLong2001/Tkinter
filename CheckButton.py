import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("500x300")

label = tk.Label(window, bg="yellow", width=20, text="I love neither")
label.pack()


def print_selection():
    if var1.get() == 0 and var2.get() == 0:
        label.config(text="I love neither")
    elif var1.get() == 1 and var2.get() == 0:
        label.config(text="I love Python")
    elif var1.get() == 0 and var2.get() == 1:
        label.config(text="I love Java")
    else:
        label.config(text="I love both")


var1 = tk.IntVar()
var2 = tk.IntVar()
checkbutton1 = tk.Checkbutton(window, text="Python", variable=var1, onvalue=1, offvalue=0, command=print_selection)
checkbutton2 = tk.Checkbutton(window, text="Java", variable=var2, onvalue=1, offvalue=0, command=print_selection)
checkbutton1.pack()
checkbutton2.pack()

window.mainloop()

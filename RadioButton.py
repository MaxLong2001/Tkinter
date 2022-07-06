import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("500x300")

var = tk.StringVar()

label = tk.Label(window, bg="yellow", width=10, text="empty")
label.pack()


def print_selection():
    label.config(text=var.get())


radioButton1 = tk.Radiobutton(window, text="OptionA", variable=var, value="A", command=print_selection, )
radioButton1.pack()
radioButton2 = tk.Radiobutton(window, text="OptionB", variable=var, value="B", command=print_selection)
radioButton2.pack()
radioButton3 = tk.Radiobutton(window, text="OptionC", variable=var, value="C", command=print_selection)
radioButton3.pack()

window.mainloop()

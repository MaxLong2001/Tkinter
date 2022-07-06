import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("My Window")
window.geometry("500x300")


def hit_me():
    # tk.messagebox.showinfo(title="Hi", message="Hello World")
    # tk.messagebox.showwarning(title="Hi", message="Hello World")
    # tk.messagebox.showerror(title="Hi", message="Hello World")
    # print(tk.messagebox.askquestion(title="Hi", message="Hello World"))
    # print(tk.messagebox.askyesno(title="Hi", message="Hello World"))
    print(tk.messagebox.askretrycancel(title="Hi", message="Hello World"))


button = tk.Button(window, text="Hit Me", width=15, height=2, command=hit_me)
button.pack()

window.mainloop()

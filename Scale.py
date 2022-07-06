import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("500x300")

label = tk.Label(window, bg="yellow", width=20, text="empty")
label.pack()


def print_selection(v):
    label.config(text="you have selected: " + v)


scale = tk.Scale(window, label="try me", from_=1, to=10, orient=tk.HORIZONTAL, length=200, showvalue=True,
                 tickinterval=3, resolution=0.01, command=print_selection)
scale.pack()

window.mainloop()

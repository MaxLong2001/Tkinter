import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("500x300")

var = tk.StringVar()
on_hit = False
label = tk.Label(window, textvariable=var, bg="green", font=("Arial", 12), width=15, height=2)
label.pack()


def hit_me():
    global on_hit
    if on_hit:
        var.set("Don't hit me!")
        on_hit = False
    else:
        var.set("Hit me!")
        on_hit = True


button = tk.Button(window, text="Hit Me", width=15, height=2, command=hit_me)
button.pack()

window.mainloop()

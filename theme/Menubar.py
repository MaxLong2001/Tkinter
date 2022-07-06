import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("500x300")

label = tk.Label(window, bg="yellow", width=20, text="")
label.pack()

counter = 0


def do_job():
    global counter
    label.config(text="do" + str(counter))
    counter += 1


menubar = tk.Menu(window)
fileMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=do_job)
fileMenu.add_command(label="Open", command=do_job)
fileMenu.add_command(label="Save", command=do_job)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=window.quit)

subMenu = tk.Menu(fileMenu)
fileMenu.add_cascade(label="Import", menu=subMenu, underline=0)
subMenu.add_command(label="Sub1", command=do_job)

window.config(menu=menubar)

window.mainloop()

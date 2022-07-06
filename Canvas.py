import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("500x300")


def moveit():
    canvas.move(rectangle, 0, -2)


canvas = tk.Canvas(window, bg="blue", height=200, width=300)
img_file = tk.PhotoImage(file="screenshot.png")
img = canvas.create_image(0, 0, anchor="nw", image=img_file)
x0, y0, x1, y1 = 100, 100, 120, 120
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill="red")
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180, fill="red")
rectangle = canvas.create_rectangle(x0 + 50, y0 + 50, x1 + 50, y1 + 50, fill="red")
canvas.pack()
button = tk.Button(window, text="move", command=moveit)
button.pack()

window.mainloop()

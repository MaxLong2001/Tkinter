import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("500x300")

# tk.Label(window, text="1").pack(side="top")
# tk.Label(window, text="2").pack(side="bottom")
# tk.Label(window, text="3").pack(side="left")
# tk.Label(window, text="4").pack(side="right")

# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=str(i * j)).grid(row=i, column=j, padx=10, pady=10)

tk.Label(window, text="1").place(x=20, y=20, anchor="nw")

window.mainloop()
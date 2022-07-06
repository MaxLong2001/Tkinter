import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("500x300")

label = tk.Label(window, text="on the window")
label.pack()

frame = tk.Frame(window)
frame.pack()
frameLeft = tk.Frame(frame)
frameRight = tk.Frame(frame)
frameLeft.pack(side="left")
frameRight.pack(side="right")

labelFrame1 = tk.Label(frameLeft, text="on the FrameLeft1")
labelFrame2 = tk.Label(frameLeft, text="on the FrameLeft2")
labelFrame3 = tk.Label(frameRight, text="on the FrameRight")
labelFrame1.pack()
labelFrame2.pack()
labelFrame3.pack()

window.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

window = tk.Tk()
window.title("Demo")
window.geometry("1000x600")
window.resizable(False, False)

window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "light")

frameHead = ttk.Frame(window, height=80, relief="groove", borderwidth=1)
frameHead.pack(side="top", fill="x")

labelInfo = ttk.Label(frameHead, text="信息录入", font=("微软雅黑", 18, "bold"), foreground="#0099CC")
labelInfo.place(x=100, y=36, anchor="w")
labelResult = ttk.Label(frameHead, text="检测结果", font=("微软雅黑", 18, "bold"))
labelResult.place(x=500, y=36, anchor="center")
labelSuggestion = ttk.Label(frameHead, text="健康建议", font=("微软雅黑", 18, "bold"))
labelSuggestion.place(x=900, y=36, anchor="e")

labelFrameInfoTitle = ttk.Label(text="基本信息", font=("微软雅黑", 14))
labelFrameInfo = ttk.LabelFrame(window, labelwidget=labelFrameInfoTitle)
labelFrameInfo.place(x=500, y=100, width=600, height=360, anchor="n")

frameInfoHeight = ttk.Frame(labelFrameInfo, height=50)
frameInfoHeight.place(x=50, y=120, width=500, height=50, anchor="w")
labelHeight = ttk.Label(frameInfoHeight, text="身高(cm)：", font=("微软雅黑", 12))
labelHeight.place(x=0, y=20, anchor="w")
entryHeight = ttk.Entry(frameInfoHeight, width=50)
entryHeight.place(x=120, y=20, anchor="w")

frameInfoWeight = ttk.Frame(labelFrameInfo, height=50)
frameInfoWeight.place(x=50, y=180, width=500, height=50, anchor="w")
labelWeight = ttk.Label(frameInfoWeight, text="体重(kg)：", font=("微软雅黑", 12))
labelWeight.place(x=0, y=20, anchor="w")
entryWeight = ttk.Entry(frameInfoWeight, width=50)
entryWeight.place(x=120, y=20, anchor="w")

frameInfoLength = ttk.Frame(labelFrameInfo, height=50)
frameInfoLength.place(x=50, y=240, width=500, height=50, anchor="w")
labelLength = ttk.Label(frameInfoLength, text="腿长(cm)：", font=("微软雅黑", 12))
labelLength.place(x=0, y=20, anchor="w")
entryLength = ttk.Entry(frameInfoLength, width=50)
entryLength.place(x=120, y=20, anchor="w")

frameInfoCircum = ttk.Frame(labelFrameInfo, height=50)
frameInfoCircum.place(x=50, y=300, width=500, height=50, anchor="w")
labelCircum = ttk.Label(frameInfoCircum, text="膝盖腿围(cm)：", font=("微软雅黑", 12))
labelCircum.place(x=0, y=20, anchor="w")
entryCircum = ttk.Entry(frameInfoCircum, width=50)
entryCircum.place(x=120, y=20, anchor="w")






labelFrameResultTitle = ttk.Label(text="检测结果", font=("微软雅黑", 14))
labelFrameResult = ttk.LabelFrame(window, labelwidget=labelFrameResultTitle)
labelFrameResult.place(x=500, y=100, width=700, height=450, anchor="n")
labelFrameResult.place_forget()

# file = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
# print(file)

window.mainloop()

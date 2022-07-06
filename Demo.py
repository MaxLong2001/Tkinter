import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import re
from tkinter.ttk import Entry

defaultColor = "black"
theme = "light"


def import_data():
    fileName = filedialog.askopenfilename(filetypes=[("CSV文件", "*.csv")])
    entryData.insert(0, fileName)


name = ""
age = 0
male = True
height = 0
weight = 0
length = 0
circum = 0
fileName = ""


def commit_data():
    global name, age, male, height, weight, length, circum, fileName
    name = entryName.get()
    age = entryAge.get()
    male = isMale.get()
    height = entryHeight.get()
    weight = entryWeight.get()
    length = entryLength.get()
    circum = entryCircum.get()
    fileName = entryData.get()
    if name == "":
        messagebox.showerror(title="姓名错误", message="请输入姓名", parent=window)
        return
    if re.match("^\d+$", age) is None:
        messagebox.showerror(title="年龄错误", message="请输入正确的年龄", parent=window)
        return
    if re.match("^\d+$", height) is None:
        messagebox.showerror(title="身高错误", message="请输入正确的身高", parent=window)
        return
    if re.match("^\d+$", weight) is None:
        messagebox.showerror(title="体重错误", message="请输入正确的体重", parent=window)
        return
    if re.match("^\d+$", length) is None:
        messagebox.showerror(title="身高错误", message="请输入正确的身高", parent=window)
        return
    if re.match("^\d+$", circum) is None:
        messagebox.showerror(title="腿围错误", message="请输入正确的腿围", parent=window)
        return
    if fileName == "":
        messagebox.showerror(title="数据错误", message="请选择数据文件", parent=window)
        return
    labelFrameInfo.place_forget()
    frameData.place_forget()
    buttonCommit.place_forget()
    labelInfo.config(foreground="#99CC66")
    labelResult.config(foreground="#0099CC")
    labelSuggestion.config(foreground=defaultColor)
    labelFrameResult1.place(x=630, y=100, width=680, height=400, anchor="n")
    labelFrameResult2.place(x=150, y=100, width=200, height=400, anchor="n")
    buttonCheckSuggestion.place(x=420, y=530, width=120, height=40, anchor="n")
    buttonReturnInfo.place(x=580, y=530, width=120, height=40, anchor="n")
    init_result_info()


def init_result_info():
    global name, age, male, height, weight, length, circum
    labelResultName.config(text="姓名：" + name)
    labelResultName.place(x=10, y=25)
    labelResultAge.config(text="年龄：" + str(age))
    labelResultAge.place(x=10, y=75)
    labelResultGender.config(text="性别：" + "男" if male else "性别：" + "女")
    labelResultGender.place(x=10, y=125)
    labelResultHeight.config(text="身高(cm)：" + str(height))
    labelResultHeight.place(x=10, y=175)
    labelResultWeight.config(text="体重(kg)：" + str(weight))
    labelResultWeight.place(x=10, y=225)
    labelResultLength.config(text="大腿长(cm)：" + str(length))
    labelResultLength.place(x=10, y=275)
    labelResultCircum.config(text="膝盖腿围(cm)：" + str(circum))
    labelResultCircum.place(x=10, y=325)


def check_suggestion():
    labelInfo.config(foreground="#99CC66")
    labelResult.config(foreground="#99CC66")
    labelSuggestion.config(foreground="#0099CC")
    labelFrameResult1.place_forget()
    buttonCheckSuggestion.place_forget()
    buttonReturnInfo.place_forget()
    buttonReturnInfo.place(x=500, y=530, width=120, height=40, anchor="n")
    labelFrameSuggestion.place(x=630, y=150, width=680, height=350, anchor="n")
    labelStatus.config(background="#99CC66")
    labelStatus.config(text="         健康")
    labelStatus.place(x=630, y=100, width=150, height=50, anchor="n")


def return_info():
    labelInfo.config(foreground="#0099CC")
    labelResult.config(foreground=defaultColor)
    labelSuggestion.config(foreground=defaultColor)
    labelFrameResult1.place_forget()
    labelFrameResult2.place_forget()
    buttonCheckSuggestion.place_forget()
    buttonReturnInfo.place_forget()
    labelFrameSuggestion.place_forget()
    labelStatus.place_forget()
    entryName.delete(0, tk.END)
    entryName.insert(0, name)
    entryAge.delete(0, tk.END)
    entryAge.insert(0, str(age))
    isMale.set(male)
    entryHeight.delete(0, tk.END)
    entryHeight.insert(0, str(height))
    entryWeight.delete(0, tk.END)
    entryWeight.insert(0, str(weight))
    entryLength.delete(0, tk.END)
    entryLength.insert(0, str(length))
    entryCircum.delete(0, tk.END)
    entryCircum.insert(0, str(circum))
    labelFrameInfo.place(x=500, y=90, width=600, height=360, anchor="n")
    frameData.place(x=500, y=470, width=480, height=50, anchor="n")
    buttonCommit.place(x=500, y=530, width=100, height=40, anchor="n")


window = tk.Tk()
window.title("Demo")
window.geometry("1000x600")
window.resizable(False, False)

window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", theme)

frameHead = ttk.Frame(window, height=70, relief="groove", borderwidth=1)
frameHead.pack(side="top", fill="x")

labelInfo = ttk.Label(frameHead, text="信息录入", font=("微软雅黑", 18, "bold"), foreground="#0099CC")
labelInfo.place(x=100, y=30, anchor="w")
labelResult = ttk.Label(frameHead, text="检测结果", font=("微软雅黑", 18, "bold"))
labelResult.place(x=500, y=30, anchor="center")
labelSuggestion = ttk.Label(frameHead, text="健康建议", font=("微软雅黑", 18, "bold"))
labelSuggestion.place(x=900, y=30, anchor="e")

"""基本信息"""
labelFrameInfoTitle = ttk.Label(text="基本信息", font=("微软雅黑", 14))
labelFrameInfo = ttk.LabelFrame(window, labelwidget=labelFrameInfoTitle)
labelFrameInfo.place(x=500, y=90, width=600, height=360, anchor="n")

frameInfoBasic = ttk.Frame(labelFrameInfo, height=50)
frameInfoBasic.place(x=50, y=60, width=500, height=50, anchor="w")

labelName = ttk.Label(frameInfoBasic, text="姓名", font=("微软雅黑", 12))
labelName.place(x=0, y=20, anchor="w")
entryName = ttk.Entry(frameInfoBasic, width=10)
entryName.place(x=40, y=20, anchor="w")

labelAge = ttk.Label(frameInfoBasic, text="年龄", font=("微软雅黑", 12))
labelAge.place(x=160, y=20, anchor="w")
entryAge = ttk.Entry(frameInfoBasic, width=10)
entryAge.place(x=200, y=20, anchor="w")

isMale = tk.BooleanVar()
isMale.set(True)
labelGender = ttk.Label(frameInfoBasic, text="性别", font=("微软雅黑", 12))
labelGender.place(x=320, y=20, anchor="w")
radioButtonMale = ttk.Radiobutton(frameInfoBasic, text="男", variable=isMale, value=True)
radioButtonMale.place(x=360, y=20, anchor="w")
radioButtonFemale = ttk.Radiobutton(frameInfoBasic, text="女", variable=isMale, value=False)
radioButtonFemale.place(x=410, y=20, anchor="w")

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
labelLength = ttk.Label(frameInfoLength, text="大腿长度(cm)：", font=("微软雅黑", 12))
labelLength.place(x=0, y=20, anchor="w")
entryLength = ttk.Entry(frameInfoLength, width=50)
entryLength.place(x=120, y=20, anchor="w")

frameInfoCircum = ttk.Frame(labelFrameInfo, height=50)
frameInfoCircum.place(x=50, y=300, width=500, height=50, anchor="w")
labelCircum = ttk.Label(frameInfoCircum, text="膝盖腿围(cm)：", font=("微软雅黑", 12))
labelCircum.place(x=0, y=20, anchor="w")
entryCircum = ttk.Entry(frameInfoCircum, width=50)
entryCircum.place(x=120, y=20, anchor="w")

frameData = ttk.Frame(window, height=50)
frameData.place(x=500, y=470, width=480, height=50, anchor="n")
entryData: Entry = ttk.Entry(frameData, width=50)
entryData.place(x=0, y=20, anchor="w")

buttonData = ttk.Button(frameData, text="导入数据", command=import_data)
buttonData.place(x=480, y=20, width=100, height=40, anchor="e")

buttonCommit = ttk.Button(window, text="确定", command=commit_data)
buttonCommit.place(x=500, y=530, width=100, height=40, anchor="n")

"""检测结果"""
labelFrameResultTitle1 = ttk.Label(text="检测结果", font=("微软雅黑", 14))
labelFrameResult1 = ttk.LabelFrame(window, labelwidget=labelFrameResultTitle1)

labelFrameResultTitle2 = ttk.Label(text="基本信息", font=("微软雅黑", 14))
labelFrameResult2 = ttk.LabelFrame(window, labelwidget=labelFrameResultTitle2)

labelResultName = ttk.Label(labelFrameResult2, font=("微软雅黑", 12))
labelResultAge = ttk.Label(labelFrameResult2, font=("微软雅黑", 12))
labelResultGender = ttk.Label(labelFrameResult2, font=("微软雅黑", 12))
labelResultHeight = ttk.Label(labelFrameResult2, font=("微软雅黑", 12))
labelResultWeight = ttk.Label(labelFrameResult2, font=("微软雅黑", 12))
labelResultLength = ttk.Label(labelFrameResult2, font=("微软雅黑", 12))
labelResultCircum = ttk.Label(labelFrameResult2, font=("微软雅黑", 12))

buttonCheckSuggestion = ttk.Button(window, text="查看健康建议", command=check_suggestion)

buttonReturnInfo = ttk.Button(window, text="编辑基本信息", command=return_info)

"""健康建议"""
labelFrameSuggestionTitle = ttk.Label(text="健康建议", font=("微软雅黑", 14))
labelFrameSuggestion = ttk.LabelFrame(window, labelwidget=labelFrameSuggestionTitle)

labelStatus = ttk.Label(window, font=("微软雅黑", 16))

window.mainloop()

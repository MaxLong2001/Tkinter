import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Entry
from PIL import ImageTk
import re

defaultColor = "black"
theme = "light"
windowNo = 1
columns = ("姓名", "年龄", "性别", "身高(cm)", "体重(kg)", "大腿长度(cm)", "膝盖腿围(cm)", "健康状况")
positiveSuggestionText = "您的膝关节可能已经受到损伤如果您的膝盖近期没有受到突发碰撞，" + \
                         "这可能是由于长期劳损或骨质疏松造成的慢性退变性撕裂，建议您依据实际情况去骨科或关节外科就医；" + \
                         "如果您的膝盖近期受到过突发碰撞或者您是四十岁以下热爱运动的人群，损伤类型通常为急性创伤性损伤，" + \
                         "建议您优先考虑运动医学科。请遵循医嘱，选择保守治疗或手术治疗，近期应当注意休息和饮食，" + \
                         "适当补充维生素和高蛋白、钙元素丰富的食物，适度活动（如散步），并做好病情监控。 "
negativeSuggestionText = "您的膝关节健康状况良好给您提供一些预防膝关节损伤的建议。" + \
                         "进行有益于膝关节健康的运动（如骑自行车、游泳），避免膝关节剧烈运动，必要时请佩戴好护膝；" + \
                         "注意饮食，补充维生素，高蛋白以及含钙丰富的食物，避免暴饮暴食，控制体重；爬楼梯时速度不宜过快，一步一阶。"


def import_data():
    fileName = filedialog.askopenfilename(filetypes=[("CSV文件", "*.csv")])
    entryData.config(state="normal")
    entryData.delete(0, tk.END)
    entryData.insert(0, fileName)
    entryData.config(state="readonly")


name = ""
age = 0
male = True
height = 0
weight = 0
length = 0
circum = 0
fileName = ""
health = True


def commit_data():
    global name, age, male, height, weight, length, circum, fileName, windowNo
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
    labelHistory.config(foreground=defaultColor)
    labelFrameResult1.place(x=630, y=100, width=680, height=400, anchor="n")
    labelFrameResult2.place(x=150, y=100, width=200, height=400, anchor="n")
    buttonCheckSuggestion.place(x=420, y=530, width=120, height=40, anchor="n")
    buttonReturnInfo.place(x=580, y=530, width=120, height=40, anchor="n")
    buttonHistory.place(x=260, y=530, width=120, height=40, anchor="n")
    windowNo = 2
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
    global windowNo
    labelInfo.config(foreground="#99CC66")
    labelResult.config(foreground="#99CC66")
    labelSuggestion.config(foreground="#0099CC")
    labelHistory.config(foreground=defaultColor)
    labelFrameResult1.place_forget()
    buttonCheckSuggestion.place_forget()
    buttonReturnInfo.place_forget()
    labelFrameHistory.place_forget()
    buttonReturnInfo.place(x=500, y=530, width=120, height=40, anchor="n")
    labelFrameSuggestion.place(x=630, y=150, width=680, height=350, anchor="n")
    buttonHistory.place(x=260, y=530, width=120, height=40, anchor="n")
    if health:
        textSuggestion.config(state="normal")
        textSuggestion.delete(1.0, "end")
        textSuggestion.insert(1.0, positiveSuggestionText)
        textSuggestion.config(state="disabled")
    else:
        textSuggestion.config(state="normal")
        textSuggestion.delete(1.0, "end")
        textSuggestion.insert(1.0, negativeSuggestionText)
        textSuggestion.config(state="disabled")
    labelStatus.config(background="#99CC66")
    labelStatus.config(text="         健康")
    labelStatus.place(x=630, y=100, width=150, height=50, anchor="n")
    windowNo = 3
    write_history_data()


def return_info():
    global windowNo
    labelInfo.config(foreground="#0099CC")
    labelResult.config(foreground=defaultColor)
    labelSuggestion.config(foreground=defaultColor)
    labelHistory.config(foreground=defaultColor)
    labelFrameResult1.place_forget()
    labelFrameResult2.place_forget()
    buttonCheckSuggestion.place_forget()
    buttonReturnInfo.place_forget()
    labelFrameSuggestion.place_forget()
    labelStatus.place_forget()
    labelFrameHistory.place_forget()
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
    buttonHistory.place(x=260, y=530, width=120, height=40, anchor="n")
    windowNo = 1


def write_history_data():
    global name, age, male, height, weight, length, circum
    f = open(".\data\history.txt", "a")
    f.write(name + " " + str(age) + " " + ("男" if male else "女") + " " + str(height) + " " + str(weight) + " " + str(
        length) + " " + str(circum) + " " + str(health) + "\n")
    f.close()


def read_history_data():
    labelInfo.config(foreground=defaultColor)
    labelResult.config(foreground=defaultColor)
    labelSuggestion.config(foreground=defaultColor)
    labelHistory.config(foreground="#0099CC")
    labelFrameInfo.place_forget()
    frameData.place_forget()
    buttonCommit.place_forget()
    labelFrameResult1.place_forget()
    labelFrameResult2.place_forget()
    buttonCheckSuggestion.place_forget()
    buttonReturnInfo.place_forget()
    labelFrameSuggestion.place_forget()
    labelStatus.place_forget()
    buttonHistory.place_forget()
    labelFrameHistory.place(x=500, y=90, width=860, height=400, anchor="n")
    buttonReturn.place(x=500, y=530, width=100, height=40, anchor="n")
    treeHistory.delete(*treeHistory.get_children())
    f = open(".\data\history.txt", "r")
    line = f.readline()
    while line:
        dataList = line.split(" ")
        treeHistory.insert("", "end", values=(
            dataList[0], dataList[1], dataList[2], dataList[3], dataList[4], dataList[5], dataList[6],
            "健康" if dataList[7].replace("\n", "") == "True" else "不健康"))
        line = f.readline()
    f.close()


def return_from_history():
    global windowNo
    if windowNo == 1:
        labelFrameHistory.place_forget()
        buttonReturn.place_forget()
        labelFrameInfo.place(x=500, y=90, width=600, height=360, anchor="n")
        frameData.place(x=500, y=470, width=480, height=50, anchor="n")
        buttonCommit.place(x=500, y=530, width=100, height=40, anchor="n")
        buttonHistory.place(x=260, y=530, width=120, height=40, anchor="n")
    elif windowNo == 2:
        labelFrameHistory.place_forget()
        buttonReturn.place_forget()
        labelFrameResult1.place(x=630, y=100, width=680, height=400, anchor="n")
        labelFrameResult2.place(x=150, y=100, width=200, height=400, anchor="n")
        buttonCheckSuggestion.place(x=420, y=530, width=120, height=40, anchor="n")
        buttonReturnInfo.place(x=580, y=530, width=120, height=40, anchor="n")
        buttonHistory.place(x=260, y=530, width=120, height=40, anchor="n")
    elif windowNo == 3:
        labelFrameHistory.place_forget()
        buttonReturn.place_forget()
        labelFrameResult2.place(x=150, y=100, width=200, height=400, anchor="n")
        buttonReturnInfo.place(x=500, y=530, width=120, height=40, anchor="n")
        labelFrameSuggestion.place(x=630, y=150, width=680, height=350, anchor="n")
        buttonHistory.place(x=260, y=530, width=120, height=40, anchor="n")
        labelStatus.place(x=630, y=100, width=150, height=50, anchor="n")


window = tk.Tk()
window.title("膝关节安全评估")
window.geometry("1000x600")
window.resizable(False, False)

window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", theme)

frameHead = ttk.Frame(window, height=70, relief="groove", borderwidth=1)
frameHead.pack(side="top", fill="x")

labelInfo = ttk.Label(frameHead, text="信息录入", font=("微软雅黑", 18, "bold"), foreground="#0099CC")
labelInfo.place(x=125, y=16, anchor="n")
labelResult = ttk.Label(frameHead, text="检测结果", font=("微软雅黑", 18, "bold"))
labelResult.place(x=375, y=16, anchor="n")
labelSuggestion = ttk.Label(frameHead, text="健康建议", font=("微软雅黑", 18, "bold"))
labelSuggestion.place(x=625, y=16, anchor="n")
labelHistory = ttk.Label(frameHead, text="历史记录", font=("微软雅黑", 18, "bold"))
labelHistory.place(x=875, y=16, anchor="n")

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
entryData: Entry = ttk.Entry(frameData, width=50, state="readonly")
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

figureFile = ImageTk.PhotoImage(file="figure.png")
labelFigure = tk.Label(labelFrameResult1, image=figureFile, width=660, height=280)
labelFigure.place(x=340, y=180, anchor="center")

buttonCheckSuggestion = ttk.Button(window, text="查看健康建议", command=check_suggestion)

buttonReturnInfo = ttk.Button(window, text="编辑基本信息", command=return_info)

"""健康建议"""
labelFrameSuggestionTitle = ttk.Label(text="健康建议", font=("微软雅黑", 14))
labelFrameSuggestion = ttk.LabelFrame(window, labelwidget=labelFrameSuggestionTitle)

textSuggestion = tk.Text(labelFrameSuggestion, width=65, height=14, wrap="word", font=("楷体", 15))
textSuggestion.place(x=340, y=155, anchor="center")

labelStatus = ttk.Label(window, font=("微软雅黑", 16))

"""历史记录"""
labelFrameHistoryTitle = ttk.Label(text="历史记录", font=("微软雅黑", 14))
labelFrameHistory = ttk.LabelFrame(window, labelwidget=labelFrameHistoryTitle)

scrollBar = ttk.Scrollbar(labelFrameHistory)
scrollBar.pack(side="right", fill="y")

treeHistory = ttk.Treeview(labelFrameHistory, columns=columns, show="headings", height=14, yscrollcommand=scrollBar.set)
for i in range(len(columns)):
    treeHistory.column(columns[i], width=100, anchor="center")
    treeHistory.heading(columns[i], text=columns[i])
treeHistory.place(x=0, y=0, anchor="nw")

treeHistoryStyle = ttk.Style()
treeHistoryStyle.configure("Treeview.Heading", font=("微软雅黑", 12))

buttonHistory = ttk.Button(window, text="查看历史记录", command=read_history_data)
buttonHistory.place(x=260, y=530, width=120, height=40, anchor="n")

buttonReturn = ttk.Button(window, text="返回", command=return_from_history)

window.mainloop()

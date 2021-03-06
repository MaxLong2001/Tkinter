# coding: utf-8

import time
import tkinter as tk
from threading import Thread
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Entry
import re
import matlab
import matlab.engine
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.font_manager import FontProperties
import numpy as np
import pandas as pd
from PIL import Image, ImageTk, ImageSequence

defaultColor = "black"
theme = "light"
windowNo = 1
columns = ("序号", "姓名", "年龄", "性别", "身高(cm)", "体重(kg)", "大腿长度(cm)", "膝盖腿围(cm)", "健康状况")
negativeSuggestionText = "健康建议：\n\n     您的膝关节可能已经受到损伤如果您的膝盖近期没有受到突发碰撞，" + \
                         "这可能是由于长期劳损或骨质疏松造成的慢性退变性撕裂，建议您依据实际情况去骨科或关节外科就医。\n\n" + \
                         "     如果您的膝盖近期受到过突发碰撞或者您是四十岁以下热爱运动的人群，损伤类型通常为急性创伤性损伤，" + \
                         "建议您优先考虑运动医学科。\n\n     请遵循医嘱，选择保守治疗或手术治疗，近期应当注意休息和饮食，" + \
                         "适当补充维生素和高蛋白、钙元素丰富的食物，适度活动（如散步），并做好病情监控。 "
positiveSuggestionText = "健康建议：\n\n     您的膝关节健康状况良好，给您提供一些预防膝关节损伤的建议：\n\n" + \
                         "     进行有益于膝关节健康的运动（如骑自行车、游泳），避免膝关节剧烈运动，必要时请佩戴好护膝。\n\n" + \
                         "     注意饮食，补充维生素，高蛋白以及含钙丰富的食物，避免暴饮暴食，控制体重；爬楼梯时速度不宜过快，一步一阶。"
subHealthSuggestionText = "健康建议：\n\n     您的膝关节可能已经受到损伤如果您的膝盖近期没有受到突发碰撞"


def import_data():
    global health, directoryName
    directoryName = filedialog.askdirectory()
    entryData.config(state="normal")
    entryData.delete(0, tk.END)
    entryData.insert(0, directoryName)
    entryData.config(state="readonly")

    try:
        infoFile = open(directoryName + "/info.txt", "r", encoding="utf-8")
        entryName.delete(0, tk.END)
        entryName.insert(0, infoFile.readline().strip("\n"))
        entryAge.delete(0, tk.END)
        entryAge.insert(0, infoFile.readline().strip("\n"))
        if infoFile.readline().strip("\n") == "男":
            isMale.set(True)
        else:
            isMale.set(False)
        entryHeight.delete(0, tk.END)
        entryHeight.insert(0, infoFile.readline().strip("\n"))
        entryWeight.delete(0, tk.END)
        entryWeight.insert(0, infoFile.readline().strip("\n"))
        entryLength.delete(0, tk.END)
        entryLength.insert(0, infoFile.readline().strip("\n"))
        entryCircum.delete(0, tk.END)
        entryCircum.insert(0, infoFile.readline().strip("\n"))
        entryExperience.delete(0, tk.END)
        entryExperience.insert(0, infoFile.readline().strip("\n"))
        infoFile.close()
    except FileNotFoundError:
        pass


name = ""
age = 0
male = True
height = 0
weight = 0
length = 0
circum = 0
experience = ""
directoryName = ""
health = 0
newMatrix = []


def get_result():
    buttonCheckSuggestion.config(state="disabled")
    buttonReturnInfo.config(state="disabled")
    labelResultData1.config(text="")
    labelResultData2.config(text="")
    labelResultData3.config(text="")
    frameResultFigure.place_forget()
    frameResultLoading.place(x=380, y=170, width=300, height=100, anchor="center")

    threadCommitData = Thread(target=commit_data)
    threadCommitData.setDaemon(True)
    threadMatlabResult = Thread(target=run_matlab_result)
    threadMatlabResult.setDaemon(True)
    threadLoadingResult = Thread(target=display_loading_result_gif)
    threadLoadingResult.setDaemon(True)
    threadCommitData.start()
    threadMatlabResult.start()
    threadLoadingResult.start()


def get_suggestion():
    buttonReturnInfo.config(state="disabled")
    textSuggestion.place_forget()
    labelStatus.place_forget()
    frameSuggestionLoading.place(x=350, y=170, width=300, height=100, anchor="center")

    threadCheckSuggestion = Thread(target=check_suggestion)
    threadCheckSuggestion.setDaemon(True)
    threadMatlabSuggestion = Thread(target=run_matlab_suggestion)
    threadMatlabSuggestion.setDaemon(True)
    threadLoadingSuggestion = Thread(target=display_loading_suggestion_gif)
    threadLoadingSuggestion.setDaemon(True)
    threadCheckSuggestion.start()
    threadMatlabSuggestion.start()
    threadLoadingSuggestion.start()


def run_matlab_result():
    global newMatrix, directoryName
    eng = matlab.engine.start_matlab()
    ans = eng.knee_function(directoryName, nargout=7)
    eng.quit()

    labelResultData1.config(text="平均变点数：" + str(format(ans[0], ".3f")))
    labelResultData2.config(text="周期：" + str(format(ans[1] / 1000000 * 4, ".3f")) + "s")
    labelResultData3.config(text="自相关系数：" + str(format(ans[2], ".3f")))

    basicData = np.zeros((len(ans[4]), 4))
    basicData[:, 0] = height
    basicData[:, 1] = weight
    basicData[:, 2] = circum
    basicData[:, 3] = length
    newMatrix = np.hstack((basicData, ans[4], ans[6], ans[5]))
    print(basicData)
    print(newMatrix)

    fig = plt.Figure(figsize=(6.6, 2.9), dpi=100)
    canvasFigure = FigureCanvasTkAgg(fig, master=frameResultFigure)
    canvasFigure.get_tk_widget().place(x=330, y=145, width=660, height=290, anchor="center")
    labelFigureXLabel = tk.Label(frameResultFigure, text="时间(s)", font=("微软雅黑", 12))
    labelFigureXLabel.place(x=340, y=290, width=100, height=20, anchor="n")

    points = np.array(ans[3][0])
    t = np.array(np.linspace(0, 4, len(points)))
    tmp = fig.add_subplot(111)
    tmp.plot(t, points)
    tmp.set_ylabel("信号强度", fontproperties=FontProperties(fname="msyh.ttc", size=12))

    frameResultLoading.place_forget()
    frameResultFigure.place(x=340, y=0, width=660, height=310, anchor="n")
    buttonCheckSuggestion.config(state="normal")
    buttonReturnInfo.config(state="normal")


def run_matlab_suggestion():
    global newMatrix, health
    dataSheet = pd.read_excel("./data/data_collection.xlsx", sheet_name="Sheet8")
    dataArray = np.array(dataSheet)
    dataList = dataArray.tolist()
    matlabDataList = matlab.double(dataList)
    matlabNewMatrix = matlab.double(newMatrix.tolist())
    print(matlabDataList)
    print(matlabNewMatrix)

    eng = matlab.engine.start_matlab()
    ans = eng.classify(matlabDataList, matlabNewMatrix, 20, nargout=1)
    eng.quit()
    print(ans)

    healthIndex = 0
    for element in range(len(ans)):
        healthIndex += sum(ans[element])
    healthIndex = healthIndex / len(ans) / len(ans[0])
    print(healthIndex)

    if healthIndex < 1 / 3:
        health = 0
        textSuggestion.config(state="normal")
        textSuggestion.delete(1.0, "end")
        textSuggestion.insert(1.0, positiveSuggestionText)
        textSuggestion.config(state="disabled")
        labelStatus.config(background="#99CC66")
        labelStatus.config(text="         健康状态良好")
    elif healthIndex < 1 / 2:
        health = 1
        textSuggestion.config(state="normal")
        textSuggestion.delete(1.0, "end")
        textSuggestion.insert(1.0, subHealthSuggestionText)
        textSuggestion.config(state="disabled")
        labelStatus.config(background="#FFCC00")
        labelStatus.config(text="         存在健康隐患")
    else:
        health = 2
        textSuggestion.config(state="normal")
        textSuggestion.delete(1.0, "end")
        textSuggestion.insert(1.0, negativeSuggestionText)
        textSuggestion.config(state="disabled")
        labelStatus.config(background="#FF0033")
        labelStatus.config(text="      建议进行专业诊断")

    textSuggestion.place(x=340, y=200, width=660, height=300, anchor="center")
    labelStatus.place(x=340, y=16, width=240, height=40, anchor="center")
    buttonReturnInfo.config(state="normal")


def commit_data():
    global name, age, male, height, weight, length, circum, experience, fileName, windowNo
    name = entryName.get()
    age = entryAge.get()
    male = isMale.get()
    height = entryHeight.get()
    weight = entryWeight.get()
    length = entryLength.get()
    circum = entryCircum.get()
    fileName = entryData.get()
    experience = entryExperience.get()
    if name == "":
        messagebox.showerror(title="姓名错误", message="请输入姓名", parent=window)
        return
    if re.match("^\d+$", age) is None:
        messagebox.showerror(title="年龄错误", message="请输入正确的年龄", parent=window)
        return
    if re.match("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$", height) is None and re.match("^[1-9]\d*$", height) is None:
        messagebox.showerror(title="身高错误", message="请输入正确的身高", parent=window)
        return
    if re.match("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$", weight) is None and re.match("^[1-9]\d*$", weight) is None:
        messagebox.showerror(title="体重错误", message="请输入正确的体重", parent=window)
        return
    if re.match("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$", length) is None and re.match("^[1-9]\d*$", length) is None:
        messagebox.showerror(title="腿长错误", message="请输入正确的腿长", parent=window)
        return
    if re.match("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$", circum) is None and re.match("^[1-9]\d*$", circum) is None:
        messagebox.showerror(title="腿围错误", message="请输入正确的腿围", parent=window)
        return
    if experience == "":
        messagebox.showerror(title="损伤经历错误", message="请输入损伤经历，若无损伤经历请填“无”", parent=window)
        return
    if fileName == "":
        messagebox.showerror(title="数据错误", message="请选择数据文件", parent=window)
        return
    labelFrameInfo.place_forget()
    frameData.place_forget()
    buttonCommit.place_forget()
    labelInfo.config(foreground="#CCCCCC")
    labelResult.config(foreground="#0099CC")
    labelSuggestion.config(foreground=defaultColor)
    labelHistory.config(foreground=defaultColor)
    labelFrameResult.place(x=630, y=100, width=680, height=400, anchor="n")
    labelFrameResultBasic.place(x=150, y=100, width=200, height=400, anchor="n")
    buttonCheckSuggestion.place(x=500, y=530, width=120, height=40, anchor="n")
    buttonReturnInfo.place(x=640, y=530, width=120, height=40, anchor="n")
    buttonHistory.place(x=360, y=530, width=120, height=40, anchor="n")
    windowNo = 2
    init_result_info()


def init_result_info():
    global name, age, male, height, weight, length, circum
    labelResultName.config(text="姓名：" + name)
    labelResultName.place(x=10, y=0)
    labelResultAge.config(text="年龄：" + str(age))
    labelResultAge.place(x=10, y=30)
    labelResultGender.config(text="性别：" + "男" if male else "性别：" + "女")
    labelResultGender.place(x=10, y=60)
    labelResultHeight.config(text="身高(cm)：" + str(height))
    labelResultHeight.place(x=10, y=90)
    labelResultWeight.config(text="体重(kg)：" + str(weight))
    labelResultWeight.place(x=10, y=120)
    labelResultLength.config(text="大腿长(cm)：" + str(length))
    labelResultLength.place(x=10, y=150)
    labelResultCircum.config(text="膝盖腿围(cm)：" + str(circum))
    labelResultCircum.place(x=10, y=180)
    labelResultExperience.config(text="损伤经历：" + experience)
    labelResultExperience.place(x=10, y=210)


def check_suggestion():
    global windowNo
    labelInfo.config(foreground="#CCCCCC")
    labelResult.config(foreground="#CCCCCC")
    labelSuggestion.config(foreground="#0099CC")
    labelHistory.config(foreground=defaultColor)

    labelFrameResult.place_forget()
    buttonCheckSuggestion.place_forget()
    buttonReturnInfo.place_forget()
    labelFrameHistory.place_forget()

    buttonReturnInfo.place(x=570, y=530, width=120, height=40, anchor="n")
    labelFrameSuggestion.place(x=630, y=100, width=680, height=400, anchor="n")
    buttonHistory.place(x=430, y=530, width=120, height=40, anchor="n")

    windowNo = 3
    write_history_data()


def return_info():
    global windowNo
    labelInfo.config(foreground="#0099CC")
    labelResult.config(foreground=defaultColor)
    labelSuggestion.config(foreground=defaultColor)
    labelHistory.config(foreground=defaultColor)

    labelFrameResult.place_forget()
    labelFrameResultBasic.place_forget()
    buttonCheckSuggestion.place_forget()
    buttonReturnInfo.place_forget()
    labelFrameSuggestion.place_forget()
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
    frameData.place(x=500, y=470, width=600, height=50, anchor="n")
    buttonCommit.place(x=570, y=530, width=120, height=40, anchor="n")
    buttonHistory.place(x=430, y=530, width=120, height=40, anchor="n")
    windowNo = 1


def write_history_data():
    global name, age, male, height, weight, length, circum
    f = open("./data/history.txt", "a", encoding="utf-8")
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
    labelFrameResult.place_forget()
    labelFrameResultBasic.place_forget()
    buttonCheckSuggestion.place_forget()
    buttonReturnInfo.place_forget()
    labelFrameSuggestion.place_forget()
    buttonHistory.place_forget()

    labelFrameHistory.place(x=500, y=90, width=910, height=400, anchor="n")
    buttonRefresh.place(x=290, y=530, width=120, height=40, anchor="n")
    buttonReturn.place(x=430, y=530, width=120, height=40, anchor="n")
    buttonClear.place(x=570, y=530, width=120, height=40, anchor="n")
    buttonDelete.place(x=710, y=530, width=120, height=40, anchor="n")

    treeHistory.delete(*treeHistory.get_children())
    f = open("./data/history.txt", "r", encoding="utf-8")
    line = f.readline()
    lineCount = 0
    while line:
        lineCount += 1
        dataList = line.split(" ")
        status = ""
        if dataList[7].strip("\n") == "0":
            status = "健康"
        elif dataList[7].strip("\n") == "1":
            status = "亚健康"
        elif dataList[7].strip("\n") == "2":
            status = "不健康"
        treeHistory.insert("", "end", values=(lineCount,
                                              dataList[0], dataList[1], dataList[2], dataList[3], dataList[4],
                                              dataList[5], dataList[6], status))
        line = f.readline()
    f.close()


def return_from_history():
    global windowNo
    if windowNo == 1:
        labelInfo.config(foreground="#0099CC")
        labelResult.config(foreground=defaultColor)
        labelSuggestion.config(foreground=defaultColor)
        labelHistory.config(foreground=defaultColor)

        labelFrameHistory.place_forget()
        buttonRefresh.place_forget()
        buttonReturn.place_forget()
        buttonClear.place_forget()
        buttonDelete.place_forget()

        labelFrameInfo.place(x=500, y=90, width=600, height=360, anchor="n")
        frameData.place(x=500, y=470, width=600, height=50, anchor="n")
        buttonCommit.place(x=570, y=530, width=120, height=40, anchor="n")
        buttonHistory.place(x=430, y=530, width=120, height=40, anchor="n")
    elif windowNo == 2:
        labelInfo.config(foreground="#CCCCCC")
        labelResult.config(foreground="#0099CC")
        labelSuggestion.config(foreground=defaultColor)
        labelHistory.config(foreground=defaultColor)

        labelFrameHistory.place_forget()
        buttonRefresh.place_forget()
        buttonReturn.place_forget()
        buttonClear.place_forget()
        buttonDelete.place_forget()

        labelFrameResult.place(x=630, y=100, width=680, height=400, anchor="n")
        labelFrameResultBasic.place(x=150, y=100, width=200, height=400, anchor="n")
        buttonCheckSuggestion.place(x=500, y=530, width=120, height=40, anchor="n")
        buttonReturnInfo.place(x=640, y=530, width=120, height=40, anchor="n")
        buttonHistory.place(x=360, y=530, width=120, height=40, anchor="n")
    elif windowNo == 3:
        labelInfo.config(foreground="#CCCCCC")
        labelResult.config(foreground="#CCCCCC")
        labelSuggestion.config(foreground="#0099CC")
        labelHistory.config(foreground=defaultColor)

        labelFrameHistory.place_forget()
        buttonRefresh.place_forget()
        buttonReturn.place_forget()
        buttonClear.place_forget()
        buttonDelete.place_forget()

        labelFrameResultBasic.place(x=150, y=100, width=200, height=400, anchor="n")
        buttonReturnInfo.place(x=570, y=530, width=120, height=40, anchor="n")
        labelFrameSuggestion.place(x=630, y=100, width=680, height=400, anchor="n")
        buttonHistory.place(x=430, y=530, width=120, height=40, anchor="n")


def refresh_history_data():
    treeHistory.delete(*treeHistory.get_children())
    f = open("./data/history.txt", "r", encoding="utf-8")
    line = f.readline()
    lineCount = 0
    while line:
        lineCount += 1
        dataList = line.split(" ")
        treeHistory.insert("", "end", values=(lineCount,
                                              dataList[0], dataList[1], dataList[2], dataList[3], dataList[4],
                                              dataList[5], dataList[6],
                                              "健康" if dataList[7].replace("\n", "") == "True" else "不健康"))
        line = f.readline()
    f.close()


def clear_history_data():
    f = open("./data/history.txt", "w", encoding="utf-8")
    f.write("")
    f.close()
    refresh_history_data()


def delete_selected_data():
    if len(treeHistory.selection()) != 1:
        messagebox.showwarning("提示", "请选择一条要删除的数据")
        return
    selectedData = treeHistory.item(treeHistory.focus()).get("values")[0] - 1
    print(selectedData)
    with open("./data/history.txt", "r", encoding="utf-8") as f_r:
        lines = f_r.readlines()
    with open("./data/history.txt", "w", encoding="utf-8") as f_w:
        for it in range(len(lines)):
            if it != selectedData:
                f_w.write(lines[it])
    treeHistory.delete(treeHistory.selection())
    refresh_history_data()


def display_loading_result_gif():
    while 1:
        gifImg = Image.open("./data/loading.gif")
        iterator = ImageSequence.Iterator(gifImg)
        for frame in iterator:
            pic = ImageTk.PhotoImage(frame)
            labelFigureLoading.config(image=pic)
            time.sleep(0.1)


def display_loading_suggestion_gif():
    while 1:
        gifImg = Image.open("./data/loading.gif")
        iterator = ImageSequence.Iterator(gifImg)
        for frame in iterator:
            pic = ImageTk.PhotoImage(frame)
            labelFigureSuggestionLoading.config(image=pic)
            time.sleep(0.1)


"""窗口"""
window = tk.Tk()
window.title("膝关节安全评估")
window.geometry("1000x600")
window.resizable(False, False)
window.iconphoto(True, tk.PhotoImage(file="./data/icon.png"))

window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", theme)

"""顶部栏"""
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
frameInfoBasic.place(x=50, y=40, width=500, height=50, anchor="w")

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
frameInfoHeight.place(x=50, y=90, width=500, height=50, anchor="w")
labelHeight = ttk.Label(frameInfoHeight, text="身高(cm)：", font=("微软雅黑", 12))
labelHeight.place(x=0, y=20, anchor="w")
entryHeight = ttk.Entry(frameInfoHeight, width=50)
entryHeight.place(x=120, y=20, anchor="w")

frameInfoWeight = ttk.Frame(labelFrameInfo, height=50)
frameInfoWeight.place(x=50, y=140, width=500, height=50, anchor="w")
labelWeight = ttk.Label(frameInfoWeight, text="体重(kg)：", font=("微软雅黑", 12))
labelWeight.place(x=0, y=20, anchor="w")
entryWeight = ttk.Entry(frameInfoWeight, width=50)
entryWeight.place(x=120, y=20, anchor="w")

frameInfoLength = ttk.Frame(labelFrameInfo, height=50)
frameInfoLength.place(x=50, y=190, width=500, height=50, anchor="w")
labelLength = ttk.Label(frameInfoLength, text="大腿长度(cm)：", font=("微软雅黑", 12))
labelLength.place(x=0, y=20, anchor="w")
entryLength = ttk.Entry(frameInfoLength, width=50)
entryLength.place(x=120, y=20, anchor="w")

frameInfoCircum = ttk.Frame(labelFrameInfo, height=50)
frameInfoCircum.place(x=50, y=240, width=500, height=50, anchor="w")
labelCircum = ttk.Label(frameInfoCircum, text="膝盖腿围(cm)：", font=("微软雅黑", 12))
labelCircum.place(x=0, y=20, anchor="w")
entryCircum = ttk.Entry(frameInfoCircum, width=50)
entryCircum.place(x=120, y=20, anchor="w")

frameInfoExperience = ttk.Frame(labelFrameInfo, height=50)
frameInfoExperience.place(x=50, y=290, width=500, height=50, anchor="w")
labelExperience = ttk.Label(frameInfoExperience, text="损伤经历：", font=("微软雅黑", 12))
labelExperience.place(x=0, y=20, anchor="w")
entryExperience = ttk.Entry(frameInfoExperience, width=50)
entryExperience.place(x=120, y=20, anchor="w")

frameData = ttk.Frame(window, height=50)
frameData.place(x=500, y=470, width=600, height=50, anchor="n")

entryData: Entry = ttk.Entry(frameData, width=65, state="readonly")
entryData.place(x=0, y=20, anchor="w")

buttonData = tk.Button(frameData, text="导入数据", command=import_data, font=("微软雅黑", 12))
buttonData.place(x=600, y=20, width=120, height=40, anchor="e")

buttonCommit = tk.Button(window, text="确定", command=get_result, font=("微软雅黑", 12))
buttonCommit.place(x=570, y=530, width=120, height=40, anchor="n")

"""检测结果"""
labelFrameResultTitle = ttk.Label(text="检测结果", font=("微软雅黑", 14))
labelFrameResult = ttk.LabelFrame(window, labelwidget=labelFrameResultTitle)

labelFrameResultBasicTitle = ttk.Label(text="基本信息", font=("微软雅黑", 14))
labelFrameResultBasic = ttk.LabelFrame(window, labelwidget=labelFrameResultBasicTitle)

labelResultName = ttk.Label(labelFrameResultBasic, font=("微软雅黑", 12))
labelResultAge = ttk.Label(labelFrameResultBasic, font=("微软雅黑", 12))
labelResultGender = ttk.Label(labelFrameResultBasic, font=("微软雅黑", 12))
labelResultHeight = ttk.Label(labelFrameResultBasic, font=("微软雅黑", 12))
labelResultWeight = ttk.Label(labelFrameResultBasic, font=("微软雅黑", 12))
labelResultLength = ttk.Label(labelFrameResultBasic, font=("微软雅黑", 12))
labelResultCircum = ttk.Label(labelFrameResultBasic, font=("微软雅黑", 12))
labelResultExperience = ttk.Label(labelFrameResultBasic, font=("微软雅黑", 12), wraplength=180)

frameResultLoading = ttk.Frame(labelFrameResult, height=300)
figureLoading = tk.PhotoImage(file="./data/loading.gif")
labelFigureLoading = tk.Label(frameResultLoading, image=figureLoading)
labelFigureLoading.place(x=0, y=50, anchor="w")
labelResultLoading = ttk.Label(frameResultLoading, text="正在计算...", font=("微软雅黑", 12))
labelResultLoading.place(x=80, y=48, anchor="w")

frameResultData = ttk.Frame(labelFrameResult, height=50)
frameResultData.place(x=340, y=320, width=660, height=40, anchor="n")
labelResultData1 = ttk.Label(frameResultData, font=("微软雅黑", 12))
labelResultData1.place(x=0, y=20, height=30, anchor="w")
labelResultData2 = ttk.Label(frameResultData, font=("微软雅黑", 12))
labelResultData2.place(x=240, y=20, height=30, anchor="w")
labelResultData3 = ttk.Label(frameResultData, font=("微软雅黑", 12))
labelResultData3.place(x=460, y=20, height=30, anchor="w")

frameResultFigure = tk.Frame(labelFrameResult)

buttonCheckSuggestion = tk.Button(window, text="查看健康建议", command=get_suggestion, font=("微软雅黑", 12))
buttonReturnInfo = tk.Button(window, text="编辑基本信息", command=return_info, font=("微软雅黑", 12))

"""健康建议"""
labelFrameSuggestionTitle = ttk.Label(text=" ", font=("微软雅黑", 14))
labelFrameSuggestion = ttk.LabelFrame(window, labelwidget=labelFrameSuggestionTitle)

frameSuggestionLoading = ttk.Frame(labelFrameSuggestion)
frameSuggestionLoading.place(x=350, y=170, width=300, height=100, anchor="center")
labelFigureSuggestionLoading = tk.Label(frameSuggestionLoading, image=figureLoading)
labelFigureSuggestionLoading.place(x=0, y=50, anchor="w")
labelSuggestionLoading = ttk.Label(frameSuggestionLoading, text="正在生成健康建议...", font=("微软雅黑", 12))
labelSuggestionLoading.place(x=80, y=48, anchor="w")

textSuggestion = tk.Text(labelFrameSuggestion, width=40, height=12, wrap="char", font=("微软雅黑", 14))
labelStatus = ttk.Label(labelFrameSuggestion, font=("微软雅黑", 16))

"""历史记录"""
labelFrameHistoryTitle = ttk.Label(text="历史记录", font=("微软雅黑", 14))
labelFrameHistory = ttk.LabelFrame(window, labelwidget=labelFrameHistoryTitle)

scrollBar = ttk.Scrollbar(labelFrameHistory)
scrollBar.pack(side="right", fill="y")

treeHistory = ttk.Treeview(labelFrameHistory, columns=columns, show="headings", height=14, yscrollcommand=scrollBar.set)
for i in range(len(columns)):
    if i == 0:
        treeHistory.column(columns[i], width=50, anchor="center")
    else:
        treeHistory.column(columns[i], width=100, anchor="center")
    treeHistory.heading(columns[i], text=columns[i])
treeHistory.place(x=0, y=0, anchor="nw")

treeHistoryStyle = ttk.Style()
treeHistoryStyle.configure("Treeview.Heading", font=("微软雅黑", 12))

buttonHistory = tk.Button(window, text="查看历史记录", command=read_history_data, font=("微软雅黑", 12))
buttonHistory.place(x=430, y=530, width=120, height=40, anchor="n")

buttonReturn = tk.Button(window, text="返回", command=return_from_history, font=("微软雅黑", 12))
buttonRefresh = tk.Button(window, text="刷新", command=refresh_history_data, font=("微软雅黑", 12))
buttonClear = tk.Button(window, text="清空历史记录", command=clear_history_data, font=("微软雅黑", 12))
buttonDelete = tk.Button(window, text="删除所选记录", command=delete_selected_data, font=("微软雅黑", 12))

window.mainloop()

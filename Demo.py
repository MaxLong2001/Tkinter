# coding: gbk

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
columns = ("���", "����", "����", "�Ա�", "���(cm)", "����(kg)", "���ȳ���(cm)", "ϥ����Χ(cm)", "����״��")
negativeSuggestionText = "�������飺\n\n   ����ϥ�ؽڿ����Ѿ��ܵ������������ϥ�ǽ���û���ܵ�ͻ����ײ��" + \
                         "����������ڳ�����������������ɵ������˱���˺�ѣ�����������ʵ�����ȥ�ǿƻ�ؽ���ƾ�ҽ��\n\n" + \
                         "   �������ϥ�ǽ����ܵ���ͻ����ײ����������ʮ�������Ȱ��˶�����Ⱥ����������ͨ��Ϊ���Դ��������ˣ�" + \
                         "���������ȿ����˶�ҽѧ�ơ�\n\n   ����ѭҽ����ѡ�������ƻ��������ƣ�����Ӧ��ע����Ϣ����ʳ��" + \
                         "�ʵ�����ά���غ͸ߵ��ס���Ԫ�طḻ��ʳ��ʶȻ����ɢ�����������ò����ء� "
positiveSuggestionText = "�������飺\n\n   ����ϥ�ؽڽ���״�����ã������ṩһЩԤ��ϥ�ؽ����˵Ľ��飺\n\n" + \
                         "   ����������ϥ�ؽڽ������˶����������г�����Ӿ��������ϥ�ؽھ����˶�����Ҫʱ������û�ϥ��\n\n" + \
                         "   ע����ʳ������ά���أ��ߵ����Լ����Ʒḻ��ʳ����Ⱪ����ʳ���������أ���¥��ʱ�ٶȲ��˹��죬һ��һ�ס�"


def import_data():
    global health, figureFile
    fileName = filedialog.askopenfilename(filetypes=[("CSV�ļ�", "*.csv")])
    if fileName == "D:/�����/���п���/knee/knee/patient.csv":
        health = False
        figureFile = ImageTk.PhotoImage(file="./data/patient.png")
        labelFigure.config(image=figureFile)
    else:
        health = True
        figureFile = ImageTk.PhotoImage(file="./data/health.png")
        labelFigure.config(image=figureFile)
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
experience = ""
fileName = ""
health = True


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
        messagebox.showerror(title="��������", message="����������", parent=window)
        return
    if re.match("^\d+$", age) is None:
        messagebox.showerror(title="�������", message="��������ȷ������", parent=window)
        return
    if re.match("^\d+$", height) is None:
        messagebox.showerror(title="��ߴ���", message="��������ȷ�����", parent=window)
        return
    if re.match("^\d+$", weight) is None:
        messagebox.showerror(title="���ش���", message="��������ȷ������", parent=window)
        return
    if re.match("^\d+$", length) is None:
        messagebox.showerror(title="��ߴ���", message="��������ȷ�����", parent=window)
        return
    if re.match("^\d+$", circum) is None:
        messagebox.showerror(title="��Χ����", message="��������ȷ����Χ", parent=window)
        return
    if experience == "":
        messagebox.showerror(title="���˾�������", message="���������˾������������˾�������ޡ�", parent=window)
        return
    if fileName == "":
        messagebox.showerror(title="���ݴ���", message="��ѡ�������ļ�", parent=window)
        return
    labelFrameInfo.place_forget()
    frameData.place_forget()
    buttonCommit.place_forget()
    labelInfo.config(foreground="#CCCCCC")
    labelResult.config(foreground="#0099CC")
    labelSuggestion.config(foreground=defaultColor)
    labelHistory.config(foreground=defaultColor)
    labelFrameResult1.place(x=630, y=100, width=680, height=400, anchor="n")
    labelFrameResult2.place(x=150, y=100, width=200, height=400, anchor="n")
    buttonCheckSuggestion.place(x=500, y=530, width=120, height=40, anchor="n")
    buttonReturnInfo.place(x=640, y=530, width=120, height=40, anchor="n")
    buttonHistory.place(x=360, y=530, width=120, height=40, anchor="n")
    windowNo = 2
    init_result_info()


def init_result_info():
    global name, age, male, height, weight, length, circum
    labelResultName.config(text="������" + name)
    labelResultName.place(x=10, y=0)
    labelResultAge.config(text="���䣺" + str(age))
    labelResultAge.place(x=10, y=30)
    labelResultGender.config(text="�Ա�" + "��" if male else "�Ա�" + "Ů")
    labelResultGender.place(x=10, y=60)
    labelResultHeight.config(text="���(cm)��" + str(height))
    labelResultHeight.place(x=10, y=90)
    labelResultWeight.config(text="����(kg)��" + str(weight))
    labelResultWeight.place(x=10, y=120)
    labelResultLength.config(text="���ȳ�(cm)��" + str(length))
    labelResultLength.place(x=10, y=150)
    labelResultCircum.config(text="ϥ����Χ(cm)��" + str(circum))
    labelResultCircum.place(x=10, y=180)
    labelResultExperience.config(text="���˾�����" + experience)
    labelResultExperience.place(x=10, y=210)


def check_suggestion():
    global windowNo
    labelInfo.config(foreground="#CCCCCC")
    labelResult.config(foreground="#CCCCCC")
    labelSuggestion.config(foreground="#0099CC")
    labelHistory.config(foreground=defaultColor)
    labelFrameResult1.place_forget()
    buttonCheckSuggestion.place_forget()
    buttonReturnInfo.place_forget()
    labelFrameHistory.place_forget()
    buttonReturnInfo.place(x=570, y=530, width=120, height=40, anchor="n")
    labelFrameSuggestion.place(x=630, y=100, width=680, height=400, anchor="n")
    buttonHistory.place(x=430, y=530, width=120, height=40, anchor="n")
    if health:
        textSuggestion.config(state="normal")
        textSuggestion.delete(1.0, "end")
        textSuggestion.insert(1.0, positiveSuggestionText)
        textSuggestion.config(state="disabled")
        labelStatus.config(background="#99CC66")
        labelStatus.config(text="        ����")
    else:
        textSuggestion.config(state="normal")
        textSuggestion.delete(1.0, "end")
        textSuggestion.insert(1.0, negativeSuggestionText)
        textSuggestion.config(state="disabled")
        labelStatus.config(background="#FF0033")
        labelStatus.config(text="      ������")
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
    f = open("./data/history.txt", "a")
    f.write(name + " " + str(age) + " " + ("��" if male else "Ů") + " " + str(height) + " " + str(weight) + " " + str(
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
    buttonHistory.place_forget()
    labelFrameHistory.place(x=500, y=90, width=910, height=400, anchor="n")
    buttonRefresh.place(x=290, y=530, width=120, height=40, anchor="n")
    buttonReturn.place(x=430, y=530, width=120, height=40, anchor="n")
    buttonClear.place(x=570, y=530, width=120, height=40, anchor="n")
    buttonDelete.place(x=710, y=530, width=120, height=40, anchor="n")
    treeHistory.delete(*treeHistory.get_children())
    f = open("./data/history.txt", "r")
    line = f.readline()
    lineCount = 0
    while line:
        lineCount += 1
        dataList = line.split(" ")
        treeHistory.insert("", "end", values=(lineCount,
                                              dataList[0], dataList[1], dataList[2], dataList[3], dataList[4],
                                              dataList[5], dataList[6],
                                              "����" if dataList[7].replace("\n", "") == "True" else "������"))
        line = f.readline()
    f.close()


def return_from_history():
    global windowNo
    if windowNo == 1:
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
        labelFrameHistory.place_forget()
        buttonRefresh.place_forget()
        buttonReturn.place_forget()
        buttonClear.place_forget()
        buttonDelete.place_forget()
        labelFrameResult1.place(x=630, y=100, width=680, height=400, anchor="n")
        labelFrameResult2.place(x=150, y=100, width=200, height=400, anchor="n")
        buttonCheckSuggestion.place(x=500, y=530, width=120, height=40, anchor="n")
        buttonReturnInfo.place(x=640, y=530, width=120, height=40, anchor="n")
        buttonHistory.place(x=360, y=530, width=120, height=40, anchor="n")
    elif windowNo == 3:
        labelFrameHistory.place_forget()
        buttonRefresh.place_forget()
        buttonReturn.place_forget()
        buttonClear.place_forget()
        buttonDelete.place_forget()
        labelFrameResult2.place(x=150, y=100, width=200, height=400, anchor="n")
        buttonReturnInfo.place(x=570, y=530, width=120, height=40, anchor="n")
        labelFrameSuggestion.place(x=630, y=100, width=680, height=400, anchor="n")
        buttonHistory.place(x=430, y=530, width=120, height=40, anchor="n")


def refresh_history_data():
    treeHistory.delete(*treeHistory.get_children())
    f = open("./data/history.txt", "r")
    line = f.readline()
    lineCount = 0
    while line:
        lineCount += 1
        dataList = line.split(" ")
        treeHistory.insert("", "end", values=(lineCount,
                                              dataList[0], dataList[1], dataList[2], dataList[3], dataList[4],
                                              dataList[5], dataList[6],
                                              "����" if dataList[7].replace("\n", "") == "True" else "������"))
        line = f.readline()
    f.close()


def clear_history_data():
    f = open("./data/history.txt", "w")
    f.write("")
    f.close()
    refresh_history_data()


def delete_selected_data():
    if len(treeHistory.selection()) != 1:
        messagebox.showwarning("��ʾ", "��ѡ��һ��Ҫɾ��������")
        return
    selectedData = treeHistory.item(treeHistory.focus()).get("values")[0] - 1
    print(selectedData)
    with open("./data/history.txt", "r") as f_r:
        lines = f_r.readlines()
    with open("./data/history.txt", "w") as f_w:
        for it in range(len(lines)):
            if it != selectedData:
                f_w.write(lines[it])
    treeHistory.delete(treeHistory.selection())
    refresh_history_data()


"""����"""
window = tk.Tk()
window.title("ϥ�ؽڰ�ȫ����")
window.geometry("1000x600")
window.resizable(False, False)
window.iconphoto(True, tk.PhotoImage(file="./data/icon.png"))

window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", theme)

"""������"""
frameHead = ttk.Frame(window, height=70, relief="groove", borderwidth=1)
frameHead.pack(side="top", fill="x")

labelInfo = ttk.Label(frameHead, text="��Ϣ¼��", font=("΢���ź�", 18, "bold"), foreground="#0099CC")
labelInfo.place(x=125, y=16, anchor="n")
labelResult = ttk.Label(frameHead, text="�����", font=("΢���ź�", 18, "bold"))
labelResult.place(x=375, y=16, anchor="n")
labelSuggestion = ttk.Label(frameHead, text="��������", font=("΢���ź�", 18, "bold"))
labelSuggestion.place(x=625, y=16, anchor="n")
labelHistory = ttk.Label(frameHead, text="��ʷ��¼", font=("΢���ź�", 18, "bold"))
labelHistory.place(x=875, y=16, anchor="n")

"""������Ϣ"""
labelFrameInfoTitle = ttk.Label(text="������Ϣ", font=("΢���ź�", 14))
labelFrameInfo = ttk.LabelFrame(window, labelwidget=labelFrameInfoTitle)
labelFrameInfo.place(x=500, y=90, width=600, height=360, anchor="n")

frameInfoBasic = ttk.Frame(labelFrameInfo, height=50)
frameInfoBasic.place(x=50, y=40, width=500, height=50, anchor="w")

labelName = ttk.Label(frameInfoBasic, text="����", font=("΢���ź�", 12))
labelName.place(x=0, y=20, anchor="w")
entryName = ttk.Entry(frameInfoBasic, width=10)
entryName.place(x=40, y=20, anchor="w")

labelAge = ttk.Label(frameInfoBasic, text="����", font=("΢���ź�", 12))
labelAge.place(x=160, y=20, anchor="w")
entryAge = ttk.Entry(frameInfoBasic, width=10)
entryAge.place(x=200, y=20, anchor="w")

isMale = tk.BooleanVar()
isMale.set(True)
labelGender = ttk.Label(frameInfoBasic, text="�Ա�", font=("΢���ź�", 12))
labelGender.place(x=320, y=20, anchor="w")
radioButtonMale = ttk.Radiobutton(frameInfoBasic, text="��", variable=isMale, value=True)
radioButtonMale.place(x=360, y=20, anchor="w")
radioButtonFemale = ttk.Radiobutton(frameInfoBasic, text="Ů", variable=isMale, value=False)
radioButtonFemale.place(x=410, y=20, anchor="w")

frameInfoHeight = ttk.Frame(labelFrameInfo, height=50)
frameInfoHeight.place(x=50, y=90, width=500, height=50, anchor="w")
labelHeight = ttk.Label(frameInfoHeight, text="���(cm)��", font=("΢���ź�", 12))
labelHeight.place(x=0, y=20, anchor="w")
entryHeight = ttk.Entry(frameInfoHeight, width=50)
entryHeight.place(x=120, y=20, anchor="w")

frameInfoWeight = ttk.Frame(labelFrameInfo, height=50)
frameInfoWeight.place(x=50, y=140, width=500, height=50, anchor="w")
labelWeight = ttk.Label(frameInfoWeight, text="����(kg)��", font=("΢���ź�", 12))
labelWeight.place(x=0, y=20, anchor="w")
entryWeight = ttk.Entry(frameInfoWeight, width=50)
entryWeight.place(x=120, y=20, anchor="w")

frameInfoLength = ttk.Frame(labelFrameInfo, height=50)
frameInfoLength.place(x=50, y=190, width=500, height=50, anchor="w")
labelLength = ttk.Label(frameInfoLength, text="���ȳ���(cm)��", font=("΢���ź�", 12))
labelLength.place(x=0, y=20, anchor="w")
entryLength = ttk.Entry(frameInfoLength, width=50)
entryLength.place(x=120, y=20, anchor="w")

frameInfoCircum = ttk.Frame(labelFrameInfo, height=50)
frameInfoCircum.place(x=50, y=240, width=500, height=50, anchor="w")
labelCircum = ttk.Label(frameInfoCircum, text="ϥ����Χ(cm)��", font=("΢���ź�", 12))
labelCircum.place(x=0, y=20, anchor="w")
entryCircum = ttk.Entry(frameInfoCircum, width=50)
entryCircum.place(x=120, y=20, anchor="w")

frameInfoExperience = ttk.Frame(labelFrameInfo, height=50)
frameInfoExperience.place(x=50, y=290, width=500, height=50, anchor="w")
labelExperience = ttk.Label(frameInfoExperience, text="���˾�����", font=("΢���ź�", 12))
labelExperience.place(x=0, y=20, anchor="w")
entryExperience = ttk.Entry(frameInfoExperience, width=50)
entryExperience.place(x=120, y=20, anchor="w")

frameData = ttk.Frame(window, height=50)
frameData.place(x=500, y=470, width=600, height=50, anchor="n")

entryData: Entry = ttk.Entry(frameData, width=65, state="readonly")
entryData.place(x=0, y=20, anchor="w")

buttonData = tk.Button(frameData, text="��������", command=import_data, font=("΢���ź�", 12))
buttonData.place(x=600, y=20, width=120, height=40, anchor="e")

buttonCommit = tk.Button(window, text="ȷ��", command=commit_data, font=("΢���ź�", 12))
buttonCommit.place(x=570, y=530, width=120, height=40, anchor="n")

"""�����"""
labelFrameResultTitle1 = ttk.Label(text="�����", font=("΢���ź�", 14))
labelFrameResult1 = ttk.LabelFrame(window, labelwidget=labelFrameResultTitle1)

labelFrameResultTitle2 = ttk.Label(text="������Ϣ", font=("΢���ź�", 14))
labelFrameResult2 = ttk.LabelFrame(window, labelwidget=labelFrameResultTitle2)

labelResultName = ttk.Label(labelFrameResult2, font=("΢���ź�", 12))
labelResultAge = ttk.Label(labelFrameResult2, font=("΢���ź�", 12))
labelResultGender = ttk.Label(labelFrameResult2, font=("΢���ź�", 12))
labelResultHeight = ttk.Label(labelFrameResult2, font=("΢���ź�", 12))
labelResultWeight = ttk.Label(labelFrameResult2, font=("΢���ź�", 12))
labelResultLength = ttk.Label(labelFrameResult2, font=("΢���ź�", 12))
labelResultCircum = ttk.Label(labelFrameResult2, font=("΢���ź�", 12))
labelResultExperience = ttk.Label(labelFrameResult2, font=("΢���ź�", 12), wraplength=180)

figureFile = ImageTk.PhotoImage(file="./data/health.png")
labelFigure = tk.Label(labelFrameResult1, image=figureFile, width=660, height=280)
labelFigure.place(x=340, y=180, anchor="center")

buttonCheckSuggestion = tk.Button(window, text="�鿴��������", command=check_suggestion, font=("΢���ź�", 12))

buttonReturnInfo = tk.Button(window, text="�༭������Ϣ", command=return_info, font=("΢���ź�", 12))

"""��������"""
labelFrameSuggestionTitle = ttk.Label(text=" ", font=("΢���ź�", 14))
labelFrameSuggestion = ttk.LabelFrame(window, labelwidget=labelFrameSuggestionTitle)

textSuggestion = tk.Text(labelFrameSuggestion, width=65, height=15, wrap="char", font=("����", 15))
textSuggestion.place(x=340, y=200, anchor="center")

labelStatus = ttk.Label(labelFrameSuggestion, font=("΢���ź�", 16))
labelStatus.place(x=340, y=16, width=140, height=40, anchor="center")

"""��ʷ��¼"""
labelFrameHistoryTitle = ttk.Label(text="��ʷ��¼", font=("΢���ź�", 14))
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
treeHistoryStyle.configure("Treeview.Heading", font=("΢���ź�", 12))

buttonHistory = tk.Button(window, text="�鿴��ʷ��¼", command=read_history_data, font=("΢���ź�", 12))
buttonHistory.place(x=430, y=530, width=120, height=40, anchor="n")

buttonReturn = tk.Button(window, text="����", command=return_from_history, font=("΢���ź�", 12))
buttonRefresh = tk.Button(window, text="ˢ��", command=refresh_history_data, font=("΢���ź�", 12))
buttonClear = tk.Button(window, text="�����ʷ��¼", command=clear_history_data, font=("΢���ź�", 12))
buttonDelete = tk.Button(window, text="ɾ����ѡ��¼", command=delete_selected_data, font=("΢���ź�", 12))

window.mainloop()

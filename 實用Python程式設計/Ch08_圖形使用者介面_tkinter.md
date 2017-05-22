
# Ch08 圖形使用者介面：tkinter
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Ch08 圖形使用者介面：tkinter](#ch08-圖形使用者介面tkinter)
  * [8.1 元件語法](#81-元件語法)
  * [8.2 幾何管理](#82-幾何管理)
  * [8.3 範例](#83-範例)
  * [8.4 習題](#84-習題)

<!-- tocstop -->



```python
## Python Codes for Chapter 8: Graphic User Interface: tkinter

#########

# from Tkinter import *   # Python 版本 3 以下
from tkinter import *    # Python 版本 3 以上
```

## 8.1 元件語法


```python
root = Tk()  # 宣告視窗名稱
frame = Frame(root, bg = 'black', height = 30, width = 30)
frame.grid(row = 0)  # 置放於視窗元件
root.mainloop()

root = Tk()
label = Label(root, bg = 'pink', text = 'Hello world!')
label.grid(row = 0)
root.mainloop()

root = Tk()
labelframe = LabelFrame(root, text = 'This is a test', bg = 'light green')
labelframe.grid(row = 0)
label1 = Label(labelframe, text = 'Label1')
label1.grid(row = 0, column = 0)
label2 = Label(labelframe, text = 'Label2')
label2.grid(row = 0, column = 1)
root.mainloop()

root = Tk()
text = Text(root, width = 30, height = 10)
text.insert(INSERT, "Hello~~~")
text.insert(END, "I like Python~~")
text.pack()
text.tag_add("tagit", "1.15", "1.21")
text.tag_config("tagit", background = "red", foreground = "yellow")
root.mainloop()

root = Tk()
textvar1 = DoubleVar() # 資料型態 double, 預設 0.0
textvar2 = IntVar()     # 資料型態 int, 預設 0
textvar3 = StringVar() # 資料型態 string, 預設 ''
entry1 = Entry(root, textvariable = textvar1)
entry1.grid(row = 0)
entry2 = Entry(root, textvariable = textvar2)
entry2.grid(row = 1)
entry3 = Entry(root, textvariable = textvar3)
entry3.grid(row = 2)
root.mainloop()

def get_info():
    temp = textvar.get() # 利用 get 指令取得第一個文字方塊之值
    gettextvar.set(temp) # 利用 set 指令將所取得之值顯示在第二個文字方塊

root = Tk()
textvar = DoubleVar()
gettextvar = DoubleVar()
entry1 = Entry(root, textvariable = textvar, width = 10).pack()
button = Button(root, text = 'Enter', width = 10, command = get_info).pack()
entry2 = Entry(root, textvariable = gettextvar, width = 10).pack()
root.mainloop()

root = Tk()
menubar = Menu(root)
text =  lambda: messagebox.showinfo("Show" , "Hello!!!")
def click():
    result = messagebox.askokcancel("Continue?", "Wanna leave?")
    if result == True:
        root.destroy() # 關閉視窗

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Show', command = text)
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = click)
menubar.add_cascade(label = 'Info', menu = filemenu)
root.config(menu = menubar)

root = Tk()
text =  lambda: messagebox.showinfo("Show" , "Hello!!!")
def click():
    result = messagebox.askokcancel("Continue?", "Wanna leave?")
    if result == True:
        root.destroy() # 關閉視窗

mbutton = Menubutton(root, text = 'Info')
filemenu = Menu(mbutton, tearoff = 0)
mbutton.config(menu = filemenu)
filemenu.add_command(label = 'Show', command = text)
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = click)
mbutton.grid(row = 0, column = 0, sticky = 'W')
mbutton.config(bg = 'yellow', bd = 1)

root = Tk()
root.title("Test")
''
leave = lambda: root.destroy() # 關閉視窗
def show():
    if checkvar.get() == 1:
        label.config(bg = 'red')
    else:
        label.config(bg = 'yellow')

label = Label(root, text = "Demo", width = 10, bg = 'yellow')
label.grid(row = 0,  column = 0)
button = Button(root, text = "Show", width = 4, command = show)
button.grid(row = 0,  column = 1)
checkvar = IntVar()
checkbutton = Checkbutton(root, text = "Red", variable = checkvar, width = 10)
checkbutton.grid(row = 1,  column = 0)
button = Button(root, text = "Exit", command = leave, width = 4)
button.grid(row = 1,  column = 1)
```

## 8.2 幾何管理


```python
root = Tk()
label = Label(root, text = 'Hello world!!', font = 'Calibri 10')
label.pack()

root = Tk()
label = Label(root, text = 'Hello world!!', font = 'Calibri 10')
label.grid(row = 0, column = 0, rowspan = 2)

root = Tk()
label = Label(root, text = 'Hello world!!', font = 'Calibri 10')
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
```

## 8.3 範例


```python
from tkinter import *
root = Tk()
root.title('開興通訊行')
def click():
    if case1 == True:
        entry_fr.delete(0, END); entry_tw1.delete(0, END); entry_jp1.delete(0, END) # 清除所有文字方塊中的數值
        label_money1 = Label(root, text = '消費金額 : 0').grid(row = 1, column = 0, sticky = 'WE')
    else:
        entry_ge.delete(0, END); entry_tw2.delete(0, END); entry_jp2.delete(0, END)
        label_money2 = Label(root, text = '消費金額 : 0').grid(row = 1, column = 0, sticky = 'WE')

def type_phone():
    global case1; global case2
    case1 = True
    case2 = False
    lbfr1 = LabelFrame(root, text = '手機廠牌')
    lbfr1.grid(row = 0, column = 0)
    label_tw = Label(lbfr1, text = '國產牌手機(10000元)')
    label_tw.grid(row = 0, column = 0)
    label_jp = Label(lbfr1, text = '日本牌手機(15000元)')
    label_jp.grid(row = 1, column = 0)
    label_fr = Label(lbfr1, text = '水果牌手機(20000元)')
    label_fr.grid(row = 2, column = 0)
    lbfr2 = LabelFrame(root, text = '購買數量')
    lbfr2.grid(row = 0, column = 1)
    global entry_fr; global entry_tw1; global entry_jp1
    entry_fr = Entry(lbfr2)
    entry_fr.grid(row = 0, column = 0)
    entry_tw1 = Entry(lbfr2)
    entry_tw1.grid(row = 1, column = 0)
    entry_jp1 = Entry(lbfr2)
    entry_jp1.grid(row = 2, column = 0)
    global label_money1
    label_money1 = Label(root, text = '消費金額： 0')
    label_money1.grid(row = 1, column = 0, sticky = 'WE')
    button = Button(root, text = '確定', command = cal1)
    button.grid(row = 1, column = 1, sticky = 'WE')

def type_camera():
    global case1; global case2
    case1 = False
    case2 = True
    lbfr1 = LabelFrame(root, text = '相機廠牌')
    lbfr1.grid(row = 0, column = 0)
    label_tw = Label(lbfr1, text = '國產牌相機(8000元)')
    label_tw.grid(row = 0, column = 0)
    label_jp = Label(lbfr1, text = '日本牌相機(10000元)')
    label_jp.grid(row = 1, column = 0)
    label_ge = Label(lbfr1, text = '德國牌相機(15000元)')
    label_ge.grid(row = 2, column = 0)
    lbfr2 = LabelFrame(root, text = '購買數量')
    lbfr2.grid(row = 0, column = 1)
    global entry_ge; global entry_tw2; global entry_jp2
    entry_ge = Entry(lbfr2)
    entry_ge.grid(row = 0, column = 0)
    entry_tw2 = Entry(lbfr2)
    entry_tw2.grid(row = 1, column = 0)
    entry_jp2 = Entry(lbfr2)
    entry_jp2.grid(row = 2, column = 0)
    global label_money2
    label_money2 = Label(root, text = '消費金額： 0')
    label_money2.grid(row = 1, column = 0, sticky = 'WE')
    button = Button(root, text = '確定', command = cal2)
    button.grid(row = 1, column = 1, sticky = 'WE')

menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = '手機', command = type_phone)
filemenu.add_command(label = '相機', command = type_camera)
filemenu.add_separator()
filemenu.add_command(label = '清除', command = click)
menubar.add_cascade(label = '商品', menu = filemenu)
root.config(menu = menubar)
def cal1():
    num1 = int(entry_fr.get())
    num2 = int(entry_tw1.get())
    num3 = int(entry_jp1.get())
    total = num1*20000 + num2*10000 + num3*15000
    label_money1.config(text = '消費金額： '+ str(total))

def cal2():
    num1 = int(entry_ge.get())
    num2 = int(entry_tw2.get())
    num3 = int(entry_jp2.get())
    total = num1*15000 + num2*8000 + num3*10000
    label_money2.config(text = '消費金額： '+ str(total))

root.mainloop()

#########
```

## 8.4 習題

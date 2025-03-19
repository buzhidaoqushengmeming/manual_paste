import sys
from time import sleep
import keyboard
import tkinter

root = tkinter.Tk()  #定义主窗口
root.title("name") #主窗口标题
width_max,height_max = root.maxsize() #获取桌面尺寸（主窗口）最大尺寸
width,height = 480,160
window_placeAndsize = '%dx%d+%d+%d' % (width,height,(width_max-width)/2,(height_max-height)/2)
root.geometry(window_placeAndsize)
_ = ''
#geometry(宽度,高度,窗口起始位置宽度,窗口起始位置高度)
root.resizable(width=1,height=1)
def a_new_timer(i):
    a = tkinter.Tk()
    a.title("name1")  # 主窗口标题
    width_max_a, height_max_a = a.maxsize()  # 获取桌面尺寸（主窗口）最大尺寸
    width_a, height_a = 100, 50
    window_placeAndsize_a = '%dx%d+%d+%d' % (width_a, height_a, (width_max_a - width_a) / 2, (height_max_a - height_a) / 2)
    a.geometry(window_placeAndsize_a)
    # geometry(宽度,高度,窗口起始位置宽度,窗口起始位置高度)
    root.resizable(width=1, height=1)
    la = tkinter.Label(a, text="请在下面的框内输入你想输入的字符串：", width=36, height=1, bg='white', fg='black', font=('宋体', 20),
                      anchor=tkinter.W)
    # height 指标签高度，单位是字符高度(font中字号大小)的倍数
    # anchor 是字符串在标签内部的方位 (N,S,W,E,NE,NW,SW,SE,CENTER) 默认方位为center
    # width 是字符宽度，若其值为0，则根据_最宽一行文本_自适应
    # bg 文本背景颜色，fg 文本颜色
    la.place(x=0, y=0)
    sleep(1)
    a.destroy()
def get_var_Entry():
    print('请在5s内将光标移动到要输出的位置')
    for i in range(3):
        sleep(1)
        print(3-i)
    for i in text1.get('0.0', 'end'):
        keyboard.write(i)
    print(text1.get('0.0', 'end'))
# Lable 相关代码
l = tkinter.Label(root,text="请在下面的框内输入你想输入的字符串：", width=36, height=1, bg='white', fg='black', font=('宋体', 20), anchor=tkinter.W)
# height 指标签高度，单位是字符高度(font中字号大小)的倍数
# anchor 是字符串在标签内部的方位 (N,S,W,E,NE,NW,SW,SE,CENTER) 默认方位为center
# width 是字符宽度，若其值为0，则根据_最宽一行文本_自适应
# bg 文本背景颜色，fg 文本颜色
l.place(x=0,y=0)


# 初始化按钮
b2 = tkinter.Button(root, text='输出', width=10, bg='Orange', fg="white", command=lambda: get_var_Entry())
# 想要执行的函数不能带有参数,但python的函数可以读取全局变量
b2.place(x=400,y=60)


# 输入文本框
text1 = tkinter.Text(root,width=56,height=10)
text1.place(x=0,y=30)

# 标签可变字符串设置
var = tkinter.StringVar()  # 设置可变标签变量
var.set('  ')
l1 = tkinter.Label(root, textvariable=var, width=0, height=1, bg='white', fg='black', font=('宋体', 20), anchor=tkinter.W)
# l1.place(x=410,y=120)

# 初始化退出按钮
b3 = tkinter.Button(root, text='退出', width=10, bg='Orange', fg="white", command=lambda: exti())

def exti():
    sys.exit()
# 想要执行的函数不能带有参数,但python的函数可以读取全局变量
b3.place(x=400,y=90)
root.mainloop()






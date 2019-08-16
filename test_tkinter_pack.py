from tkinter import *

root = Tk()
# 生成一个 400 * 150 大小的窗口
root.geometry("400x150")
# 生成五个 label 内容分别是 1，2，3，4，5 字体颜色是白色的
label1 = Label(root, text='1', fg="white", bg="#557097", height=3, width=6)
label2 = Label(root, text='2', fg="white", bg="#610814", height=3, width=6)
label3 = Label(root, text='3', fg="white", bg="#030c2d", height=3, width=6)
label4 = Label(root, text='4', fg="white", bg="#a9a9a9", height=3, width=6)
label5 = Label(root, text='5', fg="white", bg="#6a3906", height=3, width=6)
# 将这5个label全部从右往左放在root中
label1.pack(side=RIGHT)
label2.pack(side=RIGHT)
label3.pack(side=RIGHT)
label4.pack(side=RIGHT)
label5.pack(side=RIGHT)
root.mainloop()

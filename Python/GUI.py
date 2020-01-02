from tkinter import *
window = Tk()
# Label(window, text="图片文件夹:").grid(row=0, sticky=W)
# Entry(window).grid(row=0,column=1,sticky=E)

# Label(window, text="图片文件夹:").grid(row=1, sticky=W)
# Entry(window).grid(row=1,column=1,sticky=E)

def xinlabel(event):
    global window
    s = Label(window,text="模拟按钮")
    s.pack()

t=Button(window,text="模拟按钮")
t.bind("<Button-1>",xinlabel)
t.pack()

window.mainloop()

# import tkinter as tk
# window = tk.Tk()
# window.title("图片裁剪工具")
# window.geometry('500x300')
# var = tk.StringVar()
# l = tk.Label(window,textvariable = var,bg='green',width=30,height=2)
# l.pack()

# on_hit = False
# def hit_me():
#     global on_hit
#     if on_hit == False:
#         on_hit = True
#         var.set('you hit me')
#     else:
#         on_hit = False
#         var.set('')

# b = tk.Button(window,text='hit me',bg='white',fg='black',width=10,height=1,command = hit_me)
# b.pack()
# e1 = tk.Entry(window, show='*', font=('Arial', 14))   # 显示成密文形式
# e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
# e1.pack()
# e2.pack()

# window.mainloop()

# from tkinter import *
# from tkinter.filedialog import askdirectory

# def selectRPath():
#     path_ = askdirectory()
#     rpath.set(path_)

# def selectDPath():
#     path_ = askdirectory()
#     dpath.set(path_)

# root = Tk()
# rpath = StringVar()
# dpath = StringVar()

# root.geometry('500x300')

# Label(root,text = "源路径:").grid(row = 0, column = 0)
# Entry(root, textvariable = rpath).grid(row = 0, column = 1)
# Button(root, text = "路径选择", command = selectRPath).grid(row = 0, column = 2)

# Label(root,text = "目的路径:").grid(row = 1, column = 0)
# Entry(root, textvariable = dpath).grid(row = 1, column = 1)
# Button(root, text = "路径选择", command = selectDPath).grid(row = 1, column = 2)

# root.mainloop()

import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("sangbeom project(GUI)")
root.geometry("640x480")


valuse = [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=valuse)
combobox.pack()
combobox.set("카드 결제일")

readonly_combobox = ttk.Combobox(root, height=10, values=valuse, state="readonly")
readonly_combobox.current(0) # 0 번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="선택", command = btncmd)
btn.pack()




root.mainloop()
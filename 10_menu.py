from tkinter import *


root = Tk()
root.title("sangbeom project(GUI)")
root.geometry("640x480")

menu = Menu(root)

def create_new_file():
    print("새 파일을 만듭니다.")

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

# edit 메뉴

menu.add_cascade(label="Edit")

# 메뉴에 라디오 버튼 추가

menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="language", menu=menu_lang)
menu.add_cascade(label="File", menu=menu_file)

# View 메뉴 추가

menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()
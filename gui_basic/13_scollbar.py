from tkinter import *

root = Tk()

root.title("Jh GUI")
root.geometry("640x480+300+100") # 가로 x 세로 + x 좌표 + y 좌표

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")


# set 이 없으면 스크롤을 대려도 다시 올리옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
  listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()
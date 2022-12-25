from tkinter import *

root = Tk()

root.title("Jh GUI")
root.geometry("640x480+300+100") # 가로 x 세로 + x 좌표 + y 좌표

listbox = Listbox(root, selectmode="extended", height=0) # single = 하나만 선택 # extended = 여러개 선택
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")


listbox.pack()

def btncmd():
  pass

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()
from tkinter import *

root = Tk()
root.title("Jh GUI")
root.geometry("640x480+300+100") # 가로 x 세로 + x 좌표 + y 좌표
lbl1 = Label(root, text="안녕하세요")
lbl1.pack()

photo = PhotoImage(file="gui_basic/img.png")
lbl2 = Label(root, image=photo)
lbl2.pack()

def change():
  lbl1.config(text="또 만나요") # config = 변경

  global photo2
  photo2 = PhotoImage(file="gui_basic/img2.png")
  lbl2.config(image=photo2)
  
btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
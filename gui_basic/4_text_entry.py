from tkinter import *

root = Tk()

root.title("Jh GUI")
root.geometry("640x480+300+100") # 가로 x 세로 + x 좌표 + y 좌표

# Text = 여러 줄
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

# Entry = 한 줄
e = Entry(root, width=30)
e.insert(0, "한줄만 입력해요")

e.pack()

def btncmd():
  # 내용 출력
  print(txt.get("1.0", END)) # "1.0" → 1 : 라인, 0 : 0번째 column 위치 처음부터 끝까지의 변수의 내용을 가져옴 
  print(e.get())
  
  # 내용 삭제
  txt.delete("1.0", END)
  e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()
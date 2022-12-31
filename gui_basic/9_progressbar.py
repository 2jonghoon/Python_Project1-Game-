import time
import tkinter.ttk as ttk
from tkinter import *


root = Tk()

root.title("Jh GUI")
root.geometry("640x480+300+100") # 가로 x 세로 + x 좌표 + y 좌표

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # maximum = 최대값 / indeterminate = 프로그레스바가 언제 끝날지 모름
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # maximum = 최대값 / determinate = 
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#   progressbar.stop() # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
  for i in range(1, 101): # 1 부터 100 까지
    time.sleep(0.01) # 0.01 초 대기
    
    p_var2.set(i)
    
    # GUI 업데이트 
    progressbar2.update()
    print(p_var2.get())
    
btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()
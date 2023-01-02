from tkinter import *

'''
Quiz) tkinter 를 이용한 메모장 프로그램을 만드시오

[GUI 조건]
1. title : 제목 없음 - Windows 메모장
2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
3-3. 끝내기 : 프로그램 종료
4. 프로그램 시작 시 본문은 비어 있는 상태
5. 하단 status 바는 필요 없음
6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
7. 본문 우측에 상하 스크롤 바 넣기

'''

root = Tk()

# 1. title : 제목 없음 - Windows 메모장
root.title("제목 없음 - Windows 메모장")

# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
root.geometry("640x480+300+100") # 가로 x 세로 + x 좌표 + y 좌표

# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
menu = Menu(root)
# 파일
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기")
menu_file.add_command(label="저장")
menu_file.add_command(label="끝내기")
menu.add_cascade(label="파일", menu=menu_file)
# 편집
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_edit)
# 서식
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_edit)
# 보기
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="보기", menu=menu_edit)
# 도움말
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말", menu=menu_edit)

root.config(menu=menu)
root.mainloop()
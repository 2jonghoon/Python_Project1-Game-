# pip install pygame
# pygame = 비디오 게임을 개발하기 위해 설계된 파이썬 모듈들의 크로스 플랫폼 집합
# 파이썬 프로그래밍 언어와 함께 사용하도록 설계된 컴퓨터 그래픽스와 사운드 라이브러리들을 포함

import pygame # 게임 라이브러리

# 초기화 (반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("JH Game")

# 이벤트 루프가 있어야 창이 안꺼짐

# 이벤트 루프
running = True # 게임이 진행중인지 확인할 boolean형 변수
while running:
  for event in pygame.event.get(): # pygame 을 하기 위해서 필수
    if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는지?
      running = False # 게임이 진행중이 아님

# pygame 종료
pygame.quit()
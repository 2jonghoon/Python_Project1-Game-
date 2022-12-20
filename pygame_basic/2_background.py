import pygame # 게임 라이브러리

# 초기화 (반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 이미지 불러오기
# background = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\background.png")

# 화면 타이틀 설정
pygame.display.set_caption("JH Game")

# 이벤트 루프가 있어야 창이 안꺼짐

# 이벤트 루프
running = True # 게임이 진행중인지 확인할 boolean형 변수
while running:
  for event in pygame.event.get(): # pygame 을 하기 위해서 필수
    if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는지?
      running = False # 게임이 진행중이 아님
  
  screen.fill((50, 100, 255)) # fill = RGB를 이용해서 색을 채움
  # screen.blit(background, (0,0)) # blit = 화면에 전송하다.
  
  pygame.display.update() # 화면이 계속 업데이트 되게 처리해야함
  
# pygame 종료
pygame.quit()
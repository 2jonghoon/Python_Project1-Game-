# Quiz 1) 하늘에서 떨어지는 똥 피하기 게임을 만드시오
'''
[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS는 30으로 고정

[게임 이미지]
1. 배경 : 640(세로) * 480(가로) - background.png
2. 캐릭터 : 70(세로) * 70(가로) - character.png
3. 똥 : 70(세로) * 70(가로) - ddong.png
'''

import pygame # 게임 라이브러리
from random import * # 랜덤 함수 쓰기 위함
import pyautogui

###############################################################################################
# 기본 초기화 (반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임")

# FPS (Frame Per Second)
clock = pygame.time.Clock()
###############################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰드 등 설정)
'''
1. 배경 : 640(세로) * 480(가로) - background.png
2. 캐릭터 : 70(세로) * 70(가로) - character.png
3. 똥 : 70(세로) * 70(가로) - ddong.png
'''

# 배경화면
background = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\background.png")

# 캐릭터
character = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\character.png")
# 캐릭터 사이즈 가져오기
character_size = character.get_rect().size # 배열로 저장하며 [0] = width / [1] = height
character_width = character_size[0]
character_height = character_size[1]
# 캐릭터의 위치지정
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 캐릭터의 이동 속도
character_speed = 0.6

h_value = 12

# 똥 그리기
ddong = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\ddong.png")
# 똥 사이즈 가져오기
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
# 똥 위치 지정 (랜덤함수 사용)
ddong_x_pos = randint(0, (screen_width - ddong_width))
ddong_y_pos = h_value

# 똥 내려오는 속도
ddong_speed = randint(1,20)

# 똥 그리기
ddong1 = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\ddong.png")
# 똥 사이즈 가져오기
ddong1_size = ddong1.get_rect().size
ddong1_width = ddong1_size[0]
ddong1_height = ddong1_size[1]
# 똥 위치 지정 (랜덤함수 사용)
ddong1_x_pos = randint(0, (screen_width - ddong1_width))
ddong1_y_pos = h_value

# 똥 내려오는 속도
ddong1_speed = randint(1,20)

# 똥 그리기
ddong2 = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\ddong.png")
# 똥 사이즈 가져오기
ddong2_size = ddong2.get_rect().size
ddong2_width = ddong2_size[0]
ddong2_height = ddong2_size[1]
# 똥 위치 지정 (랜덤함수 사용)
ddong2_x_pos = randint(0, (screen_width - ddong2_width))
ddong2_y_pos = h_value

# 똥 내려오는 속도
ddong2_speed = randint(1,20)

# 똥 그리기
ddong3 = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\ddong.png")
# 똥 사이즈 가져오기
ddong3_size = ddong3.get_rect().size
ddong3_width = ddong3_size[0]
ddong3_height = ddong3_size[1]
# 똥 위치 지정 (랜덤함수 사용)
ddong3_x_pos = randint(0, (screen_width - ddong3_width))
ddong3_y_pos = h_value

# 똥 내려오는 속도
ddong3_speed = randint(1,20)

# 똥 그리기
ddong4 = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\ddong.png")
# 똥 사이즈 가져오기
ddong4_size = ddong4.get_rect().size
ddong4_width = ddong4_size[0]
ddong4_height = ddong4_size[1]
# 똥 위치 지정 (랜덤함수 사용)
ddong4_x_pos = randint(0, (screen_width - ddong4_width))
ddong4_y_pos = h_value

# 똥 내려오는 속도
ddong4_speed = randint(1,20)

# 코인 그리기 2022.12.22
coin = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\coin.png")
# 코인 사이즈 가져오기
coin_size = coin.get_rect().size
coin_width = coin_size[0]
coin_height = coin_size[1]
# 코인 위치 지정
coin_x_pos = randint(0, (screen_width - coin_width))
coin_y_pos = h_value
coin_speed = randint(1,15)

# 코인 그리기 2022.12.22
coin1 = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\coin1.png")
# 코인 사이즈 가져오기
coin1_size = coin1.get_rect().size
coin1_width = coin1_size[0]
coin1_height = coin1_size[1]
# 코인 위치 지정
coin1_x_pos = randint(0, (screen_width - coin1_width))
coin1_y_pos = h_value
coin1_speed = randint(1,15)

# 코인 그리기 2022.12.22
coin2 = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\coin2.png")
# 코인 사이즈 가져오기
coin2_size = coin2.get_rect().size
coin2_width = coin2_size[0]
coin2_height = coin2_size[1]
# 코인 위치 지정
coin2_x_pos = randint(0, (screen_width - coin2_width))
coin2_y_pos = h_value
coin2_speed = randint(1,15)

# 캐릭터의 현재 좌표 변수 저장
to_x = 0

# 코인 점수
coin_score = 0

# 텍스트
# 폰트 정의
score_font = pygame.font.Font(None, 30) # 폰트 객체 생성 (폰트, 크기)
timer_font = pygame.font.Font(None, 30) # 폰트 객체 생성 (폰트, 크기)

# 총 게임 시간
totalTime = 60 # 60초
start_ticks = pygame.time.get_ticks()



running = True
while running:
  dt = clock.tick(30) # 게임 화면의 초당 프레임 수 설정

  # 2. 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      running = False 
    
    # 키를 누르면 누른키에 맞게 위치 이동
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x -= character_speed
      elif event.key == pygame.K_RIGHT:
        to_x += character_speed
      
    # 키를 떼면 현재 위치에 멈춰야함
    if event.type == pygame.KEYUP:
      to_x = 0

  # 3. 게임 캐릭터 위치 정의
  character_x_pos += to_x * dt 
  
  # 똥이 내려오는 속도
  ddong_y_pos += ddong_speed
  ddong1_y_pos += ddong1_speed
  ddong2_y_pos += ddong2_speed
  ddong3_y_pos += ddong3_speed
  ddong4_y_pos += ddong4_speed
  
  # 코인 내려오는 속도
  coin_y_pos += coin_speed
  coin1_y_pos += coin1_speed
  coin2_y_pos += coin2_speed
  
  # 캐릭터가 배경화면 밖으로 나가지 않게 설정
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width
  
  # 똥의 x 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재 설정 
  if ddong_x_pos < 0 or ddong_x_pos > screen_width - ddong_width:
    ddong_x_pos = randint(0, (screen_width - ddong_width))
  
  # 똥의 y 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재설정 하고 y좌표는 0으로 재설정
  if ddong_y_pos > screen_height:
    ddong_x_pos = randint(0, (screen_width - ddong_width))
    ddong_y_pos = h_value
  
  # 똥의 x 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재 설정 
  if ddong1_x_pos < 0 or ddong1_x_pos > screen_width - ddong1_width:
    ddong1_x_pos = randint(0, (screen_width - ddong1_width))
  
  # 똥의 y 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재설정 하고 y좌표는 0으로 재설정
  if ddong1_y_pos > screen_height:
    ddong1_x_pos = randint(0, (screen_width - ddong1_width))
    ddong1_y_pos = h_value
    
  # 똥의 x 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재 설정 
  if ddong2_x_pos < 0 or ddong2_x_pos > screen_width - ddong2_width:
    ddong2_x_pos = randint(0, (screen_width - ddong2_width))
  
  # 똥의 y 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재설정 하고 y좌표는 0으로 재설정
  if ddong2_y_pos > screen_height:
    ddong2_x_pos = randint(0, (screen_width - ddong2_width))
    ddong2_y_pos = h_value
  
  # 똥의 x 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재 설정 
  if ddong3_x_pos < 0 or ddong3_x_pos > screen_width - ddong3_width:
    ddong3_x_pos = randint(0, (screen_width - ddong3_width))
  
  # 똥의 y 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재설정 하고 y좌표는 0으로 재설정
  if ddong3_y_pos > screen_height:
    ddong3_x_pos = randint(0, (screen_width - ddong3_width))
    ddong3_y_pos = h_value
    
  # 똥의 x 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재 설정 
  if ddong4_x_pos < 0 or ddong4_x_pos > screen_width - ddong4_width:
    ddong4_x_pos = randint(0, (screen_width - ddong4_width))
  
  # 똥의 y 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재설정 하고 y좌표는 0으로 재설정
  if ddong4_y_pos > screen_height:
    ddong4_x_pos = randint(0, (screen_width - ddong4_width))
    ddong4_y_pos = h_value
  
  # 코인의 y 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재설정 하고 y좌표는 0으로 재설정
  if coin_y_pos > screen_height:
    coin_x_pos = randint(0, (screen_width - coin_width))
    coin_y_pos = h_value
  
  # 코인의 y 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재설정 하고 y좌표는 0으로 재설정
  if coin1_y_pos > screen_height:
    coin1_x_pos = randint(0, (screen_width - coin1_width))
    coin1_y_pos = h_value
  
  # 코인의 y 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재설정 하고 y좌표는 0으로 재설정
  if coin2_y_pos > screen_height:
    coin2_x_pos = randint(0, (screen_width - coin2_width))
    coin2_y_pos = h_value
    
  # 4. 충돌 처리
  # 캐릭터의 현재 좌표
  character_rect = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top  = character_y_pos
  
  # 똥의 현재 좌표
  ddong_rect = ddong.get_rect()
  ddong_rect.left = ddong_x_pos
  ddong_rect.top  = ddong_y_pos
  
  # 똥의 현재 좌표
  ddong1_rect = ddong1.get_rect()
  ddong1_rect.left = ddong1_x_pos
  ddong1_rect.top  = ddong1_y_pos
  
  # 똥의 현재 좌표
  ddong2_rect = ddong2.get_rect()
  ddong2_rect.left = ddong2_x_pos
  ddong2_rect.top  = ddong2_y_pos
  
  # 똥의 현재 좌표
  ddong3_rect = ddong3.get_rect()
  ddong3_rect.left = ddong3_x_pos
  ddong3_rect.top  = ddong3_y_pos
  
  # 똥의 현재 좌표
  ddong4_rect = ddong4.get_rect()
  ddong4_rect.left = ddong4_x_pos
  ddong4_rect.top  = ddong4_y_pos
  
  # 코인과 충돌하면 코인 1씩 증가
  coin_rect = coin.get_rect()
  coin_rect.left = coin_x_pos
  coin_rect.top  = coin_y_pos
  
  # 코인과 충돌하면 코인 1씩 증가
  coin1_rect = coin1.get_rect()
  coin1_rect.left = coin1_x_pos
  coin1_rect.top  = coin1_y_pos
  
  # 코인과 충돌하면 코인 1씩 증가
  coin2_rect = coin2.get_rect()
  coin2_rect.left = coin2_x_pos
  coin2_rect.top  = coin2_y_pos
  
  if character_rect.colliderect(ddong_rect):
    running = False
  if character_rect.colliderect(ddong1_rect):
    running = False
  if character_rect.colliderect(ddong2_rect):
    running = False
  if character_rect.colliderect(ddong3_rect):
    running = False
  if character_rect.colliderect(ddong4_rect):
    running = False
  
  if character_rect.colliderect(coin_rect):
    # 충돌하면 점수는 1씩 증가 시키고 새로 그려야함
    coin_score += 1
    coin_x_pos = randint(0, (screen_width - coin_width))
    coin_y_pos = h_value
  
  if character_rect.colliderect(coin1_rect):
    # 충돌하면 점수는 2씩 증가 시키고 새로 그려야함
    coin_score += 2
    coin1_x_pos = randint(0, (screen_width - coin1_width))
    coin1_y_pos = h_value
  
  if character_rect.colliderect(coin2_rect):
    # 충돌하면 점수는 3씩 증가 시키고 새로 그려야함
    coin_score += 3
    coin2_x_pos = randint(0, (screen_width - coin2_width))
    coin2_y_pos = h_value
  
  # 5. 화면에 그리기
  # 배경화면 그리기
  screen.blit(background, (0,0))
  
  # 캐릭터 그리기
  screen.blit(character, (int(character_x_pos), int(character_y_pos)))
  
  # 똥 떨어지는 거 그리기
  screen.blit(ddong, (int(ddong_x_pos), int(ddong_y_pos)))
  screen.blit(ddong1, (int(ddong1_x_pos), int(ddong1_y_pos)))
  screen.blit(ddong2, (int(ddong2_x_pos), int(ddong2_y_pos)))
  screen.blit(ddong3, (int(ddong3_x_pos), int(ddong3_y_pos)))
  screen.blit(ddong4, (int(ddong4_x_pos), int(ddong4_y_pos)))
  
  # 코인 그리기
  screen.blit(coin, (coin_x_pos, coin_y_pos))
  screen.blit(coin1, (coin1_x_pos, coin1_y_pos))
  screen.blit(coin2, (coin2_x_pos, coin2_y_pos))
  
  score = score_font.render("Score : {0}".format(coin_score), True, (255,255,255))
  screen.blit(score, (0, 0))
  
  # 타이머 집어 넣기
  # 경과 시간 계산
  elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ticks(경과시간)은 밀리세컨드(ms) 이기 때문에 1000 으로 나눠야 초 단위로 표시
  timer = timer_font.render("Time : " + str(int(totalTime - elapsed_time)), True, (255,255,255))  # render = 글자를 그림
  # render(출력할 글자, True, 글자 색상)
  screen.blit(timer, (screen_width - 150, 0))
  
  # 만약 시간이 0 이하이면 게임 종료
  if totalTime - elapsed_time <= 0:
    running = False
    
  if running == False:
    pyautogui.alert("최종 스코어 : {0}점 입니다.".format(coin_score))

  pygame.display.update() # 화면이 계속 업데이트 되게 처리해야함

# pygame 종료
pygame.quit()
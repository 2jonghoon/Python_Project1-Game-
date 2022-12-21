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
3. 똥 : 70(세로) * 70(가로) - enemy.png
'''

import pygame # 게임 라이브러리
from random import * # 랜덤 함수 쓰기 위함
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
3. 똥 : 70(세로) * 70(가로) - enemy.png
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

# 똥 그리기
enemy = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\enemy.png")
# 똥 사이즈 가져오기
enemy_size = enemy.get_rect().size
enemy_width = character_size[0]
enemy_height = character_size[1]
# 똥 위치 지정 (랜덤함수 사용)
enemy_x_pos = randrange(int(0), int((screen_width - enemy_width)+1))
enemy_y_pos = 0

# 똥 내려오는 속도
enemy_speed = 15

# 캐릭터의 현재 좌표 변수 저장
to_x = 0

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
  enemy_y_pos += enemy_speed
  
  # 캐릭터가 배경화면 밖으로 나가지 않게 설정
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width
  
  # 똥의 x 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재 설정 
  if enemy_x_pos < 0 or enemy_x_pos > screen_width - enemy_width:
    enemy_x_pos = randrange(int(0), int((screen_width - enemy_width)+1))
  
  # 똥의 y 좌표가 배경화면 밖으로 나갈 경우 랜덤값으로 x좌표 재설정 하고 y좌표는 0으로 재설정
  if enemy_y_pos > screen_height - enemy_height:
    enemy_x_pos = randrange(int(0), int((screen_width - enemy_width)+1))
    enemy_y_pos = 0
    
  # 4. 충돌 처리
  # 캐릭터의 현재 좌표
  character_rect = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top  = character_y_pos
  
  # 똥의 현재 좌표
  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x_pos
  enemy_rect.top  = enemy_y_pos + enemy_speed

  if character_rect.colliderect(enemy_rect):
    print("게임종료")
    running = False
    
  # 5. 화면에 그리기
  # 배경화면 그리기
  screen.blit(background, (0,0))
  
  # 캐릭터 그리기
  screen.blit(character, (int(character_x_pos), int(character_y_pos)))
  
  # 똥 떨어지는 거 그리기
  screen.blit(enemy, (int(enemy_x_pos), int(enemy_y_pos)))
  
  pygame.display.update() # 화면이 계속 업데이트 되게 처리해야함

pygame.time.delay(1000)

# pygame 종료
pygame.quit()
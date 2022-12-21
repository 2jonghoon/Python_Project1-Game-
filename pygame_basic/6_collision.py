import pygame # 게임 라이브러리

# 초기화 (반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 이미지 불러오기
background = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\character.png")
character_size = character.get_rect().size # 해당 이미지의 사이즈를 구해옴
character_width = character_size[0] # 첫번째는 width
character_height = character_size[1] # 두번째는 height
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 X 좌표 구하기 (화면 가로 크기/2)
character_y_pos = screen_height - character_height # 화면 Y 좌표 구하기 (화면 세로 크기)

# 이동할 좌표 값
to_x = 0
to_y = 0

# 캐릭터 이동 속도
character_speed = 0.6

# 적 캐릭터 만들기
enemy = pygame.image.load("D:\\sourceTree\\Pythone_Project1(Game)\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size # 해당 이미지의 사이즈를 구해옴
enemy_width = enemy_size[0] # 첫번째는 width
enemy_height = enemy_size[1] # 두번째는 height
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 X 좌표 구하기 (화면 가로 크기/2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 Y 좌표 구하기 (화면 세로 크기)

# 화면 타이틀 설정
pygame.display.set_caption("JH Game")

# FPS (Frame Per Second)
clock = pygame.time.Clock()

# 이벤트 루프가 있어야 창이 안꺼짐
# 이벤트 루프
running = True # 게임이 진행중인지 확인할 boolean형 변수
while running:
  dt = clock.tick(60) # 게임 화면의 초당 프레임 수 설정
  
  print("fps : " + str(clock.get_fps()))
  
  # 캐릭터가 1초동안 100 만큼 이동을 해야함
  # 10 fps : 1초 동안에 10번 동작 → 1번에 몇 만큼 이동? 10만큼! 10 * 10 = 100
  # 20 fps : 1초 동안에 20번 동작 → 1번에 5만큼! 5 * 20 = 100
  
  
  for event in pygame.event.get(): # pygame 을 하기 위해서 필수
    if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는지?
      running = False # 게임이 진행중이 아님

    # 키보드 이벤트 발생
    if event.type == pygame.KEYDOWN: # 키가 눌려져있는지 확인

      if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
        to_x -= character_speed # to_x = to_x - 5
      elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
        to_x += character_speed
      elif event.key == pygame.K_UP: # 캐릭터를 위로
        to_y -= character_speed
      elif event.key == pygame.K_DOWN: # 캐릭터를 아래
        to_y += character_speed
    
    if event.type == pygame.KEYUP: # 키를 뗌
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0
    
  character_x_pos += to_x * dt # 프레임 값을 곱해야함
  character_y_pos += to_y * dt # 프레임 값을 곱해야함
  
  # 캐릭터가 화면 밖으로 나가게 되면 못나가게 조건
  # 가로 경계값 처리
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width :
    character_x_pos = screen_width - character_width
  
  # 세로 경계값 처리
  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > screen_height - character_height:
    character_y_pos = screen_height - character_height
  
  
  # 충돌 처리를 위한 rect 정보 업데이트
  character_rect = character.get_rect() # x,y 좌표 / width,height 가짐
  character_rect.left = character_x_pos # 캐릭터의 x좌표
  character_rect.top = character_y_pos # 캐릭터의 y좌표
  
  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x_pos
  enemy_rect.top = enemy_y_pos
  
  # character 와 enemy 가 만날때
  if character_rect.colliderect(enemy_rect): # 사각형 기준으로 충돌이 있는지 확인
    print("충돌했어요")
    running = False
  
  # screen.fill((50, 100, 255)) # fill = RGB를 이용해서 색을 채움
  screen.blit(background, (0,0)) # blit = 화면에 전송하다.
  
  screen.blit(character, (int(character_x_pos), int(character_y_pos)))
  
  # 적 캐릭터 그리기
  screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
  
  pygame.display.update() # 화면이 계속 업데이트 되게 처리해야함
  
# pygame 종료
pygame.quit()
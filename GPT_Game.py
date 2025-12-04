import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기
w = 480
h = 600

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# 화면 설정
pad = pygame.display.set_mode((w, h))
pygame.display.set_caption("Bouncing Ball Game")

# FPS 설정
clock = pygame.time.Clock()

# 패들 속성
paddle_width = 100
paddle_height = 15
paddle_x = w / 2 - paddle_width / 2  # 패들 시작 위치 (화면 중앙)
paddle_y = h - 50  # 패들 Y 위치 (하단)
paddle_speed = 10

# 공 속성
ball_radius = 10
ball_x = w / 2  # 공 시작 위치 (화면 중앙)
ball_y = h / 2
ball_dx = 3  # 공의 X 이동 속도
ball_dy = -3  # 공의 Y 이동 속도

# 점수
score = 0

# 글씨 쓰기 함수
def write(text, x, y, color, size=30):
    font = pygame.font.Font(None, size)  # 기본 폰트 사용
    text_surface = font.render(text, True, color)
    pad.blit(text_surface, (x, y))

# 게임 루프
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:  # 왼쪽 화살표
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < w - paddle_width:  # 오른쪽 화살표
        paddle_x += paddle_speed

    # 공 이동
    ball_x += ball_dx
    ball_y += ball_dy

    # 공과 벽의 충돌 처리
    if ball_x - ball_radius < 0 or ball_x + ball_radius > w:
        ball_dx = -ball_dx  # X 방향 반사
    if ball_y - ball_radius < 0:
        ball_dy = -ball_dy  # Y 방향 반사

    # 공과 패들의 충돌 처리
    if ball_y + ball_radius >= paddle_y and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_dy = -ball_dy  # 공이 패들과 충돌 시 공을 반사
        score += 1  # 점수 증가

    # 공이 바닥에 닿으면 게임 종료
    if ball_y + ball_radius > h:
        write("GAME OVER", w / 3, h / 2, red, 50)
        write(f"Score: {score}", w / 3, h / 2 + 60, white, 30)
        pygame.display.update()
        pygame.time.delay(2000)  # 2초 후 게임 종료
        pygame.quit()
        sys.exit()

    # 화면에 그리기
    pad.fill(black)  # 배경을 검정색으로 채움

    # 패들 그리기 (사각형)
    pygame.draw.rect(pad, blue, (paddle_x, paddle_y, paddle_width, paddle_height))

    # 공 그리기 (원)
    pygame.draw.circle(pad, white, (ball_x, ball_y), ball_radius)

    # 점수 표시
    write(f"Score: {score}", 10, 10, white)

    pygame.display.update()
    clock.tick(60)  # 초당 60프레임

# 주의점: 라이브러리명과 같은 파일명 사용 불가

import pygame
import sys
pygame.init()

# # # #

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)

# # # #

w = 480
h = 640

pad = pygame.display.set_mode((w,h))
pygame.display.set_caption('Shooting Game')

pad.fill(white)
# # 선 그리기
# pygame.draw.line(pad, red, (0,h/3), (w,h/3), 5)
# pygame.draw.line(pad, red, (w/2,0), (w/2,h), 5)

# # 원그리기
# pygame.draw.circle(pad, blue, (100,100), 50, 5)
# pygame.draw.circle(pad, blue, (380,100), 50, 5)

# # 사각형 그리기
# pygame.draw.rect(pad, yellow, (120, 400, 240, 200), 5)

# pygame.draw.polygon(pad, black, ((w/2,h/3),(100,400), (380,400)), 5)

# pygame.draw.ellipse(pad, red, (100,150,150,80),2)

# 그리기

pygame.draw.rect(pad, yellow, (120, 400, 240, 200), 0)
pygame.draw.rect(pad, yellow, (300, 200, 50, 200), 0)
pygame.draw.rect(pad, red, (200, 500, 80, 100), 0)

pygame.draw.circle(pad, blue, (320 , 180), 10, 5)
pygame.draw.circle(pad, blue, (320 , 140), 10, 5)
pygame.draw.circle(pad, blue, (320 , 100), 10, 5)
pygame.draw.circle(pad, blue, (320 , 60), 10, 5)


pygame.draw.polygon(pad, black, ((w/2,h/3),(100,400), (380,400)), 0)


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
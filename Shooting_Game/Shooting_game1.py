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

bg = pygame.image.load("images/background1.jpg") # 이미지 가져오기
pad.blit(bg,(-100,-100))

p = pygame.image.load("images/plane3.png")
pad.blit(p,(w/2-36,h-76))


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# 주의점: 라이브러리명과 같은 파일명 사용 불가

import pygame
import sys
import random
pygame.init()

# # # #

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)

# # # #

w = 480
h = 600

pad = pygame.display.set_mode((w,h))
pygame.display.set_caption('Shooting Game')


# -------------이미지 로드 함수------------------
def img_load(obj):
    img = pygame.image.load("images/"+str(obj))
    img_size = img.get_rect().size
    return img, img_size[0],img_size[1]
# ---------------------------------------------


bg = img_load("background1.jpg")[0] # 이미지 가져오기
p,pw,ph = img_load("plane3.png")
r,rw,rh = img_load("rock02.png")

px = w/2-pw/2
py = h-ph
ps = 0 # 전투기 스피드

pad.blit(bg,(-100,-100))
pad.blit(p,(px,py))
pad.blit(r,(random.randint(0,w-rw),10))


pygame.display.update()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT: # 왼쪽 화살표키
                ps = -10
            elif event.key == pygame.K_RIGHT: # 오른쪽 화살표키
                ps = +10
        if event.type in [pygame.KEYUP]:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ps = 0
    px += ps
    if(px <= 0):
        px = 0
    elif(px >= w-pw):
        px = w-pw
    
    pad.blit(bg,(-100,-100)) # 잔상 제거
    pad.blit(p,(px,py))
    pad.blit(r,(200,10))
    pygame.display.update()
    clock.tick(60)

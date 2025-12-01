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

# -------------글씨 쓰기 함수------------------
def write(string,a,b,color,size = 20):
    global pad
    font = pygame.font.Font('images/NanumGothic.ttf',size)
    text = font.render(string, False, color)
    pad.blit(text,(a,b))
# ---------------------------------------------

# -------------이미지 로드 함수------------------
def img_load(obj):
    img = pygame.image.load("images/"+str(obj))
    img_size = img.get_rect().size
    return img, img_size[0],img_size[1]
# ---------------------------------------------


bg = img_load("background3.jpg")[0] # 이미지 가져오기
p,pw,ph = img_load("plane3.png")
px = w/2-pw/2
py = h-ph
ps = 0  # 전투기 스피드

# -----------------운석그리기----------------
rlist = ["rock01", "rock02", "rock03", "rock04", "rock05", "rock06", "rock07", "rock08", "rock09", "rock10",]

r,rw,rh = img_load(random.choice(rlist)+".png")
rx = random.randint(0,w-rw)
ry = 10
rs = 2

def rock_init():
    global r, rw, rh, rx, ry
    r,rw,rh = img_load(random.choice(rlist)+".png")
    rx = random.randint(0,w-rw)
    ry = 10

# -------------------------------------------

# -----------------미사일그리기----------------
m,mw,mh = img_load("missile.png")

mx = px+pw/2-mw/2
my = py-mh
mlist = []
# -------------------------------------------

# ---------------폭발 이미지 만들기------------
exp = img_load("explosion.png")[0]
# ------------------------------------------

pad.blit(bg,(0,0))
pad.blit(p,(px,py))
pad.blit(m,(mx,my))
pad.blit(r,(rx,ry))

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
            elif event.key == pygame.K_SPACE:
                mx = px+pw/2-mw/2
                my = py-mh
                mlist.append([mx,my]) # 발사할 미사일

        if event.type in [pygame.KEYUP]:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ps = 0
    px += ps
    if(px <= 0):
        px = 0
    elif(px >= w-pw):
        px = w-pw
    
    ry += rs
    if(ry > h): # 바위가 화면 아래로 떨어지면
        rock_init()

    pad.blit(bg,(0,0)) # 잔상 제거
    pad.blit(p,(px,py))
    pad.blit(r,(rx,ry))

    # 전투기와 바위가 부딪친 상황
    if (py < ry + rh) and (px < rx + rw) and (px + pw > rx):
        pad.blit(exp,(rx,ry))
        rock_init() 

    if len(mlist) != 0: # 발사된 미사일이 있을때
        for mis in mlist:
            mis[1] -= 20
            # 운석과 미사일이 충돌
            if mis[1] < ry + rh and (mis[0] < rx + rw) and (mis[0] + mw > rx):
                pad.blit(exp,(rx, ry))
                mlist.remove(mis)
                rock_init()
            elif mis[1] < -50:
                mlist.remove(mis)

            pad.blit(m,(mis[0],mis[1]))
    
    write("Scores: ",10,10,white)
    pygame.display.update()
    clock.tick(60)

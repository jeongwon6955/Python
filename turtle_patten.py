from turtle import * # turtle 모듈을 임포트하여 그래픽을 그릴 수 있도록 함

# 펜 색상 설정: 선 색상은 빨간색, 채우기 색상은 노란색
# color('red','yellow')

# # 도형 채우기 시작
# begin_fill()

# # turtle의 속도를 가장 빠르게 설정 (0이 가장 빠름)
# speed(0)

# # 무한 루프를 통해 도형을 그리는 코드
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1: # 터틀의 현재 위치가 원점에 가까워지면 종료
#         break

# # 도형 채우기를 마무리
# end_fill()

# # 그래픽 창을 유지하며 종료
# done()

# bgcolor('gray')
# speed(0)

# color('#4f0111', 'black')
# begin_fill()

# while True:
#     forward(5)
#     right(1)
#     circle(7500)
#     if abs(pos()) < 1:
#         break

# end_fill()
# done()


speed(0)

color('black', 'red')

begin_fill()

while True:
    forward(100)
    left(100)
    circle(600)
    if abs(pos()) < 1:
        break

end_fill()
done()
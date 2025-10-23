import turtle as t
import random as r

# 1. 다각형 그리기
# n = int(input('몇각형을 그릴까요?'))

# for i in range(1,n+1):
#     t.forward(100)
#     t.left(360/n)

# 2. 이중 반복문 다각형 그리길 입력한 각형에서 -> 3각형 까지

# n = int(input('몇각형부터 그릴까요? '))

# for i in range(n,2,-1): # 그릴 각형 8 7 6 5 4 3각형
#     for j in range(i): # 8각형 - 8번 반복
#         t.forward(100)
#         t.left(360/i)

# 3. 이중 반복문 다각형 색칠하기

# color_list = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'gray', 'brown', 'navy', 'black']
# n = int(input('몇각형부터 그릴까요? ')) # 최대 8각형 이하

# for i in range(n,2,-1):
#     t.color(color_list[i])
#     t.begin_fill()
#     for j in range(i):
#         t.forward(100)
#         t.left(360/i)
#     t.end_fill()

# 4. 이중 반복문 다각형 랜덤 색칠하기

# color_list = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'gray', 'brown', 'navy', 'black']
# n = int(input('몇각형부터 그릴까요? ')) # 11

# for i in range(n,2,-1):
#     t.color(r.choice(color_list))
#     t.begin_fill()
#     for j in range(i):
#         t.forward(100)
#         t.left(360/i)
#     t.end_fill()

# 5. 색깔이 중복되지 않도록 그리기 리스트 변수에서 값 제거하는 방법 remove
# color_list 갯수만큼만 다각형 13각

color_list = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'gray', 'brown', 'navy', 'black']
n = int(input('몇각형부터 그릴까요? ')) # 11

for i in range(n,2,-1): # 8
    t_color = r.choice(color_list)
    t.color(t_color)
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()
    color_list.remove(t_color)

t.done()

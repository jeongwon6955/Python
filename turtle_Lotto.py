# Lotto 번호 생성기
import random
import turtle as t
t.speed(10) # 0 ~ 10
t.bgcolor('#000')
t.pensize(1)

# 로또번호 공이 통안에 있어요
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]

numbers = []
for i in range(1,46): # i 값: number 삽입
    numbers.append(i)
    # print(numbers)

random.shuffle(numbers) # 공 섞기

num1 = numbers[1]
num2 = numbers[2]
num3 = numbers[3]
num4 = numbers[4]
num5 = numbers[5]
num6 = numbers[6]
# bonus = numbers[7]

print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
# print(bonus)

t.shape('turtle')
t.hideturtle()
t.color('#fff')
t.penup()
t.goto(0,150)
t.pendown()
t.write('Random Lotto', align= 'center', font=('impact',90,'bold'))

color = ['red', 'blue', 'green', 'yellow', 'gray', 'navy', 'purple', 'orange']

# 첫번째 공 그리기
# t.penup()
# t.goto(-500,-100)
# t.color[color[0]]
# t.begin_fill()
# t.pendown()
# t.circle(70,360)
# t.end_fill()
# t.color('#fff')
# t.write(f'{num1}', align= 'center', font=('impact',70,'bold'))

# # 두번째 공 그리기
# t.penup()
# t.goto(-300,-100)
# t.pendown()
# t.circle(70,360)
# t.write(f'{num2}', align= 'center', font=('impact',70,'bold'))

# # 세번째 공 그리기
# t.penup()
# t.goto(-100,-100)
# t.pendown()
# t.circle(70,360)
# t.write(f'{num3}', align= 'center', font=('impact',70,'bold'))

# # 네번째 공 그리기
# t.penup()
# t.goto(100,-100)
# t.pendown()
# t.circle(70,360)
# t.write(f'{num4}', align= 'center', font=('impact',70,'bold'))

# # 다섯번째 공 그리기
# t.penup()
# t.goto(300,-100)
# t.pendown()
# t.circle(70,360)
# t.write(f'{num5}', align= 'center', font=('impact',70,'bold'))

# # 여섯번째 공 그리기
# t.penup()
# t.goto(500,-100)
# t.pendown()
# t.circle(70,360)
# t.write(f'{num6}', align= 'center', font=('impact',70,'bold'))

# for문 활용
x = -500
for i in range(1,7):
    t_color = random.choice(color)
    t.penup()
    t.goto(x,-100)
    t.pendown()
    t.color(t_color) # 공 색깔
    t.begin_fill()
    t.circle(70,360)
    t.end_fill()
    t.color('#fff')
    t.write(f'{numbers[i]}', align= 'center', font=('impact',70,'bold'))
    x = x + 200
    color.remove(t_color)
    
t.done()
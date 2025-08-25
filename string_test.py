""" import math

# 입출력함수 문자열 활용하기
# input() print()

# 비만도 (BMI) 구하기
# 비만도 = 몸무게 / (키의 제곱) * 1000

height = int(input("키 입력: "))
weight = int(input("몸무게 입력: "))
bmi = weight / math.pow(height, 2) * 10000

if(bmi < 18.5):
    result = "저체중"
elif(bmi < 23):
    result = "정상체중"
elif(bmi < 25):
    result = "과체중"
elif(bmi < 30):
    result = "비만"
else:
    result = "고도비만"

print(f"당신의 비만도는 {bmi:.2f}으로 {result}입니다.")

print(type(bmi))
 """

import turtle as t

t.shape("turtle")

# 구각형 그리기
t.color("cyan")
t.begin_fill()
for i in range(9):
    t.forward(150)
    t.left(40)
t.end_fill()

# 팔각형 그리기
t.color("orange")
t.begin_fill()
for i in range(8):
    t.forward(150)
    t.left(45)
t.end_fill()

# 육각형 그리기
t.color("purple")
t.begin_fill()
for i in range(6):
    t.forward(150)
    t.left(60)
t.end_fill()

# 오각형 그리기

t.color("red")
t.begin_fill()
for i in range(5):
    t.forward(150)
    t.left(72)
t.end_fill()

# 사각형 그리기
t.color("blue")
t.begin_fill()
for i in range(4):
    t.forward(150)
    t.left(90)
t.end_fill()

# 삼각형 그리기
t.color("green")
t.begin_fill()
for i in range(3):
    t.forward(150)
    t.left(120)
t.end_fill()
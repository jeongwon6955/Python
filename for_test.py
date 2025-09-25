# 제어문 - 선택문
# 복습 주사위게임 random

# import random
# # 1부터 6까지 적힌 주사위 두개를 던져 나오는 값을a,b라고 할때

# a = random.randint(1,6) # 첫번째 주사위
# b = random.randint(1,6) # 두번째 주사위

# # if a,b 모두 홀수이면 (a의제곱 + b) 출력하시오
# # elif a,b 모두 짝수이면 절대값(a-b) 출력하시오 abs()
# # else 그외에는 2*(a+b)를 출력하시요
# print("a값: ",a)
# print("b값: ",b)

# if (a % 2 == 1 and b % 2 == 1):
#     print(pow(a,2) + b)
# elif (a % 2 == 0 and b % 2 == 0):
#     print(abs(a-b))
# else:
#     print(2*(a+b))

# 제어문 - 반복문 for while

# 1. 문자열을 이용한 반복문

# hi = "안녕하세요"

# for ch in hi:
#     print("안녕")
#     print(ch)

# hi = "안녕하세요"

# for ch in hi:
#     print(ch, end='')

# korea = "사랑하는 우리나라 대한민국"
# count = 0

# for i in korea:
#     count += 1
#     print(count)

# korea = "나는 인평자동차고등학교 AI 소프트웨어과 1학년 1반 16번 최정원입니다"

# for i in korea:
#     if(i == " "):
#         print()
#     else:
#         print(i,end='')

# 2. range() 사용한 반복

import turtle

# n = int(input('몇 각형을 그릴꺼니? '))

# for t in range(n):
#     turtle.forward(100)
#     turtle.left(360 / n)

# turtle.done()

# for i in range(3,100,3):
#     print(i, end='/')

# for i in range(5,501,5): # 5의 배수 출력 한줄로 100단위로 다음줄로 출력
#     if(i % 100 == 0):
#         print()
#     else:
#         print(i,end='/')

# for문을 이용하여 23부터 40까지 출력하시오
# for i in range(23,41,1):
#     print(i,end="/")

# for문을 이용하여 97부터 77까지 출력하시오

# for i in range(97,76,-1):
#     print(i,end="/")

n = int(input("값입력"))

for i in range(1,10):
    print(n*i)
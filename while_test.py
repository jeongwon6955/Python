# 제어문 반복문 - for while

# while 문
# 1~10까지의 합을 구하는 프로그램

# i = 1
# sum = 0

# while i<=100: # i 1 2 3 4 5 6 7 8 9 10
#     sum += i
#     i += 1
#     print('1부터 10까지의 합: ',sum)

# 3부터 15까지 출력하는 while문 작성

# i = 3

# while i<=15:
#     print(i)
#     i += 1

# => for문으로 변경

# for i in range(3,16):
#     print(i)

# while True: # 무한 반복
#     jumsu = int(input('점수를 입력하세요: ')) # 0 ~ 100
#     if (jumsu >= 0 and jumsu <= 100):
#         break
# print(f'당신의 점수는 {jumsu}점 입니다')

# 키보드로부터 숫자하나 입력받고 
# 무한반복되다가 입력된 값이 4이면 탈출하세요
# 입력된 값 출력하고 무한반복

# while True: # 무한 반복
#     i = int(input('숫자하나 입력하세요(4 입력시 종료): '))
#     if (i == 4):
#         break
#     print(f'입력된 값은 {i} 입니다')

fruit = ['사과','포도','배','참외']

# for i in fruit:
#     print(i)

# => while
i = 0
while i < len(fruit):
    print(fruit[i])
    i += 1
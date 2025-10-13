# 제어문 - 반복문 for 문자열 range 리스트변수

# 구구단 찍기

# 2단 찍기
# print('구구단 2단')
# for i in range(1,10):
#     print(f'2 * {i} = {2*i}') # 9번

# 8단 찍기
# print('구구단 8단')
# for i in range(1,10):
#     print(f'8 * {i} = {8*i}')

# 4단 홀수만 찍기
# print('구구단 4단 홀수만 출력')
# for i in range(1,10,2):
#     print(f'4 * {i} = {4*i}')

# 중복 for문
# for i in range(1,6): # i = 1 2 3 4 5
#     # print(f'i값은 {i}')
#     for j in range(1,6): # j = 1 2 3 4 5
#         print("잘 지냈니? ") # 25

# 구구단 2단 ~ 9단 세로 출력
# print('구구단 출력하기')
# for i in range(2,10): # 단 8번
#     print()
#     print(f'구구단 {i}단')
#     for j in range(1,10): # 곱하는 수 9번
#         print(f'{i} * {j} = {i*j}') #72번 반복

# 구구단 2단 ~ 9단 가로 출력
# print('구구단 출력하기')
# for i in range(2,10): # 단 8번
#     print()
#     print(f'구구단 {i}단')
#     for j in range(1,10): # 곱하는 수 9번
#         print(f'{i} * {j} = {i*j:>2}  ',end='') #72번 반복
#     print()

# 출력 포매팅 정렬하기

# name = '최정원'
# print(f'{name:<10}') # 왼쪽정렬
# print(f'{name:>10}') # 오른쪽정렬
# print(f'{name:^10}') # 가운데정렬

# 구구단 2단 ~ 9단 1단씩 세로 출력
# print('구구단 출력하기')
# for i in range(1,10): # 단 8번
#     for j in range(2,10): # 곱하는 수 9번
#         print(f'{j} * {i} = {i*j:>2}  ',end='') #72번 반복
#     print()

# for i in range(1,6):
#     print('*'*i)

for i in range(1,6):
    print()
    for j in range(1,6):
        if(i >= j):
            print('*',end='')
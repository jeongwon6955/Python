# 함수 자주 사용하는 기능을 함수로 정의 호출해서 사용
# 1.내장함수 : 이미 만들어져 있고, 파이썬 포함
# 2.사용자 정의 함수 : def 으로 정의 만들어주어야함 호출
# 3.라이브러리 함수 : import turtle random

# return 값이 있는 함수

# def say():
#     return 'HI'
# a = say()
# print(a)

# 두 수를 더하여 더한값을 리턴하는 함수 작성
# 출력문 3과 5의 합은 8 입니다
# add_num 함수 작성

# def add_num(i,j): # 매개변수
#     return(i+j)

# a = 3
# b = 5
# c = add_num(a,b)
# print(f'{a}와 {b}의 합은 {c} 입니다')

# 두 수를 입력받아 더하는 계산기

# a = int(input('첫 번째 수를 입력하세요: '))
# b = int(input('두 번째 수를 입력하세요: '))
# c = add_num(a,b)
# print(f'{a}와 {b}의 합은 {c} 입니다')

# 사칙연산 계산기
# def add_num(i,j):
#     return (i+j)

# def sub_num(i,j):
#     return (i-j)

# def mul_num(i,j):
#     return (i*j)

# def div_num(i,j):
#     return (i/j)

# print("@@@사칙연산 계산기@@@")
# num1 = int(input('계산할 첫번째 수: ')) 
# num2 = int(input('계산할 두번째 수: ')) 

# op_code = input('연산자를 선택하세요 (+, -, *, //): ')

# if op_code == '+':
#     result = add_num(num1,num2)
#     print(f'{num1}과 {num2}의 합은 {result}입니다')
# elif op_code == '-':
#     result = sub_num(num1,num2)
#     print(f'{num1}과 {num2}의 뺄셈은 {result}입니다')
# elif op_code == '*':
#     result = mul_num(num1,num2)
#     print(f'{num1}과 {num2}의 곱은 {result}입니다')
# elif op_code == '//':
#     result = div_num(num1,num2)
#     print(f'{num1}과 {num2}의 몫은 {result}입니다')
# else:
#     print('다시 입력해주세요')

# 리스트 변수 score에 있는 학생성적을 넘겨받아
# 총점, 평균, 최고점수, 최저점수를 리턴하는 함수 작성
def scoreFunc(scoreList): # 성적처리 함수 작성
    total = sum(scoreList) # 총점
    avg = total/len(scoreList) # 평균
    max_score = max(scoreList) # 최고점
    min_score = min(scoreList) # 최하점
    return total,avg,max_score,min_score

scores = [85, 92, 78, 95, 88, 95, 72, 16, 55, 80, 90, 99, 100, 70, 65, 66, 82, 71]
total,avg,max_score,min_score = scoreFunc(scores)

print('총점: ',total)
print('평균: ',avg)
print('최고점: ',max_score)
print('최저점: ',min_score)

print('입력한 점수: ', scores)
print('전체학생수: ', 18, '명')
# 제어문 연습(중첩 if문) - 놀이동산 요금계산
# 주간, 야간, 대인, 소인, 요금 구분하기

# k = int(input('구분: 1.주간 2.야간?'))
# m = int(input('대상: 1.대인 2.소인?'))
# pay = 0

# if(k == 1):
#     if(m == 1):
#         pay = 5
#     else:
#         pay = 4
# else:
#     if(m == 1):
#         pay = 3
#     else:
#         pay = 2

# print(f'당신의 입장료는 {pay}만원입니다')

# 주간 대인 50000 주간소인 40000
# 야간 대인 30000 야간소인 20000
# 출력결과: 당신의 입장료는 000원입니다.


# for반복문
# 3. 리스트 변수 이용한 반복문
# fruit = ['apple', 'grape', 'orange', 'banana']
# # print(fruit[2])
# count = 0

# for f in fruit: # 리스트변수의 갯수 만큼 반복
#     print(f)
#     count += 1
#     print(count)
# print(fruit)

# n = [0,1,2,3,4]
# for i in n:
#     print('hello')

# # tuple변수를 이용한 반복
# food = ('치킨', '피자', '햄버거', '보쌈')
# print(type(food))

# for f in food:
#     print(f)

# # 리스트 변수안에 있는 정수 값이 홀수 인지 짝수인지 판별하는 코드를 작성하시오

# # 00는 짝수입니다 or 00는 홀수입니다

# number = [273,103,5,32,65,9,72,880,99,58]

# for n in number: # n변수에 순서대로 값이 들어온다
#     if(n%2 == 0):
#         print(f'{n}는 짝수입니다')
#     else:
#         print(f'{n}는 홀수입니다')

# 자릿수 273은 3자리수입니다

# for n in number: # n변수에 순서대로 값이 들어온다
#     print('{}는 {}자리수입니다'.format(n,len(str(n)))) # print(f'{n}는 {len(srt(n))}자리수입니다)

# # 5명의 정보처리 기능사 자격증 필기 점수가 리스트에 담겨있습니다.
# # 이때 각 점수가 합격 점수 인지 불합격 점수인지 판별하여 출력하시오.(60점 이상 합격)

# score_list = [98,58,65,78,84]

# # 1번 학생은 98점으로 합격입니다

# count = 0
# sum_score = 0

# for score in score_list:
#     sum_score += score # 총점

#     count += 1
#     if(score >= 60):
#         print(f'{count}번 학생은 {score}점으로 합격입니다')
#     else:
#         print(f'{count}번 학생은 {score}점으로 불합격입니다')

# print(f'총점은 {sum_score} 입니다')  # print(sum(score_list))

# for 반복문 1.문자열 2.range() 3.리스트변수

# range()함수를 이용한 반복
# 1~10까지의 합을 구하시오

hap = 0
mul = 1
for n in range(1,11):
    hap += n
    mul *= n
print(f'1~10까지의 합은 {hap}입니다')
print(f'1~10까지의 합은 {mul}입니다')

# 제어문 - 조건문(선택문) if if~else if~elif~else

# 1. 단일 선택문(if)

# num = int(input('자연수 입력: '))

# if(num % 2 == 0): # 홀짝판별
#     print('*',end='')
# print(num)

# 2-1. 이중 선택문(if~else) 홀짝 판별

# num = int(input('자연수 입력: '))

# if(num % 2 == 0): # 짝수라면
#     print('짝수입니다')
# else: # 홀수라면
#     print('홀수입니다')

# 2-2 나이 판별
# 나이가 17살이상이면 '다 컸네' 그렇지 않으면 '넌 아직 어려' 출력

# age = int(input("나이 입력: "))

# if(age >= 17):
#     print('다 컸네')
# else:
#     print('넌 아직 어려')

# 2-3. 점수를 입력받아 60점 이상이면 '합격' 그렇지 않으면 '불합격' 출력

# score = int(input('점수 입력: '))

# if(score >= 60):
#     print('합격')
#     print('신난다')
# else:
#     print('불합격')
#     print('ㅜㅜ')
# print('화이팅하자')

# 3. 다중 선택문 if~elif~else
# 3-1 나이가 8세미만은 '유아' 8세이상 19세 이하 '학생' 그외에는 '성인'

# age = int(input('나이 입력: '))

# if 8 <= age <= 19: # age >= 8 and age <= 19
#     print('학생')
# elif age < 8:
#     print('유아')
# else:
#     print('성인')

# 3-2 요일별 게임조건 일요일 게임열판하기 토요일 밤새서 게임하기 else 평일 물한잔하기 => 공부시작
# today = input('오늘은 무슨요일?')

# if(today == '일요일'):
#     print('게임 열판하기', end='')
# elif(today == '토요일'):
#     print('밤새서 게임하기', end='')
# else:
#     print('물 한잔하기', end= '')
# print('-> 공부시작')

# 혼자해보기 리조트에 객실당 4명의 손님까지 무료 입장입니다. 
# 입장인원은 입력하여 입장인원이 4명 이하이면 '추가비용없습니다' 입장인원이 4명보다 많으면 '추가비용 1인당 1만원입니다' 라는 메세지를 출력하세요

total = int(input('투숙객 수를 입력하세요: '))

if(total <= 4):
    print('추가비용없습니다')
else:
    print('추가비용은 1인당 1만원 입니다')

# 입장인원이 4명보다 많으면 추가되는 1명당 1만원씩을 계산해서
# '추가비용은 00 입니다' 라는 메세지를 출력하세요
# 입장인원이 8명 초과되면 '입장인원은 최대 8명 입니다' 라고 출력하세요

total = int(input('투숙객 수를 입력하세요: '))
pri = 0

if(total <= 4):
    print('추가비용없습니다')
elif(total <= 8):
    pri = (total-4) * 10000
    print('추가비용은', pri, '입니다')
else:
    print('입장인원은 최대 8명 입니다')
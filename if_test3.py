#  제어문 - 선택문 연습 if if~else if~elif~else

# 홀짝 판별 %

# num = 66

# if num % 2 == 0:
#     print('짝수입니다') # 조건이 참일때 실행
# else:
#     print('홀수입니다')


# 리조트에 객실당 4명의 손님까지 무료 입장입니다.
# 입장 인원을 입력하여 입장인원이 4명 이하이면 "추가 비용 없습니다"
# 입장 인원이 4명보다 많으면 "추가비용 1인당 1만원입니다"라는 메시지를 출력

# total = 6

# if total <= 4:
#     print('추가비용이 없습니다')
# else:
#     print('추가비용 1인당 1만원입니다')

# 변경) 4명이 넘으면 추가비용이 1인당 만원 8명이 넘으면 최대 입장인원은 8명 입니다
# 5명:1만원 6명:2만원 7명:3만원 8명:4만원

# total = 9

# if total <= 4:
#     print('추가비용이 없습니다')
# elif total == 5:
#     print('추가비용은 1만원 입니다')
# elif total == 6:
#     print('추가비용은 2만원 입니다')
# elif total == 7:
#     print('추가비용은 3만원 입니다')
# elif total == 8:
#     print('추가비용은 4만원 입니다')
# else:
#     print('최대 입장인원은 8명 입니다')

# 간소화

# total = 9

# if total <= 4:
#     print('추가비용이 없습니다')
# elif 4 < total <= 8:
#     print(f'추가비용은 {total-4}만원 입니다')
# else:
#     print('최대 입장인원은 8명 입니다')

# 소숫점 표현 round() 출력 포매팅
# round()

# print(round(5.6666,2)) # 5.67
# print(round(5.25783,4)) # 5.2578
# print(type(round(5.7777,0))) # 6.0
# print(type(round(5.7777))) # 6

# # 출력 포매팅
# print('{:.2f}'.format(3.5555)) # 3.56
# print('{:.3f}'.format(3.2567)) # 3.257
# print('{:.0f}'.format(3.5555)) # 4

# print('{0}과{0}'.format(3.5555, 3.7777))
# print('{1:.2f} 과 {0:.3f}'.format(3.5556, 3.7777))

# money = int(input('가지고 있는 돈은 얼마인가요? '))
# if money >= 20000:
#     print('탕수육 먹어요')
# elif money >= 10000:
#     print('쟁반짜장 먹자')
# elif money >= 6000:
#     print('해물짬뽕 어때')
# elif money >= 4000:
#     print('짜장면 먹지뭐')
# else:
#     print('단무지나 먹어야겠다')

# scores = [85, 92, 78, 95, 88]

# print('입력된 점수: ', scores)
# print('전체학생수: ', len(scores), '명')
# if len(scores) > 0:
#     max_score = max(scores)
#     min_score = min(scores)
#     tot_score = sum(scores)
#     avg_score = sum(scores) / len(scores)
#     print('최고 점수: ',max_score,'점')
#     print('최저 점수' ,min_score,'점')
#     print('총합 점수:' ,tot_score,'점')
#     print("평균 점수" ,'{:.2f}'.format(avg_score))
# else:
#     print('입력된 점숙가 없습니다')

# 점수에 따른 학점 판단

score = int(input('당신의 점수는? '))

if score >= 90:
    print('A학점입니다')
elif score >= 80:
    print('B학점입니다')
elif score >= 70:
    print('C학점입니다')
elif score >= 60:
    print('D학점입니다')
else:
    print('F학점입니다')
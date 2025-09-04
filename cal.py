# 예약어 변수명
import keyword
import datetime
import calendar

# 달력 보기
print(calendar.month(2009,4))


# 예약어 확인
# print(keyword.kwlist)

# today = datetime.date.today()
# print(today.year)
# print(today.month)
# print(today.day)
# print("오늘은",today.year,"년",today.month,"월",today.day,"일 입니다")

# now = datetime.datetime.now()
# print(now)

# print(f"지금은 {now.hour}시 {now.minute}분 {now.second}초 입니다")

# 이스케이프문 복습
# food = 'Python\'s favorite food is per!'
# say =  '\"Python is very easy.\" he says.'

# print(food)
# print(say)

# upper() lower() title()
# food변수 값 대문자로 출력하세요

# print(food.upper())

# say변수값 소문자로 출력하세요

# print(say.lower())

# print(say.title())

# calculator 계산기 만들기

# num1 = int(input("첫 번째 값 받기: "))
# num2 = int(input("두 번째 값 받기: "))
# add_result = num1 + num2
# sub_result = num1 - num2
# mul_result = num1 * num2
# div_result = num1 / num2
# print("덧셈결과: %d"%(add_result))
# print("뺄셈결과: %d"%(sub_result))
# print("곱셈결과: %d"%(mul_result))
# print(f"나눗셈결과: {round(div_result,2)}")

# round 반올림

# pi = 3.9465966535
# print(round(pi,2)) # 소숫점 두째자리까지 출력(세째자리에서 반올림)
# print(round(pi))
# print(round(pi,5))
# print(round(pi,0))
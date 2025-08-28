# 표준 함수

# 여러줄의 문자 입력 '''
profile = '''1.성명: 최정원
2.소속: 인평자동차고등학교
3.취미: 코딩
4.특기: 끈기'''

# print 포맷팅
name = '최정원'
age = 17
print('내 이름은', name, '입니다')
print('내 나이는', age, '입니다')

print('이름:',name,' 나이:',age)
print('이름: %s, 나이: %d'%(name,age))
print('이름: {}, 나이: {}'.format(name,age))
print(f'이름: {name}, 나이: {age}')

a = 13
print('%o'%(a))
print('%x'%(a))

# print(name * 100)

# len() - 문자열의 길이를 구함 (공백 포함)

profile = '''1.성명: 최정원
2.소속: 인평자동차고등학교
3.취미: 코딩
4.특기: 끈기'''
name = '1. 최 정 원'
print(len(profile))
print(len(name))

# max() - 제일 큰 값, min() - 제일 작은 값
a = '1234'
print(max(a))
numbers = [1, 5, -2, 0, 6]
print('가장 큰 값은%d입니다'%(max(numbers)))
print('가장 큰 값은%d입니다'%(min(numbers)))

# 합계구하기 sum()
print('합계는%d입니다'%(sum(numbers)))
print('평균는%d입니다'%(sum(numbers)/len(numbers)))

# 제곱구하기 pow()
print('2의 3승은%d'%(pow(2,3))) # print(2**3)

# 알파벳을 lower() - 소문자로 upper() - 대문자로
a = 'I Love Python'
print(a.upper())
print(a.lower())

# join() 구분자 넣기
s1 = ['Hello', 'Python', '!']
s2 = '@'.join(s1)
print(s2)
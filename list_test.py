# 리스트 변수 [] 여러개의 값 저장, 변경 가능
# h = ['lee', 17, 172.5, True]
# i = []

# print(type(h))
# print(type(i))

# c = h[1] + h[2]

# print(type(c))


# singer = ['카리나', '윈터', '안유진', '설윤', '송하영', '아이유']

# print(singer)

# append() 값 추가

# singer.append('지드래곤')
# print(singer)

# singer.append('오해원')
# print(singer)

#remove() 값 삭제

# singer.remove('윈터')
# print(singer)

# singer.remove('설윤')
# print(singer)

# ['카리나', '안유진', '송하영', '아이유', '지드래곤', '오해원']

# insert() 값 삽입 원하는 위치에
# singer.insert(2, '제니')
# print(singer)

# pop() 원하는 위치에 값 삭제 4번지 값 삭제
# singer.pop(4)
# print(singer)

# singer.pop(1)
# print(singer)

# singer.pop(2)
# print(singer)

# singer.clear() # 모두 지우기
# print(singer)

# singer.insert(2, '제니')
# print(singer)
# print(singer[0])

# fruit = ['사과', '참외', '수박', '레몬', '오렌지']

# print(type(fruit))
# fruit.append('두리안')
# fruit.remove('레몬')
# fruit.pop(3)
# fruit.insert(2, '포도')
# print(fruit)

# sort()

# fruit.sort()
# print(fruit)

# score = [90.2, 78.6, 89.5, 67.8, 60.2, 99.5, 53.2]

# score.sort(reverse=True)
# print(score)

# random() 함수 
import random

x = random.random  # 0이상 1미만의 난수 생성
print(x)

x = [1,2,3,4,5,6,7,8]
random.shuffle(x) # shuffle 값 섞기
print(x)

y = random.choice(x) # choice 1개 선택
z = random.sample(x,3) # sample 정해진 갯수 만큼 뽑기

print(z)

num = random.randint(1,18)

print(num)

num = random.randint(1,18)

print(num)


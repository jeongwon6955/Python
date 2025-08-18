# 입출력문 연습 - print input
# 한줄 주석 ''' ''' """ """ 여러줄 주석
'''
print("hello world!!")

print("hello world!!")

print("hello world!!")

message = "최정원"
h1 = 안녕하세요 저는 인평자동차고등학교에 재학중인 최정원이라고 합니다.

print(message)
print(h1)


# 변수만들기 - 자료형의 이해
a = 4 # 정수
b = 2.5 # 실수
c = "hello" # 문자열
d = True # 논리

print("a변수에 들어있는 값은", b,"입니다")

print(a)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

name = input("이름을 입력하세요: ") # 키보드로 부터 입력

print("입력하신 이름은", name, "입니다")

age = input("나이를 입력해주세요: ")

print("입력하신 나이는", age,"살 입니다")

# 이름과 나이를 입력 받고 결과가
# 제이름은 000이고 나이는 00살 입니다

print("제이름은", name,"이고", "나이는", age,"살 입니다")
print("이름은", name,"이고 나이는", age,"살 입니다")
'''
# 두 수의 덧셈(키보드로부터 수를 입력 받기)

a = int(input("첫번째 수 입력: ")) # 캐스트 연산
b = int(input("두번째 수 입력: "))
c = a + b
print("두수의 합:", c)
print(type(a))
print(type(b))
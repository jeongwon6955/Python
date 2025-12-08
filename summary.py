# 2회 고사 대비
'''
1. 주석처리 # ''' ''' """ """ p134
2. 변수 p63
3. 문자열 함수 p74 len() max() min() lower() upper() split()
4. input() 키보드로부터 입력
    num = input("정수하나를 입력하세요: ") # type string
    => num = int(input("정수하나를 입력하세요: ")) # type int
    a = 10 # type int
    str(a) = > 10은 문자열로 바뀐다 캐스트 연산자(자료형 변환 연산자)
5. 리스트변수 p76
    여러개의 값 저장, 다른 자료형 저장 가능, [], 변경할 수 있다(변경, 추가, 삭제, 수정)

    color = ["red", "black", "yellow"]
    값 추가 color.append("blue")
    값 삽입 color.insert(1, "white")
    값 삭제 remove() pop() del() # del color[2]
6. 이스케이프 문자 진달래꽃 \ 사용 p109
7. 연산자 p113
    산술연산자 + - * / // %
    비교연산자 > < >= <= != ==
    논리연산자 and or not
    대입연산자 =
    우선순위 (), 산술, 비교, 논리
8. range(시작값, 끝값, 증감) 함수 p77
    range(5,20,3) # 5, 8, 11, 14, 17
9. 함수 p158 내장함수 사용자정의함수 라이브러리함수
    사용자 정의 함수 p164
    def 호출

    def sum(a,b): # 매개변수
        return a+b

    result = sum(55,70) # 인수
10. 파일처리

# 수행 평가-----------------------

홀짝 판별 프로그램 작성

# 홀짝 판별 프로그램 작성
num = int(input("한개의 정수 입력: "))
 
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 구구단 출력
for i in range(1,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")

# 
num2 = 0

while True:
    num2 += 1
    print(num2)
    if num2 >= 5:
        break
'''

# global 변수
num3 = 3
def func(n):
    global num3
    num3 = n * 3

func(num3)
print(num3)
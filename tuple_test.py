# 컨테이너 변수(시퀀스 자료형) - 배열
# 리스트 튜플 문자열 딕셔너리
# 리스트 - 여러개의 값, 수정, []

# 튜플변수 - 값 수정 안됨 ()
# t1 = (1,2,3)
# print(type(t1))

# t2 = tuple(range(101))
# print(t2)

# t1 = t1 + t2
# print(t1)

# t2.append(10) 값 추가 불가

# color = ("red", "black", "blue", "yellow")
# color.pop("red") 값 삭제 불가

# print(color[2]) # blue
# print(color[1:3]) # black blue
# print(color[1::2]) # black yellow

# print(t2)

# print(t2[3::3])
# print(t2[50::5])
# print(t2[50::-5])
# print(t2[::-5])

# print("black" in color)
# print("blue" not in color)

# 패킹 언패킹
# fruit = ("수박", "참외", "딸기", "복숭아") # 패킹(묶기)

# f1,f2,f3,f4 = fruit # 언패킹(풀기)
# print(type(f1))
# f1,*other,f2 = fruit
# print(f1,f2)
# print(other)

# num = tuple(range(10))

# print(num)

# n1,n2,*ot = num

# print(n1,n2)
# print(ot)

# n1,n2,*other,n3 = num

# print(n1,n2,n3)
# print(other)

# 딕셔너리 자료형 {}

dic = {"kor":80, "eng":92, "mat":77}
print(dic)

print(dic["kor"])

print("mat" in dic)

dic.setdefault("music",100) # 딕셔너리 변수 값 입력

print(dic)

dic.pop("eng") # pop 값 삭제

print(dic)

del dic["kor"] # del 값 삭제

print(dic)

dic.clear()

print(dic)

del dic
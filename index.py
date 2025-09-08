import random

while True:
 a = random.randint(1,6)
 b = random.randint(1,6)
 c = random.randint(1,6)
 d = random.randint(1,6)
 e = random.randint(1,6)

 user_input = input('주사위를 굴리려면 1를 눌러주세요')

 if user_input == "1":
    print(a,b,c,d,e)
    break
 else:
    print('입력값이 1이 아닙니다')
# 예외처리 try~except

'''
str = "89점"

try:
    score = int(str)
    print(str)
except:
    print("예외가 발생했습니다")
'''

try:
    print(name)
except NameError:
    print('변수가 선언되지 않았습니다')
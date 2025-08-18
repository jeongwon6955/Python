import random

paper = 1
rock = 2
scissors = 3

computer = random.randint(1,3)

input("가위 바위 보")
while True:

  if(rock and paper and scissors == computer):
      print("비겼습니다")
  elif(rock < computer or paper+1 == computer or scissors-1 > computer):
      print("이겼습니다")
  elif(rock > computer or paper+1 < computer or scissors-1 == computer):
      print("졌습니다")
  break
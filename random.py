# print('hello world')
# print('hello')
# 주사위게임
import random

print("🎲 주사위 게임에 오신 것을 환영합니다! 🎲")

while True:
    input("주사위를 굴리려면 엔터를 누르세요...")
    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print(f"당신의 주사위: {player_roll}")
    print(f"컴퓨터의 주사위: {computer_roll}")

    if player_roll > computer_roll:
        print("🎉 당신이 이겼습니다!")
    elif player_roll < computer_roll:
        print("😢 컴퓨터가 이겼습니다!")
    else:
        print("🤝 무승부입니다!")

    again = input("다시 하시겠습니까? (y/n): ").strip().lower()
    if again != "y":
        print("게임을 종료합니다. 감사합니다!")
        break
import random

def start_game():
    print("=" * 30)
    print("나만의 숫자 맞추기 게임!")
    print("1부터 100 사이의 숫자를 맞춰보세요.")
    print("=" * 30)

    # 1~100 사이의 난수 생성
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("숫자를 입력하세요: "))
            attempts += 1

            if guess < secret_number:
                print("더 큰 숫자입니다! ↑")
            elif guess > secret_number:
                print("더 작은 숫자입니다! ↓")
            else:
                print(f"축하합니다! {attempts}번 만에 맞추셨습니다! 🎉")
                break
        except ValueError:
            print("올바른 숫자를 입력해 주세요.")

if __name__ == "__main__":
    start_game()

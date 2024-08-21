import random

# ユーザーから最小値と最大値を取得
min_number = int(input('What is minimum number??\n'))
max_number = int(input('What is maximum number??\n'))

# 指定された範囲で乱数を生成
random_number = random.randint(min_number, max_number)

# ユーザーが正解するまで繰り返す
while True:
    guess = int(input(f'Guess a number between {min_number} and {max_number}: '))
    
    if guess < min_number or guess > max_number:
        print(f'Please enter a number between {min_number} and {max_number}.')
    elif guess < random_number:
        print('Too low! Try again.')
    elif guess > random_number:
        print('Too high! Try again.')
    else:
        print(f'Congratulations! You guessed the right number: {random_number}')
        break

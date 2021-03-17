# Number guessing game between two player.

# secret_number = int(input(f'Enter a secret number to guess : '))
guess_limit = 3
secret_number = 10
guess_count = 0

while guess_count < guess_limit:
    guess = int(input(f'Guess the number entered  : '))
    guess_count += 1
    if guess == secret_number:
        print('Hurrey!! You Won!')
        break
else:
    print('Oops! You made three guesses but failed!')

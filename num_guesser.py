import random

def numberGame():
    number = random.randint(1,10)
    guess = input('What\'s your number guess? ')
    try:
        while True:
            if (int(guess) == number):
                print(f"You guessed it! The number was {number}")
                break
            else:
                guess = input('What\'s your number guess? ')
    except:
        print(f"Cannot guess with a type {type(guess)}")

numberGame()

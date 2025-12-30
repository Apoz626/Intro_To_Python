import random

def play():
    guess = ''
    number = random.randint(1, 5)
    found = False

    print("Guess a random number between 1 and 5")
    guess = int(input())

    while (guess != number):
        print("Try again!")
        guess = int(input())
        
    print("Congratulation! You guessed it!")

play()


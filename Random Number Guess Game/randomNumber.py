##import random
##
##def play():
##    number = random.randint(1, 5)
##
##    print("Guess a random number between 1 and 5")
##    try:
##        guess = int(input())
##
##        while (guess != number):
##            print("Try again!")
##            guess = int(input())
##            
##        print("Congratulation! You guessed it!")
##    except ValueError:
##        print('Error: You must enter a number.')
##        print('Restarting...\n')
##        play()
##
##play()

import random

def play():
    number = random.randint(1,5)

    print("Guess a number between 1 and 5" + str(number))

    while True:
        try:
            guess = int(input())
            if(guess == number):
                print("Congratulations")
                break
            else:
                print('Try again')
        except ValueError:
            print('Error: Must enter a number')
            continue

play()

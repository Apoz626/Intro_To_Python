##name = ''
##
##while name != 'your name':
##    print("Type your name")
##    name = input()
##print("Thank you")

##guess = ''
##while guess != 5:
##    print('Guess a number (hint: it is 5)')
##    guess = int(input())
##print("Got it!")

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

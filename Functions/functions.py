##def hello(name):
##    for i in range(len(name)):
##        print('Howdy ' + name + '!')
##        print('Your name has: ' + str(len(name)) + ' letters!')
##
##name = 'Dom Papaspiliopulous'
##hello(name)

def plusOne(number):
    number = number + 1
    return plusOneMore(number)

def plusOneMore(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

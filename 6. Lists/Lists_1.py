##spam = ['cat', 'bat', 'rat', 'elephant']
##
##print('the ' + spam[-1] + ' is afraid of the ' + spam[-2])


spam = [10,20,30]
print(spam)

spam[1] = 'Hello'
print(spam)

## this is a slice / starting at (not including) index 1 and UP TO
## (not includeing) 3, replace with new values
spam[1:3] = ['CAT', 'DOG', 'MOUSE']
print(spam)

print(spam[:2])
print(spam[2:])

del spam[2]

print(spam)

print(len(spam))

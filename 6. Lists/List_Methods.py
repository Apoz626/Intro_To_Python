spam = ['hello', 'hi', 'howdy', 'heyas']

print(spam.index('heyas'))

##try:
##    print(spam.index('HOWDY Partner'))
##except ValueError:
##    print('Value index does not exist')

spam.append('moose')
print(spam)

spam.insert(1, 'chicken')
print(spam)

spam.remove('howdy')
print(spam)

del spam[0]
print(spam)

spam2 = ['cat', 'cat', 'rat', 'rat']
spam2.remove('cat') ## only removes first 'cat'
print(spam2)
    
spam2 = [2, 5, 3.14, 1, -7]
spam2.sort() ## COOL
print(spam2)

spam2.sort(reverse = True) ## REVERSE COOL
print(spam2)

spam3 = ['Alice', 'Bob', 'ants', 'badgers', 'Carls', 'cats'] # ASCII sort
spam3.sort()
print(spam3)

spam3.sort(key=str.lower) ## Sets all to lowercase, sorts by alphabetical order
print(spam3)

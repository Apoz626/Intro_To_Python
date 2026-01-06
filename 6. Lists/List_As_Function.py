def eggs(someParameter): ## reference is referenced and mutated
    someParameter.append('Hell0')

spam = [1,2,3] ## reference created and stored
eggs(spam)
print(spam)

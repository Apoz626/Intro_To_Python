#### Mutable
##name = 'Zophie a cat'
##newName = name[0:7] + 'the' + name[8:12]
##print(newName)

spam = [0, 1, 2, 3, 4, 5] ## this is a REFERENCE
cheese = spam
cheese[1] = 'Hello!' ## reference changed
print(cheese) ## same list referenced
print(spam) ## same list referenced



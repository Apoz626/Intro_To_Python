import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)

cheese[1] = 42
print('Spam: ' + str(spam))
print('Cheese: ' + str(cheese))

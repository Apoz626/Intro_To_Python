import random

heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads += 1
    if i == 500:
        # set breakpoint here, code will stop here in debugger
        print('Halfway there!')
print('Out of 1000 flips, heads showed up: ' + str(heads) + ' times!')

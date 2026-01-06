##print(list(range(0, 60, 3)))

##supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
##
##for i in range(len(supplies)): ##always use 'len()'
##    print('Index: ' + str(i) + ' in supplies is: ' + supplies[i])
##

#### Multiple assignemnts
##cat = ['fat', 'orange', 'loud']
##
##size, color, disposition = cat
##
##print('Size: ' + size + '/ color: ' + color + ' / disposition: ' + disposition)

#### Switching values
a = 'AAA'
b = 'BBB'

a, b = b, a

print(a, b)

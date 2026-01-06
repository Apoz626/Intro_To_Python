myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])

print('My cat has ' + myCat['color'] + ' fur.')

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}
print(eggs == ham)

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for k in eggs.keys():
    print(k)

for k, v in eggs.items():
    print(k, v)

print('cat' in eggs.values())

##if 'color' not in eggs:
##    print(eggs['name'])

print(eggs.get('age', 0))
print(eggs.get('color', 'Not found'))

if 'color' not in eggs:
    eggs['color'] = 'black'

## SetDefault does the same thing as above
eggs.setdefault('color', 'black')
print(eggs)
    

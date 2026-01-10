import re

## greedy match
digitRegex = re.compile(r'(\d){3,5}')
print('greedy match: ' + str(digitRegex.search('1234567890')))

## non-greedy match
digitRegex = re.compile(r'(\d){3,5}?')
print('non-greedy match: ' + str(digitRegex.search('1234567890')))

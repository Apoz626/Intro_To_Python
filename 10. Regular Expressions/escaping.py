import re

## match
regex = re.compile(r'\+\*\?')
match = regex.search('I learned about +*? regex syntax')
print(match.group())

## match at least one
regex = re.compile(r'(\+\*\?)+')
match = regex.search('I learned about +*?+*?+*?+*?+*? regex syntax')
print(match.group())

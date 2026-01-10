import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'

phonNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = phonNumRegex.search(message)

print(match.group())
print(phonNumRegex.findall(message))

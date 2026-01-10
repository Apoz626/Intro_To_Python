import re

phonNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
message = 'My number is 415-555-4242'


match = phonNumRegex.search(message)

print(match.group(1))
print(match.group(2))

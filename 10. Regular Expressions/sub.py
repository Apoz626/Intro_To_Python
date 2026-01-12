import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
## using sub
print(namesRegex.sub('Redacted', 'Agent Alice-alice gave the secret documents to Agent Bob'))

## one word chars for group 1 after Agent followed by 0 or more word chars
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

## sub with same thing, use raw string to get rid of \
print(namesRegex.sub(r'Agent \1*****', 'Agent Alice gave the secret documents to Agent Bob.'))

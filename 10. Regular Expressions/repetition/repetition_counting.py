import re

##batRegex = re.compile(r'Bat(wo)?man')
##match = batRegex.search('The Adventures of Batwoman')
##
##print(match.group())

## Area code checking
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
print(phoneRegex.search('My phone number is 555-1234'))

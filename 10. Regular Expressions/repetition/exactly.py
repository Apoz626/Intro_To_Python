import re

## find 'Ha' exactly 3 times
haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said "HaHaHa"'))

### exactly 3 phone numbers that can be separated my ', ' or ' '
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?( )?){3}')
print(phoneRegex.search('My numbers are 415-555-2933 404-203-3939, 403-222-3333'))

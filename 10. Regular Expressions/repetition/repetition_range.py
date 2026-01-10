import re

## find 'Ha' at least 3 - 5 times
haRegex = re.compile(r'(Ha){3,5}')
print(haRegex.search('He said "HaHaHaHaHa"'))

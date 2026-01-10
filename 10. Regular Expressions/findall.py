import re

## creates 3 groups per each phone number found 1.(full) 2(area) 3(rest)
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
resume = '''Anthony Positano Cell: 630-304-3020 / Office: 488-383-3838'''

print(phoneRegex.findall(resume))

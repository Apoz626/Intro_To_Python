import pprint

message = 'It was a bright cold day in April, and the clocks were stricking thirteen.'
count = {} #'r': 12

for character in message.upper():
    count.setdefault(character, 0) #if character isn't already in count
    count[character] = count[character] + 1
    
##pprint.pprint(count)
pretty = pprint.pformat(count)
print(pretty)

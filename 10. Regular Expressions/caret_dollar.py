import re

## 'Hello must be at beginning of string
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
print(beginsWithHelloRegex.search('He said Hello!'))

## 'world!' must be at end of string
beginsWithHelloRegex = re.compile(r'world!$')
print(beginsWithHelloRegex.search('Hello world!'))

## 1 or more digits must be at the beginning AND end of string
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('23888487757829')) ## counts
print(allDigitsRegex.search('2388848x7757829')) ## doesn't count

## '.at' says that '.' can be anything followed by 'at'
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

## one or two chars followd by 'at'
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

## Look for 'First Name: ', and 'Last Name: ', and take everything else / greedy
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Anthony Last Name: Positano'))

## non greedy / as little as possible
serve = re.compile(r'<(.*?)>')
print(serve.findall('<To serve humans> for dinner.>'))

## greedy / takes the first '>'
serve = re.compile(r'<(.*)>')
print(serve.findall('<To serve humans> for dinner.>'))

## take all before new line
dotStar = re.compile(r'.*')
print(dotStar.search('Serve the public trust.\nProtect the innocent.\nUphold the law.'))

## take everything including new lines
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search('Serve the public trust.\nProtect the innocent.\nUphold the law.'))

## finall vowels
vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))

## case insensitive matching with 're.I'
vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))

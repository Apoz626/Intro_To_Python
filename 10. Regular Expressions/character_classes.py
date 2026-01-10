import re

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

## look for 1 or more number followed by a space followed by 1 or more word characters
songRegex = re.compile(r'\d+\s\w+')
print(songRegex.findall(lyrics))

## character class
vowelRegex = re.compile(r'[aeiou]') ## r'a|e|i|o|u'
print('Custom character class: ')
print(vowelRegex.findall(lyrics))

## match 2 vowels in a row in the same word
vowelRegex = re.compile(r'[aeiouAEIOU]{2}') ## r'a|e|i|o|u'
print('Number match character class: ')
print(vowelRegex.findall('The quick brown fox jumped over the lazy dog'))

## ^[] is a negative character class | match any characters that aren't in the class
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print('Negative Character Class: ')
print(vowelRegex.findall('The quick brown fox jumped over the lazy dog'))

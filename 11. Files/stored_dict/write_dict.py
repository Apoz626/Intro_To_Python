import shelve # can store data structures in files

# open 'mydata'
shelfFile = shelve.open('mydata')

# read mydata file with stored dict
print(shelfFile['cats'])

# typecast list to read keys and values
print(list(shelfFile.keys()))
print(list(shelfFile.values()))

# must close when done
shelfFile.close()

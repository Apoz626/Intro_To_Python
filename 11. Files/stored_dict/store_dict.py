import shelve # can store data structures in files

# open 'mydata'
shelfFile = shelve.open('mydata')

# add dictionay struct to the file
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']

# must close when done
shelfFile.close()

import os

print(os.getcwd())
### reading from .txt file
##helloFile = open('C:\\Users\\tonyp\\Documents\\hello.txt')
##print(helloFile.read())
##print(helloFile.readlines())

# 'w' to open a file in write mode, 'a' for append mode (add to text at eof)
helloFile2 = open('hello2.txt', 'w')
helloFile2.write('Hello2!!!!!')
helloFile2.write('\nANOTHER LINE!!!!!!!!')

# append to existing file
helloFile3 = open('hello2.txt', 'a')
helloFile2.write('\nFrom hello3!!!')

# must close when done with file
##helloFile.close()
helloFile2.close()

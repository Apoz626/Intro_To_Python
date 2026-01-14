import os

# will join to current working directory
os.path.join('folder1', 'folder2', 'folder3', 'file.png')

# get current working directory
print(os.getcwd())

# change working directory
os.chdir('c:\\')

# absolute file path, always starts with 'c:\'
'c:\folder1\folder2\folder3'

# .\ = add to path - ..\ = go back a directory
os.chdir(r'C:\Users\tonyp\Documents\Programming\Programming_Projects\Python\Intro_To_Python\11. Files')

# get absolute path from relative file
print(os.path.abspath('files.py'))
print(os.path.abspath('..\\..\\'))

# isabs() returns true if is absolute file path
print(os.path.isabs(r'C:\Users\tonyp\Documents\Programming\Programming_Projects\Python\Intro_To_Python\11. Files'))

# gives relative path between two paths
print(os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1'))

# give dirname (preceding path)and basename (current file name)
print(os.path.dirname('c:\\folder1\\folder2\\spam.png') + '=dirname')
print(os.path.basename('c:\\folder1\\folder2\\spam.png') + '=basename')

# check if file exists
print('VBoxAudioTest.exe=' + str(os.path.exists(r'C:\Program Files\Oracle\VirtualBox\VBoxAudioTest.exe')))

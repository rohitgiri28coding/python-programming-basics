import os

path = 'C:\\Users\\DOS\\Desktop\\ZONAL MEET'

if os.path.exists(path):
    print('Location exists.')
    if os.path.isfile(path):
        print('It\'s a file')
    elif os.path.isdir(path):
        print('It\'s a directory')
    elif os.path.islink(path):
        print('It\'s a link')
else:
    print('Location does not exists')

import os

source = 'C:\\Users\\DOS\\OneDrive\\Python_Codes\\rr.txt'
destination = 'C:\\Users\\DOS\\Desktop\\moved file.txt'

try:
    if os.path.exists(destination):
        print('There is already a file.')
    else:
        os.replace(source, destination)
        print('File moved.')
except FileNotFoundError:
    print(source+' was not found')

# We can similarly move folder/dir

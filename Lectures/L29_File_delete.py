import os

try:
    os.remove('rr.txt')
except FileNotFoundError:
    print('File already deleted.')
except PermissionError:
    print('You do not have permission to delete that')

try:
    os.rmdir('f')
except FileNotFoundError:
    print('Folder already deleted')
except PermissionError:
    print('You do not have permission to delete that')
except OSError:
    print('Folder is not empty, use shutil.rmtree(path) fn to forcefully remove the dir')
else:
    print('Folder deleted')


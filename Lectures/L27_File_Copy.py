# copyfile() = copies the content of the file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata(file's creation and modification times)
# arguments = source file, destination
import shutil

shutil.copyfile('C:\\Users\\DOS\\OneDrive\\venv\\Lib\\site-packages\\pip-22.3.1.dist-info\\LICENSE.txt', 'copy.txt')
shutil.copy('C:\\Users\\DOS\\OneDrive\\venv\\Lib\\site-packages\\pip-22.3.1.dist-info\\LICENSE.txt', 'copy.txt')
shutil.copy2('C:\\Users\\DOS\\OneDrive\\venv\\Lib\\site-packages\\pip-22.3.1.dist-info\\LICENSE.txt', 'copy.txt')

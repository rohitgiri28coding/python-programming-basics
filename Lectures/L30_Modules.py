#  modules =  a file containing a python code, may contain fn, classes, etc.
#             it makes our code better organized and structured, but also give us the ability to reuse it
# Used with modular programming, which separates the program into part

# M1
import A12_Factorial

print(A12_Factorial.fact(10))

# M2
import A12_Factorial as a

print(a.fact(10))

# M3
from A12_Factorial import fact

print(fact(10))

# M4                       if there are more than one import of files and file have same fn name then
#                          it will give error. So try not using it.
from A12_Factorial import *

print(fact(10))


help('modules')         # prints the list of modules python provides


# inorder to make a python package we have to make a dir then make a __init__.py file inside it

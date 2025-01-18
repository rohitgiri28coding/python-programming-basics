# str = str[n]     ==>   returns (n+1)th letter of the str
#                  ==>   if n<0 it will return nth char from the end of the str
# str = str[m:n]   ==>   returns a str from (m+1) to (n-1)
#                  ==>   m will be inclusive and n will be exclusive
#                  ==>   if there is nothing in place of n, then it will return a str
#                                                           from (m+1)th letter to the end of the str

name = 'Rohit'
print(name)
print(name[0])     # R
print(name[-1])    # t
print(name[0:3])   # Roh
print(name[2:])    # hit
print(name[2:-1])  # hi
n = 422.45852
print('%.2f' % n)       # printing specific decimal without formatting string
age = 20
print(age)
marks = 9.2
print(str(marks) + "cgpa")
print(marks, 'cgpa')
age = age1 = age2 = 10
marks += 1
marks -= 0.2
print("Current Marks: " + str(marks) + ' cgpa')
print(type(age))
age = age + 0.8
print(age)
print(type(age))
eligible_voter = True
print(eligible_voter)
multi_line_string = '''
Hi, I am Rohit.
I am learning python.
'''
print(multi_line_string)

# Scope and Accessibility:
#
# Class Variables: Class variables are defined within a class but outside any methods.
# They are shared among all instances (objects) of the class.
# They are accessible using the class name itself or through any instance of the class.
# Instance Variables: Instance variables are specific to each instance (object) of the class.
# They are defined inside methods or the _init_() method.
# Each instance of the class has its own copy of instance variables,
# and they are accessed using the instance name.

# Memory Allocation:
#
# Class Variables: Class variables are stored in a single memory location and are shared by all
# instances of the class. When modified, the change is reflected in all instances.
# Instance Variables: Instance variables are allocated separate memory for each instance of the class.
# Each instance has its own unique set of instance variables.

# Modification:
#
# Class Variables: Class variables can be modified directly using the class name.
# When modified, the change applies to all instances of the class.
# Instance Variables: Instance variables are specific to each instance,
# and their values can be modified independently for each instance.
# Here's an example to illustrate the differences:
#
# python
# Copy code
# class MyClass:
#     class_variable = "Shared"
#
#     def _init_(self, instance_variable):
#         self.instance_variable = instance_variable
#
#
# # Class variable accessed using class name
# print(MyClass.class_variable)  # Output: Shared
#
# # Instance variables accessed using instances
# obj1 = MyClass("Instance 1")
# obj2 = MyClass("Instance 2")
# print(obj1.instance_variable)  # Output: Instance 1
# print(obj2.instance_variable)  # Output: Instance 2
#
# # Modifying class variable
# MyClass.class_variable = "Modified"
# print(obj1.class_variable)  # Output: Modified
# print(obj2.class_variable)  # Output: Modified
#
# # Modifying instance variables
# obj1.instance_variable = "Modified Instance 1"
# print(obj1.instance_variable)  # Output: Modified Instance 1
# print(obj2.instance_variable)  # Output: Instance 2
# In this example, class_variable is a class variable shared among all instances,
# while instance_variable is an instance variable specific to each instance.
# Modifying the class variable affects all instances,
# but modifying instance variables only affects their respective instances.

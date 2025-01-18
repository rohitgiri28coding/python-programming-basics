# Initialize a defaultdict with a default value of an empty list
from collections import defaultdict

my_dict_list = defaultdict(list)

# Initialize a defaultdict with a default value of a custom function
def default_value():
    return "Not Present"

my_dict_custom = defaultdict(default_value)
print(my_dict_custom['key1'])  # Output: 10
print(my_dict_custom['key2'])  # Output: 20
print(my_dict_custom['key3'])  # Output: 0 (defa
# Use these dictionaries similarly as shown in the previous example

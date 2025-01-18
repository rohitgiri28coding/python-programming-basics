first_name = "Rohit"
last_name = "Giri"
full_name = f"{first_name} {last_name} is a coder."  # Formatted string
print(full_name)

a = 'aa'
b = 'bb'
c = 'cc'
d = 'dd'
print(a, b, c, d, sep='**')


#  STRING FUNCTIONS

# Strings in python are arrays

print(len(full_name))  # Returns length og string
first_name.upper()  # Converts in uppercase
print(first_name)
print(full_name.find('i'))  # Returns index
full_name = full_name.replace('coder', 'good coder')
print(full_name)
print('Rohit' in full_name)  # Returns bool value
text = 'hi bro'
print(text.capitalize())  # Capitalize the first letter of the string: Hi bro
# isdigit,isalpha, count('char')
n = 3
print(text*n)

# slicing with string indexing

print(full_name[0:5])  # 1st is inclusive and 2nd is exclusive
print(full_name[0:10:2])  # [start:stop:step]
print(first_name[3:])  # shorthand for writing [starting_index:end_of_string]
print(first_name[::-1])  # Reverse the name
print(first_name[-1:-7:-1])      # if full name is 6 char word

# slicing with slice function

website = "https://google.com"
website_name = slice(8, -4)
print(website[website_name])  # google

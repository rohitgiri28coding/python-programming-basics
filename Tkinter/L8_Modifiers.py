# Modifiers, also known as flags or options, are settings in regular expressions that control how
# pattern matching is performed. They can change the behavior of regex patterns to make them
# case-insensitive, perform multiline matching, and more. In most regex implementations, modifiers
# are represented as single-character flags appended to the end of the regex pattern.
# Here are some common modifiers:
#
# Case Insensitive (i):
# The "i" modifier makes the pattern matching case-insensitive, meaning it will match both uppercase
# and lowercase characters.
import re

pattern = r'apple'
text = "I like Apple, AppLE, and APPLE"
result = re.findall(pattern, text, re.I)
print(f"Found matches: {result}")  # Output: Found matches: ['Apple', 'AppLE', 'APPLE']

# Multiline (m):
#
# The "m" modifier allows patterns to match the start (^) and end ($) of each line within a
# multiline string, instead of just the start and end of the entire string.

pattern = r'^apple'
text = "apple is a fruit.\nI like apples."
result = re.findall(pattern, text, re.M)
print(f"Found matches: {result}")  # Output: Found matches: ['apple', 'apple']

# Dot All (s):
#
# The "s" modifier makes the dot (.) metacharacter match any character, including newline characters.
# By default, the dot matches any character except newline.

pattern = r'.+'
text = "Line 1\nLine 2"
result = re.findall(pattern, text, re.S)
print(f"Found matches: {result}")  # Output: Found matches: ['Line 1\nLine 2']

# Verbose (x):

# The "x" modifier allows you to write more readable and well-documented regex patterns by
# ignoring whitespace and allowing comments.

pattern = r'''
   \d{3}  # Match three digits
   -      # Match a hyphen
   \d{2}  # Match two digits
'''
text = "123-45"
result = re.search(pattern, text, re.X)
print(f"Found a match: {result.group()}")  # Output: Found a match: 123-45

# Unicode (u):
#
# The "u" modifier enables Unicode matching, allowing the regex pattern to work with Unicode
# characters and properties.

pattern = r'\p{L}+'
text = "café"
result = re.findall(pattern, text, re.U)
print(f"Found matches: {result}")  # Output: Found matches: ['café']

#  Single Line (s):
#
# The "s" modifier makes the dot (.) metacharacter match any character, including newline characters.
# It's similar to "Dot All."

pattern = r'.+'
text = "Line 1\nLine 2"
result = re.findall(pattern, text, re.S)
print(f"Found matches: {result}")  # Output: Found matches: ['Line 1\nLine 2']
# These modifiers provide additional control and flexibility when using regular expressions,
# making it easier to tailor your pattern matching to specific needs.
# You can use one or more modifiers together in a single regex pattern to achieve the desired behavior.


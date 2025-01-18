# Metacharacters in regular expressions are special characters that have a special meaning or
# function within a regex pattern. Unlike literal characters, metacharacters are not matched as
# themselves but rather serve to define the structure and behavior of the pattern.
import re  # Import the regular expressions module

# Example 1: Dot (.)
# Dot (.): Matches any character except a newline.
# In Example 1, it matches any sequence ending with "at" and return the char+at
pattern = r'.at'
text = "The cat sat on the mat ccat mahacatji"
result = re.findall(pattern, text)
print(f"Found matches: {result}")  # Output: Found matches: ['cat', 'sat', 'mat', 'cat', 'cat']

# Example 2: Asterisk (*)
# Asterisk (*): Matches 0 or more occurrences of the preceding character or group.
# In Example 2, it matches "ct," "cat," "caat," and "caaat."
# [ ]* occurs 0 or more times
pattern = r'ca*t'
text = "ct, cat, caat, caaat, cbt"
result = re.findall(pattern, text)
print(f"Found matches: {result}")  # Output: Found matches: ['ct', 'cat', 'caat', 'caaat']

# Example 3: Plus (+)
# Plus (+): Matches 1 or more occurrences of the preceding character or group.
# In Example 3, it matches "cat," "caat," and "caaat."
# [ ]+ occurs 1 or more times
pattern = r'ca+t'
text = "ct, cat, caat, caaat, cbt"
result = re.findall(pattern, text)
print(f"Found matches: {result}")  # Output: Found matches: ['cat', 'caat', 'caaat']

# Example 4: Question Mark (?)
# Question Mark (?): Matches 0 or 1 occurrence of the preceding character or group.
# In Example 4, it matches "ct," "cat," and "caat."
# occurs [ ]? occurs 0 or 1 times
pattern = r'ca?t'
text = "ct, cat, caat, cbt"
result = re.findall(pattern, text)
print(f"Found matches: {result}")  # Output: Found matches: ['ct', 'cat', 'caat']

# Example 5: Square Brackets []
# Square Brackets []: Create a character class that matches any single character inside the brackets.
# In Example 5, it matches vowels.
pattern = r'[aeiou]'
text = "The quick brown fox jumps over the lazy dog"
result = re.findall(pattern, text)
print(f"Found vowels: {result}")  # Output: Found vowels: ['e', 'u', 'i', 'o', 'o', 'a', 'o', 'e', 'e', 'a', 'o']

# Example 6: Caret (^) - Matches the start of a line
# Caret (^): Matches the start of a line. In Example 6, it matches "The" only at the beginning of the text.

pattern = r'^The'
text = "The quick brown fox\nThe lazy dog"
result = re.findall(pattern, text)
print(f"Found matches: {result}")  # Output: Found matches: ['The']

# Example 7: Dollar Sign ($) - Matches the end of a line
# Dollar Sign ($): Matches the end of a line. In Example 7, it matches "dog" only at the end of the text.

pattern = r'dog$'
text = "The quick brown fox\nThe lazy dog"
result = re.findall(pattern, text)
print(f"Found matches: {result}")  # Output: Found matches: ['dog']

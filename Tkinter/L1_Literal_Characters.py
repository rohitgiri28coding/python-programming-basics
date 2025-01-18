# Literal characters in regular expressions are characters that match themselves exactly.
# This means that if you include a character in your regex pattern,
# it will look for that exact character in the text you're searching through.

import re  # Import the regular expressions module

# Example 1: Matching a single character 'a'
pattern = r'a'
text = "apple"
result = re.search(pattern, text)
if result:
    print(f"Found a match: {result.group()}")  # Output: Found a match: a

# Example 2: Matching a sequence of literal characters
pattern = r'cat'
text = "The cat sat on the mat"
result = re.search(pattern, text)
if result:
    print(f"Found a match: {result.group()}")  # Output: Found a match: cat

# Example 3: Matching a specific word
pattern = r'apple'
text = "I like apples"
result = re.search(pattern, text)
if result:
    print(f"Found a match: {result.group()}")  # Output: Found a match: apple

# Example 4: Matching a character with a metacharacter (escaping)
pattern = r'\.'
text = "This is a period."
result = re.search(pattern, text)
if result:
    print(f"Found a match: {result.group()}")  # Output: Found a match: .

# Example 5: Matching a literal backslash
pattern = r'\\'
text = "This is a backslash \\"
result = re.search(pattern, text)
if result:
    print(f"Found a match: {result.group()}")  # Output: Found a match: \

# Example 6: Matching a character in a character class
pattern = r'[aeiou]'
text = "The quick brown fox jumps over the lazy dog"
result = re.findall(pattern, text)
print(f"Found vowels: {result}")  # Output: Found vowels: ['e', 'u', 'i', 'o', 'o', 'a', 'o', 'e', 'e', 'a', 'o']

# Example 7: Matching digits in a range
pattern = r'[0-9]'
text = "The price is $25.99"
result = re.findall(pattern, text)
print(f"Found digits: {result}")  # Output: Found digits: ['2', '5', '9', '9']

# Example 8: Matching a specific word with word boundaries
pattern = r'\bapple\b'
text = "I like apple pie, but not pineapples"
result = re.search(pattern, text)
if result:
    print(f"Found a match: {result.group()}")  # Output: Found a match: apple

# Character classes, denoted by square brackets [] in regular expressions, are used to define a
# set of characters from which the regex engine can match a single character.
# They allow you to specify a range of characters that can be matched at a particular position in the text.

import re  # Import the regular expressions module

# Example 1: Matching a single character from a character class
# Single Character from a Character Class: [aeiou] matches any single vowel character in Example 1.

pattern = r'[aeiou]'  # Matches any vowel
text = "The quick brown fox"
result = re.findall(pattern, text)
print(f"Found matches: {result}")  # Output: Found matches: ['e', 'u', 'i', 'o']

# Example 2: Character class with a range
# Character Class with a Range: [0-9] matches any single digit character from 0 to 9 in Example 2.

pattern = r'[0-9]'  # Matches any digit from 0 to 9
text = "The price is $25.99"
result = re.findall(pattern, text)
print(f"Found matches: {result}")  # Output: Found matches: ['2', '5', '9', '9']

# Example 3: Character class with negation (^ inside)
# Character Class with Negation (^ inside): [^0-9] matches any character that is NOT a digit.
# The ^ inside the character class negates the set of characters to match anything except digits in Example 3.

pattern = r'[^0-9]'  # Matches any character that is NOT a digit
text = "The price is $25.99"
result = re.findall(pattern, text)
print(f"Found matches: {result}")  # Output: Found matches: ['T', 'h', 'e', ' ', 'p', 'r', 'i', 'c', 'e',
#                                                                ' ', 'i', 's', ' ', '$', '.', '']

# Example 4: Character class with multiple character ranges
# Multiple Character Ranges: [A-Za-z] matches any uppercase or lowercase letter in Example 4.

pattern = r'[A-Za-z]'  # Matches any uppercase or lowercase letter
text = "Hello World 123"
result = re.findall(pattern, text)
print(f"Found matches: {result}")  # Output: Found matches: ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']

# Example 5: Matching special characters inside a character class
# Matching Special Characters: [.$] matches either a period (.) or a dollar sign ($) in Example 5.
# When a metacharacter like the dot is placed inside a character class, it's treated
# as a literal character and doesn't have its usual special meaning.

pattern = r'[.$]'  # Matches a period (.) or dollar sign ($)
text = "The price is $25.99"
result = re.findall(pattern, text)
print(f"Found matches: {result}")  # Output: Found matches: ['$', '.']

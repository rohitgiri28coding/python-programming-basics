# Quantifiers in regular expressions specify how many times a character or a group of characters
# should be repeated. They allow you to define the quantity of characters to match in your regex pattern.

import re  # Import the regular expressions module

# Example 1: Asterisk (*) - Matches 0 or more occurrences
# Asterisk (*): Matches 0 or more occurrences of the preceding character or group.
# In Example 1, ab* matches "a," "ab," "abb," and "ab...".

pattern = r'ab*'  # Matches 'a' followed by zero or more 'b's
text1 = "a"
text2 = "ab"
text3 = "abb"
text4 = "abc"
result1 = re.search(pattern, text1)
result2 = re.search(pattern, text2)
result3 = re.search(pattern, text3)
result4 = re.search(pattern, text4)
print(f"Result 1: {result1 is not None}")  # Output: Result 1: True
print(f"Result 2: {result2 is not None}")  # Output: Result 2: True
print(f"Result 3: {result3 is not None}")  # Output: Result 3: True
print(f"Result 4: {result4 is not None}")  # Output: Result 4: True

# Example 2: Plus (+) - Matches 1 or more occurrences
# Plus (+): Matches 1 or more occurrences of the preceding character or group.
# In Example 2, ab+ matches "ab," "abb," and "ab...," but not "a."

pattern = r'ab+'  # Matches 'a' followed by one or more 'b's
text1 = "a"
text2 = "ab"
text3 = "abb"
text4 = "abc"
result1 = re.search(pattern, text1)
result2 = re.search(pattern, text2)
result3 = re.search(pattern, text3)
result4 = re.search(pattern, text4)
print(f"Result 1: {result1 is not None}")  # Output: Result 1: False
print(f"Result 2: {result2 is not None}")  # Output: Result 2: True
print(f"Result 3: {result3 is not None}")  # Output: Result 3: True
print(f"Result 4: {result4 is not None}")  # Output: Result 4: False

# Example 3: Question Mark (?) - Matches 0 or 1 occurrence
# Question Mark (?): Matches 0 or 1 occurrence of the preceding character or group.
# In Example 3, ab? matches "a" and "ab," but not "abb" or "ab...".

pattern = r'ab?'  # Matches 'a' followed by zero or one 'b'
text1 = "a"
text2 = "ab"
text3 = "abb"
text4 = "abc"
result1 = re.search(pattern, text1)
result2 = re.search(pattern, text2)
result3 = re.search(pattern, text3)
result4 = re.search(pattern, text4)
print(f"Result 1: {result1 is not None}")  # Output: Result 1: True
print(f"Result 2: {result2 is not None}")  # Output: Result 2: True
print(f"Result 3: {result3 is not None}")  # Output: Result 3: False
print(f"Result 4: {result4 is not None}")  # Output: Result 4: False

# Example 4: Curly Braces ({n} and {n, m}) - Matches exactly n or between n and m occurrences
# Curly Braces ({n} and {n, m}): Specify exact repetition or a range of repetition.
# In Example 4, a{2} matches "aa" exactly, and a{1,3} matches "a," "aa," and "aaa."

pattern1 = r'a{2}'  # Matches 'a' repeated exactly 2 times
pattern2 = r'a{1,3}'  # Matches 'a' repeated between 1 and 3 times
text1 = "aa"
text2 = "aaa"
text3 = "aaaa"
text4 = "a"
result1 = re.search(pattern1, text1)
result2 = re.search(pattern1, text2)
result3 = re.search(pattern1, text3)
result4 = re.search(pattern1, text4)
result5 = re.search(pattern2, text1)
result6 = re.search(pattern2, text2)
result7 = re.search(pattern2, text3)
result8 = re.search(pattern2, text4)
print(f"Result 1: {result1 is not None}")  # Output: Result 1: True
print(f"Result 2: {result2 is not None}")  # Output: Result 2: False
print(f"Result 3: {result3 is not None}")  # Output: Result 3: False
print(f"Result 4: {result4 is not None}")  # Output: Result 4: False
print(f"Result 5: {result5 is not None}")  # Output: Result 5: True
print(f"Result 6: {result6 is not None}")  # Output: Result 6: True
print(f"Result 7: {result7 is not None}")  # Output: Result 7: True
print(f"Result 8: {result8 is not None}")  # Output: Result 8: False


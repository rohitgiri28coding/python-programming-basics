# Anchors in regular expressions are metacharacters that specify a position within the text where a
# match should occur. They don't match any characters themselves but define the boundary conditions
# for where the regex engine should start or end a match

# Caret (^) - Start of Line Anchor:

# The caret anchor (^) is used to match the position at the beginning of a line or string.
# It asserts that the text immediately following the caret must start with the specified pattern.
import re  # Import the regular expressions module

# Example 1: Matching at the start of a line
pattern = r'^Hello'
text1 = "Hello, World!"
text2 = "Hi, Hello"
result1 = re.search(pattern, text1)
result2 = re.search(pattern, text2)
print(f"Result 1: {result1 is not None}")  # Output: Result 1: True
print(f"Result 2: {result2 is not None}")  # Output: Result 2: False

# Dollar Sign ($) - End of Line Anchor:

# The dollar sign anchor ($) is used to match the position at the end of a line or string.
# It asserts that the text immediately preceding the dollar sign must end with the specified pattern.

# Example 2: Matching at the end of a line
pattern = r'World$'
text1 = "Hello, World!"
text2 = "Hello, World! Goodbye, World!"
result1 = re.search(pattern, text1)
result2 = re.search(pattern, text2)
print(f"Result 1: {result1 is not None}")  # Output: Result 1: True
print(f"Result 2: {result2 is not None}")  # Output: Result 2: False

# Anchors are useful for enforcing specific position-based constraints in your regular expressions.
# They are often used in combination with other regex elements to ensure that a pattern is found
# only at the desired location within the text. These anchors are essential for tasks such as
# validating that a string conforms to a specific format or extracting data from structured text
# documents where patterns occur at known positions

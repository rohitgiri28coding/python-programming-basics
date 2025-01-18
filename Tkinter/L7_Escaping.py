# Escaping in regular expressions is the process of preceding a metacharacter or any character
# with a special meaning in regex with a backslash \. This allows you to treat these
# characters as literal characters, matching them in the text exactly as they are,
# rather than as part of their special regex functionality.
#
# Here are some common metacharacters and characters that often need escaping in regex:
#
# Backslash (): In regex, the backslash itself is a metacharacter used for escaping other metacharacters.
# To match a literal backslash in your text, you need to escape it with another backslash (\\).
#
# Dot (.): The dot is a metacharacter that matches any character except a newline.
# If you want to match a literal dot in your text, you should escape it as \..
#
# Asterisk (*): The asterisk is a metacharacter that specifies 0 or more repetitions of the preceding
# character or group. To match a literal asterisk, use \*.
#
# Plus (+): The plus sign is a metacharacter that specifies 1 or more repetitions of the preceding
# character or group. To match a literal plus sign, use \+.
#
# Question Mark (?): The question mark is a metacharacter that specifies 0 or 1 occurrence of the
# preceding character or group. To match a literal question mark, use \?.
#
# Square Brackets ([]): Square brackets are used to define character classes.
# To match literal square brackets, escape them as \[ and \].
#
# Caret (^): The caret is an anchor that matches the start of a line or string.
# To match a literal caret, use \^.
#
# Dollar Sign ($): The dollar sign is an anchor that matches the end of a line or string.
# To match a literal dollar sign, use \$.
#
# Pipe (|): The pipe is used for alternation, allowing you to specify multiple alternative patterns.
# To match a literal pipe, use \|.
#
# Parentheses (()): Parentheses are used for grouping and capturing. To match literal parentheses,
# use \( and \).
#
# Here's an example of escaping in regex:

import re

# Example: Matching a literal dot (.)
pattern = r'example\.com'
text = "Visit our website at example.com"
result = re.search(pattern, text)
if result:
    print(f"Found a match: {result.group()}")  # Output: Found a match: example.com

# In this example, we use example\.com to match the literal string "example.com," ensuring
# that the dot is treated as a regular character and not as the regex metacharacter for any character.

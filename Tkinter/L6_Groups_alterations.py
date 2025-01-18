# Groups and alternations are powerful features in regular expressions that allow you to create
# more complex and flexible patterns for matching and extracting text. They help you group parts
# of your pattern and specify multiple alternatives for matching. Let's explore each concept:
#
# 1. Groups (Parentheses ()):
#
# Groups are used to create sub-patterns within a larger regex pattern.
# You enclose the sub-pattern you want to group in parentheses. Groups serve several purposes:
#
# Grouping: You can use groups to apply quantifiers, metacharacters, or alternation to a specific part of the pattern.
#
# Capturing: Groups can capture and extract portions of the matched text, which can be useful for further processing.
#
# Backreferencing: You can refer back to captured groups within the same regex pattern.
#
# Here's an example using groups to match and capture email addresses:
import re

# Example: Matching and capturing email addresses
pattern = r'(\w+)@(\w+\.\w+)'
text = "Send an email to john@example.com and jane@domain.co"
matches = re.findall(pattern, text)
for match in matches:
    print(f"Full email: {match[0]}")
    print(f"Domain: {match[1]}")
# In this example, (\w+) captures the username part, and (\w+\.\w+) captures the domain part of each email address.

# 2. Alternation (Pipe |):
#
# Alternation allows you to specify multiple alternative patterns to be matched.
# It works like an OR operator. For example, (cat|dog) will match either "cat" or "dog."
#
# Here's an example using alternation to match different date formats:
# Example: Matching dates in different formats
pattern = r'\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{2}-\d{2}'
text = "Dates: 12/31/2022, 2023-01-15, 5/5/21"
matches = re.findall(pattern, text)
print(f"Found dates: {matches}")
# In this example, the alternation (pattern1|pattern2) matches dates in either "MM/DD/YYYY" or "YYYY-MM-DD" format.

# 3. Non-Capturing Groups (?:):

# Sometimes, you may want to use groups for grouping and applying quantifiers or alternation,
# but you don't want to capture the matched text. You can use non-capturing groups (?:...) for
# this purpose. Non-capturing groups are used like regular groups but without capturing the matched text.

# Example: Using non-capturing groups
pattern = r'(?:\d{1,2}/\d{1,2}/\d{4})|(?:\d{4}-\d{2}-\d{2})'
text = "Dates: 12/31/2022, 2023-01-15, 5/5/21"
matches = re.findall(pattern, text)
print(f"Found dates: {matches}")

# In this example, (?:...) is used to create non-capturing groups for date formats.
#
# Groups and alternations greatly enhance the flexibility of regular expressions,
# allowing you to build intricate patterns to match and extract the specific text
# you need from complex data. Whether you want to capture parts of the matched text
# or create patterns with multiple alternatives, groups and alternations are essential tools in regex.

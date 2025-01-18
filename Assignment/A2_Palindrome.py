entered_str = input('Enter a String: ').lower()
if (entered_str[::-1]) == entered_str:
    print(entered_str + ' is a Palindrome')
else:
    print(entered_str + ' is Not a Palindrome')

# M2

if entered_str == ''.join(reversed(entered_str)):
    print(entered_str, ' is a palindrome.')
else:
    print(entered_str, ' is not a palindrome.')

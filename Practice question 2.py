def next_letter(word):
    new_word = ''
    vowel = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
    for letter in word:
        if letter in vowel:
            new_word += chr(ord(letter)+1)
        else:
            new_word += letter
    return new_word


print(next_letter('Io'))


def next_char(word):
    return ''.join([chr(ord(letter)+1) if letter in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') else letter for letter in word])


print(next_char('Hi'))

# zip(*iterables) = aggregates elements from two or more iterables
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ['I_Rohit', 'Cool_dude', 'Bro']
passwords = ('Rohit56', 'D@d', 'Bh@i')

login = zip(usernames, passwords)

print(type(login))

for i in login:
    print(i)



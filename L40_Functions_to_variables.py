def hello():
    print('hello')


hello()
hi = hello                          # Both are pointing at same memory reference
hi()

say = print
say(hi)                 # prints address in hexadecimal
print(hello)

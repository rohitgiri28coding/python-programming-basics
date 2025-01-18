# Higher order fn = a fn that either:
#                       1. accepts other fn as argument
#                               or
#                       2. returns a function
#
#                       (In python, fn are also treated as objects)


# e.g. to show higher order fn that accepts fn as arg
def hello(obj):
    text = obj('hello')
    print(text)


def lower(text):
    return text.lower()


def upper(text):
    return text.upper()


hello(upper)
hello(lower)


# e.g. to show higher order fn that returns a fn

def divisor(x):
    def dividend(y):
        return y/x
    return dividend


divide = divisor(5)
print(divide(10))


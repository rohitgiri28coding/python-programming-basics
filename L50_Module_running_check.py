# Modules can run as a standalone program
#  OR
# Module can be imported and used by other modules
#
# Python interpreter sets "special variables", one of which is main
# Python will assign the __name__ variable of value '__main__' if it's the initial module being running


def hello():
    print('Hello!')


if __name__ == '__main__':
    print('running from this module directly ')
    hello()
else:
    print('called from other module(indirectly).Imported module name ' + __name__)
#                                                     will run when called from another file

import L50_Indirect_Call

print('Imported module name ' + L50_Indirect_Call.__name__)

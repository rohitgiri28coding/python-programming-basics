# thread = a flow of execution. Like a separate order of instructions
#          However each thread takes a turn to achieve concurrency
#          GIL = (global interpreter lock),
#          which allows only one thread to hold the control of the python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events
#               (tasks which are cpu intensive) uses multiprocessing

# io bound = program/task spends most of it's time waiting for external events
#             (such as waiting for user input, web scrapping) uses multithreading

import threading
import time


def eating(name):
    print(name.capitalize() + ' started eating.')
    time.sleep(4)
    print('eating completed')


def drinking(name):
    print(name.capitalize() + ' started drinking.')
    time.sleep(3)
    print('drinking completed')


def studying(name):
    print(name.capitalize() + ' started studying')
    time.sleep(5)
    print('completed studying.')


x = threading.Thread(target=studying, args=('Rohit',))
x.start()

y = threading.Thread(target=eating, args=('Rohit',))
y.start()

z = threading.Thread(target=drinking, args=('Rohit',))
z.start()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())


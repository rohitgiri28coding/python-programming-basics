import time

print(time.ctime(0))            # convert a time expressed in s since epoch to a readable str
#                                 epoch = when computer thinks time begin (reference point)

print(time.time())              # returns current seconds since epoch

print(time.ctime(time.time()))   # prints current date and time

time_obj = time.localtime()

print(time.strftime("%d %B %Y %H:%M:%S", time_obj))      # %d --> date, %B-->Month, %Y-->Year

time_obj = time.gmtime()                    # UTC or Coordinated Universal Time

# (year, month, day, hours, minutes, seconds, day of the week, day of the year, daylight saving time)
time_tuple = (2002, 8, 28, 21, 0, 0, 2, 0, 0)
print(time.asctime(time_tuple))
print(time.mktime(time_tuple))      # count s since epoch



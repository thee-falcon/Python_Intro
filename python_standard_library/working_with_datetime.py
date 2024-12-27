# we are going learn how to work with date time obejects in python

from datetime import datetime
import time

dt1 = datetime(2024, 1, 1) # will print this date with time 2024-01-01 00:00:00
dt2 = datetime.now() # will print the current date and time, retrieves the current local date and time.

print(dt2)

dt = datetime.strptime("2024/12/27", "%Y/%m/%d") # print the date with specific format with a time: 00:00:00
dt = datetime.fromtimestamp(time.time()) # will print the current date and time, retrieves the current time as a floating-point number representing seconds since the Unix epoch (January 1, 1970, 00:00:00 UTC).
print(dt)

print(f"{dt.year}/{dt.month}") # the output of this line of code
print(dt.strftime("%Y/%m"))    # is similar of this method

# we're going to work with date and time in python

import time

def send_emails():
    for i in range(1000):
        print(f"email is send to the user{i}")

start = time.time()
send_emails()
end = time.time()
duration = end - start
print(f"the duration of the time{duration}")
from datetime import datetime, timedelta

# timedelta is present under datetime library which is generally used for calculating differences in dates and also can be used for date
# date manupilations in Python. Its is one of the easiest ways to perform date manipulations
dt1 = datetime(2024,12,27) + timedelta(days=1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("method of total seconds", duration.total_seconds())
#  Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime 

now = datetime.now()
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.timestamp())

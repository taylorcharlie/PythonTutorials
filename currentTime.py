
from datetime import datetime
  
# The now() mehtod is used
# to get the current time
# on the date that is now.
now_method = datetime.now()
  
# strftime() method used to
# get the hour,minute and second
# current time.
currentTime = now_method.strftime("%H:%M:%S")
print("Current Time =", currentTime)
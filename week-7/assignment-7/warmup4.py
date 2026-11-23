#Print today's date in the following format. The example below shows the format — your date will be the day you run the script:
#Today is April 24, 2026.
#Use datetime.now() and .strftime().

from datetime import datetime
today = datetime.now()
print(f"Today is {today.strftime("%B %d, %Y")}.")
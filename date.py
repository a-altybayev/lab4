#task 1
from datetime import datetime, timedelta
x = datetime.today()
d = x - timedelta(days=5)
print("Today:",x)
print("Five days ago:",d)
#strftime()

#task 2
from datetime import datetime, timedelta
x = datetime.today()
y = x - timedelta(days=1)
z = x + timedelta(days=1)
print("Yesterday:",y)
print("Today:",x)
print("Tomorrow:",z)

#task 3
from datetime import datetime
a = datetime.now()
print(a.strftime('%d-%m-%Y, %H:%M:%S'))

#task 4
from datetime import datetime
day1 = datetime.now()
day2 = datetime(2004,11,4)
diff = (day1-day2).total_seconds()
print("Difference is seconds:", diff)
from datetime import date
from datetime import datetime
from datetime import timedelta 

a = date(1993,9,1)
b = date.today()
eternal = (b - a).days 
print("It's been " + str(eternal) + " days since Eternal September")

september = input("Enter day: ")
date2 = a + timedelta(days=int(september))
print(date2)
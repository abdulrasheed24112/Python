import datetime
from datetime import date 
import datetime as dt
today_date = datetime.date.today()
print(today_date)

today_date = datetime.datetime.now()
print(today_date.strftime("%H:%M"))

today_time = date.today()
print(today_time)
print("The date is :",dt.date.today())
day_time = dt.datetime.now()
print(day_time.strftime("%H:%M:%S"))
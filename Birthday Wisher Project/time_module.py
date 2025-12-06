import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
print(year,month,day)

birthday_time = dt.datetime(year,month= 12,day= 5)
print(birthday_time)
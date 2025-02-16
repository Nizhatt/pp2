import datetime as day
print("Yesterday: ", day.datetime.now()-day.timedelta(1))
print("Today: ", day.datetime.now())
print("Tomorrow: ", day.datetime.now()+day.timedelta(1))
import datetime
day_of_week = input("Enter day") .lower()

ck_day = datetime.datetime.strptime(day_of_week,"%A")

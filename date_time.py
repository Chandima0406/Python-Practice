import datetime

b_day = datetime.date(2001,4,6)

print(b_day)

today = datetime.date.today()
print(today)

print(b_day.strftime('%A, %B %d, %Y'))

print(today - b_day)

t = datetime.time(9, 38, 45, 10000)
print(t.second)

r = datetime.datetime.today()
print(r)
print(r.time())
print(r.date())
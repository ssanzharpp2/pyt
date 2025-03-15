import datetime

cur = datetime.datetime.now()
delt = datetime.timedelta(days=5)
goal = cur - delt
print(goal)


import datetime
yt = datetime.datetime.now() - datetime.timedelta(days=1)
tm = datetime.datetime.now() + datetime.timedelta(days=1)
td = datetime.datetime.now()
print("Yesterday:", yt.strftime("%Y-%m-%d"))
print("Today:",td.strftime("%Y-%m-%d"))
print("Tommorow:", tm.strftime("%Y-%m-%d"))


import datetime
n = datetime.datetime.now()
print(n.replace(microsecond=0))




import datetime
n = 2
while n > 0:
    y = int(input("Year: "))
    m = int(input("Month: "))
    d = int(input("Day: "))
    h = int(input("Hour: "))
    m1 = int(input("Minute: "))
    s = int(input("Second: "))
    global date1, date2
    if n == 2:
        date1 = datetime.datetime(y, m, d, h, m1, s)
    else:
        date2 = datetime.datetime(y, m, d, h,m1,s)
    n -= 1
dif = date2 - date1
dfs = dif.total_seconds()
print(dfs)
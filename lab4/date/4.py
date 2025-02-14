import datetime

date1 = datetime.datetime(2025, 1, 24, 12, 0, 0)
date2 = datetime.datetime(2025, 2, 14, 18, 0, 0)
dif = date2 - date1
dfs = dif.total_seconds()
print(dfs)



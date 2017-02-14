from datetime import date, timedelta

start_date = [int(i) for i in input().split()]
res = date(*start_date) + timedelta(days=int(input()))
print(res.year, res.month, res.day)

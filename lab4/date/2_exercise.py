from datetime import date, timedelta
today_date=date.today()
yesterday_date=today_date-timedelta(days=1)
tomorrow_date=today_date+timedelta(days=1)
print(f"Yesteday: {yesterday_date}")
print(f"Today: {today_date}")
print(f"Tomorrow: {tomorrow_date}")
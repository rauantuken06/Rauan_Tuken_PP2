from datetime import datetime, timedelta
curent_date=datetime.now()
new_date=curent_date-timedelta(days=5)
print(f"Curent date: {curent_date.strftime("%d-%m-%Y")}")
print(f"Date after subtracting 5 days: {new_date.strftime("%d-%m-%Y")}")
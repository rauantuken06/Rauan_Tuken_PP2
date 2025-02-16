from datetime import datetime
common_date=datetime.now()
drop_milisec=common_date.strftime("%d-%m-%Y, %H:%M:%S")
print(drop_milisec)
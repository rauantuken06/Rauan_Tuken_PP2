from datetime import datetime, timedelta
yesterday=datetime.now()-timedelta(days=1)
tomorrow=datetime.now()+timedelta(days=1)
difference=tomorrow-yesterday
seconds=difference.total_seconds()
print(f"Difference in seconds: {seconds}")
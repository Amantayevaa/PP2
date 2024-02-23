#1
from datetime import datetime, timedelta
print(datetime.now()-timedelta(5))

#2
from datetime import datetime, timedelta
print(f"Yesterday: {datetime.now()-timedelta(1)}") 
print(f"Today:  {datetime.now()}")
print(f"Tomorrow: {datetime.now()+timedelta(1)}")

#3
from datetime import datetime
print(datetime.now().replace(microsecond=0))

#4
from datetime import datetime
def difference(date1, date2):
    d = abs(date2-date1)
    return(d.days * 24 *3600 + d.seconds)
date_str1 = "2024-01-01 12:00:00"
date_str2 = "2024-01-02 12:00:00"

date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
difference_in_seconds = difference(date1, date2)
print(difference_in_seconds)
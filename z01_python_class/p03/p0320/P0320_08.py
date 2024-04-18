from datetime import datetime
import time

now = datetime.now()


end_day = datetime(2024,6,24)
print(end_day)

print(end_day-now)  #   95 days, 8:08:27.317120
print((end_day-now).days)  #   95 남은 일
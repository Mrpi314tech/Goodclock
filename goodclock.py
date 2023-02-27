from datetime import datetime as dt
hour=int(dt.now().strftime("%H"))
minute=int(dt.now().strftime("%M"))
if minute <= 9:
    minute="0"+str(minute)
if hour >= 12:
    mn="PM"
    if hour == 12:
        hour = 12
    else:
        hour-=12
else:
    mn="AM"
hour=str(hour)
minute=str(minute)
clock=hour+":"+minute+" "+mn
print(minute)
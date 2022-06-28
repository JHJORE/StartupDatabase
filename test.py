import pandas as pd

datestring='20.09.16'
datestring= datestring[:6] + "20" + datestring[6:]
print(datestring)

date = pd.to_datetime(datestring, format="%d.%m.%Y")
print(date.strftime("%x"))
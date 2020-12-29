import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time
from matplotlib.figure import Figure
date = time.strftime("%Y%m%d")
df = pd.read_csv(date + '.csv', header=None)
df.columns = ["Temp C", "Pressure", "Humidity", "Time"]
Temp = df['Temp C']
Time = (df['Time'])
Time = pd.DatetimeIndex(pd.to_datetime(df['Time'], unit='s')).tz_localize('UTC').tz_convert('US/Eastern')
Time = pd.Series([val.time() for val in Time])
Humidity = df['Humidity']
plt.figure(figsize=(20,10))
plt.subplot(211)
plt.plot(Time,Temp,'k')
plt.xlabel('Time', fontsize = 18)
plt.ylabel('Temperature C',fontsize = 18)
plt.subplot(212)
plt.plot(Time,Humidity,'k')
plt.xlabel('Time', fontsize = 18)
plt.ylabel('Humidity %',fontsize = 18)
plt.ylim(0,100)
plt.savefig('/home/pi/'+ date + '.png')
plt.close()

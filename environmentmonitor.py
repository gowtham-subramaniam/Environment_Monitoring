from sense_hat import SenseHat
from datetime import datetime
from csv import writer
import csv
from gpiozero import CPUTemperature
import time
filename = time.strftime("%Y%m%d")
sense = SenseHat()
def get_sense_data():
    cpu_temp = CPUTemperature().temperature
    sense_data = []
    sense_data.append(sense.get_temperature()-((cpu_temp - sense.get_temperature())/2.466))
    sense_data.append(sense.get_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(time.time())
    return sense_data

f = open(filename + ".csv", "a")
w = csv.writer(f,delimiter=",")

while True:
        current_date = time.strftime("%Y%m%d")
        data = get_sense_data()
        print(data)
        if current_date != filename:
            f.close()
            filename = current_date
            f = open(filename + ".csv", "a")
            w = csv.writer(f, delimiter=",")

        w.writerow(data)
        time.sleep(1)


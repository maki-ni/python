import matplotlib.pyplot as plt 
import csv
from datetime import datetime

filename = 'data/Weather_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # to check which values had the temperature and date
    # for index, header in enumerate(header_row):
    #     print(index, header)
# highs and lows are the maximum and minimum temperatures of the file
    highs, lows, dates = [], [], []
    
    for line in reader:
        try:
            date = datetime.strptime(line[2], '%Y-%m-%d')
            high = int(line[8])
            low = int(line[9])
        except ValueError:
            print(f"Missing Data on Date: {date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='green')
fig.autofmt_xdate()
plt.title("Annual temperature, 2018", fontsize=24)
plt.xlabel('dates', fontsize=16)
plt.ylabel("temperature", fontsize = 16)

plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
#
# weather.py: Print min and max temps from a file
#

import matplotlib.pyplot as plt

fileobj = open('marchweather.csv', 'r')

line1 = fileobj.readline()
line2 = fileobj.readline()

fileobj.close()

mins = line1.split(',')
mins = [float(value1) for value1 in mins]
maxs = line2.split(',')
maxs = [float(value2) for value2 in maxs]
dates = range(1,32)

plt.plot(dates, mins, dates, maxs)
plt.show()

#
# Student Name: <your name>
# Student ID  : <your ID>
#
# test2b.py: Print min and max temps for March 2017 in Perth
#(source: http://www.bom.gov.au/climate/) 
import matplotlib.pyplot as plt

mins = [20.1, 22.9, 20.3, 22.9, 21.3, 19.2, 17.9, 20.7, 18.1, 19.5, 15.6,         18.5, 20.6, 18.7, 16.6, 13, 11.7, 16.8, 10.3, 12.6, 17.5, 16.2,16.8, 14.7, 15.7, 16.6, 8.3, 9.5, 12.9, 12.1, 9.6]
maxs = [37.7, 29.9, 35.2, 36.1, 36.2, 34.7, 33.8, 34.5, 31.9, 29.9, 30.9,24.8, 24.2, 24.1, 24, 28.3, 24.6, 19.8, 23.8, 26.2, 21.4, 24, 24.2,26.3, 27.2, 22.4, 23.3, 22.9, 24.9, 28, 29.9]
dates = range(1,32)
plt.subplot(211)
plt.ylabel('Temperature (Celsius)')
plt.title('Perth Max/Min March 2017')
plt.plot(dates, maxs, 'gs')
plt.subplot(212)
plt.ylabel('Temperature (Celsius)')
plt.xlabel('Day')
plt.plot(dates, mins, 'k^')
plt.show()

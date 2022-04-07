#
# growthsubplot.py - simulation of unconstrained growth with subplots
#
import numpy as np
import matplotlib.pyplot as plt

plt.ylabel('growth')

length = 100
population = 100
rate = 0.1
step = 0.5
numberOfIterations = length/step
ratePerStep = rate*step
values = np.zeros(int(numberOfIterations + 1))
hours = np.zeros(int(numberOfIterations + 1))
values[0] = 100

for i in range(1, int(numberOfIterations) + 1):
        growth = ratePerStep*population
        population = population + growth
        time = i*step
        values[i] = population
        hours[i] = time
        print('time: ', time, 'growth: ', growth, 'population: ', population)

plt.figure(1)

plt.subplot(211)
plt.plot(hours, values, '--')
plt.title('Unconstained Growth')
plt.ylabel('Population')

plt.subplot(212)
plt.plot(hours, values, 'ro')
plt.ylabel('Population')
plt.xlabel('Time')
plt.show()

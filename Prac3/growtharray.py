#
# growtharray.py - simulation of unconstrained growth using arrays
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
population[0] = 100

for i in range(1, int(numberOfIterations) + 1):
        growth = ratePerStep*population
        population = population + growth
        time = i*step
        values[i] = population
        hours[i] = time
        print('time: ', time, 'growth: ', growth, 'population: ', population)

plt.plot(hours, values, 'r-')
plt.title('Prac 3.1: Unconstrained Growth')
plt.show()

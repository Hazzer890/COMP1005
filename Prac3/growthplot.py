#
# growth.py - simulation of unconstrained growth
#

import matplotlib.pyplot as plt
plt.ylabel('growth')

length = 100
population = 100
rate = 0.1
step = 0.5
numberOfIterations = length/step
ratePerStep = rate*step
values = []

for i in range(1, int(numberOfIterations) + 1):
        growth = ratePerStep*population
        population = population + growth
        time = i*step
        values.append(population)
        print('time: ', time, 'growth: ', growth, 'population: ', population)

plt.plot(values, 'r-')
plt.title('Prac 3.1: Unconstrained Growth')
plt.show()

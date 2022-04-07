#
# growth.py - simulation of unconstrained growth
#

length = 10
population = 100
rate = 0.1
step = 0.5
numberOfIterations = length/step
ratePerStep = rate*step

for i in range(1, int(numberOfIterations) + 1):
        growth = ratePerStep*population
        population = population + growth
        time = i*step
        print('time: ', time, 'growth: ', growth, 'population: ', population)


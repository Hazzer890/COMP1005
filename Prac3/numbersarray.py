#
# numbersarray.py: Read in ten numbers and give sum, min, max & mean 
#
import numpy as np
import matplotlib.pyplot as plt

numarray = np.zeros(10)

print('Enter ten numbers...')

for i in range(len(numarray)):
    print('Enter number (', i, ')...')
    numarray[i] = int(input())

print('Total is ', numarray.sum())
print('Min is ', numarray.min())
print('Max is ', numarray.max())
print('Mean is ', numarray.mean())

plt.plot(numarray, 'bo')
plt.show()

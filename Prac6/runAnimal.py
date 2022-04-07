import numpy as np
from animals import *

csvfile = open('animals.csv')
data = csvfile.readlines()
objectArray = np.ndarray(len(data), object)
for i in range(len(data)):
    line = data[i].split(",")
    
    if line[0] == 'Dog':
        objectArray[i] = Dog(line[1], line[2], line[3], line[4])
    elif line[0] == 'Cat':
        objectArray[i] = Cat(line[1], line[2], line[3], line[4])
    elif line[0] == 'Bird':
        objectArray[i] = Bird(line[1], line[2], line[3], line[4])
    objectArray[i].printit()

csvfile.close()

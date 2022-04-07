#
# Author : 
# ID : 
#
# growth2D.py - Basic simulation of lifeforms 
#
# Revisions: 
#
# 12/4/21 – Base version for assignment
#
#
# 14/04/21 - In class work 
#

import random
import matplotlib.pyplot as plt
import numpy as np

RMAX  = 20
CMAX  = 25
POP   = 20
STEPS = 10

def movepop(popgrid):
    # Move population - by one step (randomly) in x and y

    nextgrid = np.zeros((RMAX, CMAX), dtype=int)

    for r in range(RMAX):
        for c in range(CMAX):
            for i in range(int(popgrid[r,c])):
                rmoved = r + random.choice([-1,0,1])
                cmoved = c + random.choice([-1,0,1])
                if rmoved == -1:
                    rmoved = 0
                if cmoved == -1:
                    cmoved = 0
                if rmoved == RMAX:
                    rmoved = RMAX - 1
                if cmoved == CMAX:
                    cmoved = CMAX -1
                nextgrid[rmoved,cmoved] += 1
    return(nextgrid)

def growpop(nextgrid):
    # Reproduction - 10% chance of reproducing +1 to pop in cell

    for r in range(RMAX):
        for c in range(CMAX):
            for i in range(int(nextgrid[r,c])):
                if random.random() <= 0.1:
                    nextgrid[r,c] += 1

    return(nextgrid)

def plotpop(popgrid):
    # Plot current population as array (could also use scatter plot)
    plt.title('2D Simulation of Population Growth')
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.imshow(popgrid, cmap=plt.cm.Greens_r)   # Note plt origin is top left
    plt.colorbar()
    plt.show()

def plotsave(popgrid, filename):
    plt.title('2D Simulation of Population Growth')
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.imshow(popgrid, cmap=plt.cm.Greens_r)   # Note plt origin is top left
    plt.colorbar()
    plt.savefig('../Plot/'+filename+'.png')

def main():

    print("\n ### 2D Growth Simulation ###\n")
    
    # Initialise population
    filename = input("Please input data filename: ")
    csvfile = open('../Data/' + filename + '.csv')
    popgrid = np.zeros((RMAX, CMAX), dtype=int)
    popgrid = np.loadtxt(csvfile, delimiter=',')
    nextgrid = np.zeros((RMAX, CMAX), dtype=int)
    
    for i in range(POP):
        randR = random.randint(0,RMAX-1)
        randC = random.randint(0,CMAX-1)
        popgrid[randR,randC] += 1
        print("Life at : [", randR, randC, "]")

    print("\n ### INITIAL POPULATION ###")
    plt.title('2D Simulation of Population Growth')
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.imshow(popgrid, cmap=plt.cm.Greens_r)   # Note plt origin is top left 
    plt.colorbar()
    plt.show()

    # Simulation
    
    for i in range(STEPS):
        print("\n ### TIMESTEP ",i, "###")

        nextgrid = movepop(popgrid)

        nextgrid = growpop(nextgrid)
    
        popgrid = nextgrid

        plotpop(popgrid)    
    
    plotsave(popgrid, filename)


if __name__ == "__main__":
    main()

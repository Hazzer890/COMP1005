# 
# Student Name: Harry Cassidy
# Student ID  : 20607591
#   test1.py  : Print a string and its length, also print every 3rd charater 
#                backwards adn uppercase, also print string forwards even 
#                characters lowercase odd characters uppercase and every 3rd 
#                as a %, also check how many of a character is in the string and
#                print, plot this infomation as a bar graph
#
import numpy as np
import matplotlib.pyplot as plt

funstring = "Fundamentals of Programming (Fun Times in Python-world!)"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphalist = [c for c in alphabet]       # use for x labels in plot
alphacount = np.zeros(len(alphabet))

print("\n-= PRACTICAL TEST 1 =-\n")

print((funstring[::-3]).upper())

for i in range(0, len(funstring)):
    if(i%3 == 0):
        print('%', end='')
    elif(i%2 != 0):
        print((funstring[i]).upper(), end='')
    else:
        print(funstring[i].lower(), end='')
print('\n')

# A bit about funstring

print("Length : ", len(funstring))
print("Number of A's : ", funstring.count("A"))

for i in range(0, len(alphabet)):
    alphacount[i] = (funstring.upper()).count(alphabet[i])
print(alphacount)

plt.title('Alpha Counts in Funstring')
plt.xlabel('Alphabet')
plt.ylabel('Alpha Count')
plt.bar(alphalist, alphacount, 0.9, color='magenta')
plt.show()


    

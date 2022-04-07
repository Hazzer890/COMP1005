#
#    strings1.py - read in a string and print it in reverse
#                    using a loop and a method call

instring = input('Enter a string...')
# *** add upper and duplicating code here

instring = instring.upper()
instring = instring + instring

#reversing with while loop

print('Reversed string is : ', end='')
index = 1
while index <= len(instring)-2:
    print(instring[index], end='')
    index = index + 2
print()

# reversing with a range loop

print('Reversed string is : ', end='')
for index in range(1, len(instring)-1, 2):
    print(instring[index], end='')
print()

# reversing with slicing

print('Reversed string is :', instring[1:len(instring)-1:2])

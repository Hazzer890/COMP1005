#
# bucket2.py - bucket list builder
#

print('\nBUCKET LIST BUILDER\n')

bucket = []

choice = input('Enter selection: e(X)it, (A)dd, (D)elete, (L)ist...')
choice = choice.upper()
while choice[0] != 'X':
    if choice[0] == 'A':
        print('Enter list item... ')
        newitem = input()
        bucket.append(newitem)
    elif choice[0] == 'D':
        delitem = input('Number of Bucket item')
        del bucket[int(delitem)]
    elif choice[0] == 'L':
        for item in bucket:
            print(item)
    else:
        print('Invalid Selection')
    choice = input('Enter selection: e(X)it, (A)dd, (D)elete, (L)ist..')
    choice = choice.upper()

print('\nGOODBYE!\n')


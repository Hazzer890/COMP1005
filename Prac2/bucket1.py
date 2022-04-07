#
# bucket1.py - use a python list for item in a bucket list
#

print('\nBUCKET LIST\n')

bucket1 = ['Witness something turly majestic', 'help a complete stranger', 'Laugh until I cry', 'Drive a Shelby Mustang']

bucket1.append('Kiss the most beautiful girl in the world')
bucket1.append('get a tatto')
bucket1.append('skydiving')
del bucket1[5]

bucket2 = ['visit stonehenge', 'drive a motorcycle on the great wall of china', 'go on a safari', 'visit the taj mahal', 'sit on the great egyptian pyramids', 'find the joy in your life']

print('bucket 1: ', bucket1)
print('bucket 2: ', bucket2)

bucket = bucket1 + bucket2
bucket.insert(5, 'get a tattoo')

print('Joined buckets: ', bucket)

print('\nNicer formatting....\n')

for item in bucket:
    print(item)


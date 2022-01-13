### Sample input ###
n = 5
array = [8, 3, 7, 9, 2]

m = 3
x = [5, 7, 9]

array = set(array)
print(array)

for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
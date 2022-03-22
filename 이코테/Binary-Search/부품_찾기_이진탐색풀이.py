### Sample input ###
n = 5
array = [8, 3, 7, 9, 2]

m = 3
x = [5, 7, 9]

array.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

for i in x:
    if binary_search(array, i, 0, n-1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
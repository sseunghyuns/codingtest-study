n = int(input())
array = list(map(int, input().split()))

start = 0
end = len(array)-1
answer = -1
while start <= end:
    mid = (start + end)//2
    
    if array[mid] < mid: # case 1
        start = mid+1
    elif array[mid] > mid: # case 2
        end = mid-1
    else:
        answer = mid
        break
print(answer)
# case 1
# -5 -3 1 3 5
# 0  1  2 3 4 

# case 2
# 0 5 7 9 15
# 0 1 2 3 4

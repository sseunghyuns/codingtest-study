'''
나의 풀이
재귀 형태의 이진 탐색.
만약 target에 해당하는 값을 찾았다면, 해당 값을 기준으로 좌, 우로 탐색하는 방식. O(logN)?
=> 만약 n개의 원소가 모두 target이라면? O(N)의 시간 복잡도를 갖게 됨.
=> 따라서 답지의 방식대로 target의 첫 번째 index와 마지막 index를 찾는 방식으로 풀어야 한다.

답지 풀이: target의 첫 index와 마지막 index를 찾는 방식
'''
#############
# 첫 번째 시도 #
#############
# 만약 x와 같은 값을 찾으면, 아래와 같이 다시 양쪽으로 탐색을 진행한다. 
# 1. end=mid-1로 왼편 탐색
# 2. start = mid+1로 오른편 탐색

# 만약 x보다 작은 값이면,
# start = mid+1 설정 후 오른편 탐색

# 만약 x보다 큰 값이면, 
# end = mid-1 설정 후 왼편 탐색
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
array = list(map(int, input().split()))
count = 0

def binary_search(start, end, target):
    global count
    if start > end:
        # print(f'return {start}, {end}')
        return None
    mid = (start + end) // 2
    # print(f'start: {start}, mid: {mid}, end: {end}')

    if array[mid] == target:
        count += 1
        # print(f'start: {start}, end: {end}->{mid-1}')
        binary_search(start, mid-1, target)
        # print(f'start: {start}->{mid+1}, end: {end}')
        binary_search(mid+1, end, target)
        
    elif array[mid] < target:
        binary_search(mid+1, end, target)
        
    else:
        binary_search(start, mid-1, target)

binary_search(0, n-1, x)
if count==0:
    print(-1)
else:
    print(count)
    
    
#############
# 두 번째 시도 #
#############

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
array = list(map(int, input().split()))

def binary_search_left(start, end, array, target):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            if mid-1 < 0 or array[mid-1] != target:
                return mid
            else:
                end = mid-1
                
        elif array[mid]>target:
            end = mid-1
        
        else:
            start = mid+1
    return None
    
def binary_search_right(start, end, array, target):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            if mid+1 > n-1 or array[mid+1] != target:
                return mid
            else:
                start = mid + 1
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None
        
            
def count_target(n, x, array):
    first_index = binary_search_left(0, n-1, array, x)
    
    if first_index is None:
        return print(-1)
        
    last_index = binary_search_right(0, n-1, array, x)
    last_index = first_index if last_index is None else last_index
    
    return print(last_index-first_index+1)
    
count_target(n, x, array)
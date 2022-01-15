# Sample Input
n, m = 4, 6
array = [19, 15, 10, 17]

array = sorted(array, reverse=True)
start = 0
end = max(array)

def binary_search(array, target, start, end):
    while (start <= end):
        mid = (start + end) // 2
        total = sum([i-mid for i in array if i>mid])
        
        # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
        if total < target:
            end = mid-1
        
        # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 기록해두기.
            start = mid+1                    
    return result

print(binary_search(array, m, start, end))


# 처음 이진 탐색으로 접근했던 코드
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
    
#     mid = (start + end) // 2
#     remains = sum([i-array[mid] for i in array if i-array[mid]>0])
    
#     if remains == target:
#         return array[mid]
#     elif remains > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)


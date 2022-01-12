# 퀵 정렬은 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 알고리즘이다.
# 선택 정렬과 삽입 정렬의 시간 복잡도는 O(N^2), 최악의 경우에도 O(N^2)를 보장한다.
# 퀵 정렬의 평균 시간 복잡도는 O(NlogN)으로 앞선 두 정렬 알고리즘에 비해 매우 빠른 편이다. 하지만 최악의 경우 시간 복잡도가 O(N^2)이다.
# 특히 퀵 정렬은 이미 데이터가 정렬되어 있는 경우에 매우 느리게 작동한다. 삽입 정렬과 반대된다고 이해할 수 있다. 

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    
    pivot = start # 피벗은 첫 번째 원소
    left = start+1
    right = end
    
    while left <= right:
        
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left +=1
        
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
    
quick_sort(array, 0, len(array)-1)
print(array)



### Python의 장점을 살린 퀵 정렬 소스코드 ###
# 전통 퀵 정렬의 분할 방식과는 조금 다르다.
# 피벗과 데이터를 비교하는 비교 연산 횟수가 증가하므로 시간 면에서는 조금 비효율적이지만 더 직관적이고 기억하기 쉽다는 장점이 있다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    
    # 리스트가 한 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
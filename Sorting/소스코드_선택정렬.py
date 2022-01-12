# 선택 정렬은 N-1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내는 알고리즘이다.
# 연산 횟수는 N + (N-1) + ... + 2 이고, 이는 약 N x (N+1) / 2 이다. 빅오 표기법으로 간단히 O(N^2)라고 표현할 수 있다.
# 따라서 만약 정렬해야 할 데이터의 개수가 100배 늘어나면, 이론적으로 수행시간은 약 10,000배로 늘어나기 때문에 비효율적.
# 다만 특정한 리스트에서 가장 작은 데이터를 찾아야 하는 일이 빈번히 발생하므로 선택 정렬 소스코드 형태에 익숙해질 필요가 있다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)
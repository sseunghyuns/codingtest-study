### Sample Input ###
n = 4
array = [1, 3, 1, 5]

d = [0] * 100
d[0] = array[0] # 첫 번째 식량 창고 선택a
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])
    
print(d[n-1])
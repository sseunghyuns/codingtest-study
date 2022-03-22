### Sample Input ###
n = 3
m = 7
array = [2,3,5]

d = [10001] *(m+1) # 10001은 범위를 벗어나는 화폐가치로 설정. 더 큰 아무 수여도 상관 없다.

d[0] = 0 # 화폐가 0원일 때는 0개를 선택해야하기 때문

# 작은 화폐단위부터 메모이제이션 진행
for i in range(n):
    for j in range(array[i], m+1): # 가장 작은 화폐부터 시작.
        # print(j-array[i])
        if d[j - array[i]]!=10001: # 없어도 되는 부분. 이해를 위해 삽입.
             # 점화식: a[i] = min(a[i], a[i-k]+1)
            d[j] = min(d[j], d[j-array[i]]+1)        
       
print(d) # [0, 10001, 1, 1, 2, 1, 2, 2]
result = d[m] if d[m]!= 10001 else -1
print(result) # 마지막 화폐가치 7을 만들 수 있는 최소한의 화폐 개수
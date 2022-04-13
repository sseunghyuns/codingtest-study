'''
풀이시간: 30분
'''

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    # 데이터 array 형식으로 입력받기 
    array = []
    start = 0
    for i in range(len(data)//m):
        array.append(data[start:start+m])
        start = start+m
    if n == 1:
        print(sum(array[0]))
        continue
   # array[행][열]
   # m번 반복문을 돌며, 각 행별로 가질 수 있는 최대값을 비교하여 저장
    for i in range(1, m): # 열
        for j in range(n): # 행
            if j == 0: # 첫 번째 행일 경우, 왼쪽, 혹은 왼쪽 아래에서만 올 수 있음
                array[j][i] += max(array[j][i-1], array[j+1][i-1])
            
            elif j == n-1: # 마지막 행일 경우, 왼쪽, 왼쪽 위에서만 올 수 있음
                array[j][i] += max(array[j][i-1], array[j-1][i-1])
            
            else:
                array[j][i] += max(array[j][i-1], array[j-1][i-1], array[j+1][i-1])

    answer = 0
    for i in range(n):
        answer = max(answer, (array[i][-1]))
    print(answer)
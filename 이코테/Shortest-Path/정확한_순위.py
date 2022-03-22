INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j]=0
            
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, m+1):
    for a in range(1, m+1):
        for b in range(1, m+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
# print(graph)

result = 0
for i in range(1, n+1):
    count=0
    for j in range(1, n+1):
        if graph[i][j]!=INF or graph[j][i]!=INF: # 도달 가능한 경우
            count+=1
    if count == n: # 모두 도달할 수 있는 경우
        result+=1
print(result)
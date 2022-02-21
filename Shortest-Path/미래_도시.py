INF = int(1e9) # 무한값 설정
n, m = map(int, input().split()) # 회사의 개수 n, 간선(경로)의 개수 m 입력받기
graph = [[INF]*(n+1) for _ in range(n+1)] # 무한으로 그래프 값 초기화

for a in range(n+1):
    for b in range(n+1):
        if a==b:
            graph[a][b]=0

# 간선 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1    

x, k = map(int, input().split()) # x회사, k회사의 정보 입력받기

# ### Sample Input ### 
# graph = [[0, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000], [1000000000, 0, 1, 1, 1, 1000000000], [1000000000, 1, 0, 1000000000, 1, 1000000000], [1000000000, 1, 1000000000, 0, 1, 1], [1000000000, 1, 1, 1, 0, 1], [1000000000, 1000000000, 1000000000, 1, 1, 0]]
# n, m, x, k = 5, 7, 4, 5

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][k] + graph[k][x]

# 결과 출력
if distance >= INF:
    print(-1)
else:
    print(distance)

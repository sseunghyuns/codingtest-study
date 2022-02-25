from re import M


n = int(input())
m = int(input())
INF = int(1e9)

info = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            info[i][j]=0    

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < info[a][b]:
        info[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            info[j][k] = min(info[j][k], info[j][i] + info[i][k])
            
for i in range(1, n+1):
    for j in range(1, n+1):
        if info[i][j]==INF:
            print(0, end=" ")
        else:
            print(info[i][j], end=" ")
    print()

'''
bfs 문제
풀이시간 30분
python3 제출시 시간초과, 동일 코드 pypy3 제출시 성공
'''

from collections import deque

m, n, h = map(int, input().split())
array = []

for _ in range(h):
    arr = []
    for _ in range(n):
        
        arr.append(list(map(int, input().split())))
        
    array.append(arr)

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if array[i][j][k] ==1:
                q.append((i,j,k))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

days = -1 # -1부터 시작
counts = len(q) # 하루 계산

while q:
    now_h, now_n, now_m = q.popleft()
    counts -= 1
    for i in range(6):
        nh, nn, nm = now_h+dz[i], now_n+dy[i], now_m+dx[i]
        if nh<0 or nh>=h or nn<0 or nn>=n or nm<0 or nm>=m: # 범위 벗어날 경우
            continue
        
        if array[nh][nn][nm]==0: # 안익은 토마토가 있는 칸
            array[nh][nn][nm] = 1
            q.append((nh, nn, nm))
    
    if counts == 0:
        counts = len(q)
        days += 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if array[i][j][k] ==0:
                days = -1
                break
print(days)
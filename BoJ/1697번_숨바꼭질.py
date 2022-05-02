from collections import deque

n, k = map(int, input().split())

q = deque()
level = 0
visited = [False] * 100001
q.append((n, level))

while q:
    now, lvl = q.popleft()
    visited[now] = True
    
    if now==k:
        break
    else:
        if 0<=now-1 <= 100000 and not visited[now-1]:
            q.append((now-1, lvl+1))
        if 0<=now+1 <= 100000 and not visited[now+1]:
            q.append((now+1, lvl+1))
        if 0<=now*2 <= 100000 and not visited[now*2]:
            q.append((now*2, lvl+1))

print(lvl)     
# 5
# 4,6,10
# (3,5,8), (5,7,12), (9,11,20)

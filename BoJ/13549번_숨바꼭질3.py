'''
https://www.acmicpc.net/problem/13549
'''


from collections import deque

n, k = map(int, input().split())

q = deque()
q.append(n) # 현재위치, 걸린 시간
visited = [False]*100001
dist = [-1] * 100001

visited[n] = True
dist[n] = 0

while q:
    now = q.popleft()
    if now == k:
        break
    if 0<=now*2<100001 and not visited[now*2]:
        visited[now*2] = True
        dist[now*2] = dist[now]
        q.appendleft((now*2))  
         
    if 0<=now-1<100001 and not visited[now-1]:
        visited[now-1] = True
        dist[now-1] = dist[now]+1
        q.append((now-1))
        
    if 0<=now+1<100001 and not visited[now+1]:
        visited[now+1] = True
        dist[now+1] = dist[now] +1
        q.append((now+1))  


print(dist[now])
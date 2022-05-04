'''
https://www.acmicpc.net/status?user_id=lsh9621&problem_id=13913&from_mine=1
0 0, 200 200 등과 같은 케이스에 대해 각각 0, 200값이 나와야함. 이 부분을 고려하지 못해 여러번 실패
'''
from collections import deque

n, k = map(int, input().split())

q = deque()
visited = [False] * 200001
path = [0] * 100001
q.append((n,0)) # now, level

while q:
    now, level = q.popleft()
    if now ==k:
        break

    if 0<=now+1<=100000 and not visited[now+1]:
        visited[now+1]=True
        path[now+1] = now 
        q.append((now+1, level+1))
    if 0<=now-1<=100000 and not visited[now-1]:
        visited[now-1]=True
        q.append((now-1, level+1))  
        path[now-1] = now
    if 0<=2*now<=100000 and not visited[2*now]:
        visited[2*now]=True
        q.append((2*now, level+1))             
        path[2*now] = now

print(level)

answer = []
while now != n:
    answer.append(now)
    now = path[now]
answer.append(n)

for i in answer[::-1]:
    print(i, end=' ')

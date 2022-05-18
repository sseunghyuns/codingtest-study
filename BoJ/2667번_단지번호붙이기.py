'''
https://www.acmicpc.net/problem/2667
'''

from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append([int(i) for i in input()])


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    count = 1
    q = deque([[x, y]])
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]==1:
                    q.append([nx, ny])
                    graph[nx][ny]=0
                    count+=1
    return count
        
answer=[]
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            answer.append(bfs(i, j))

print(len(answer))
for cnt in sorted(answer):
    print(cnt)


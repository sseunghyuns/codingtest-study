from collections import deque
'''
0-1 bfs
=> 0과 1의 가중치만 존재하는 그래프에서 
최단 거리 구하기.
O(V+E)의 시간 복잡도
'''
M, N = map(int, input().split())
maze = []

for _ in range(N):
    maze.append([int(i) for i in input()])

dx = [1,-1,0,0]
dy = [0,0,1,-1]
INF = int(1e9)
visited = [[INF]*M for _ in range(N)]
visited[0][0] = 0
queue = deque([(0,0)])

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if visited[nx][ny]==INF:
                if maze[nx][ny]==1:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny)) # 벽을 최소한으로 부수기 위해 append left
        
    
print(visited[N-1][M-1])


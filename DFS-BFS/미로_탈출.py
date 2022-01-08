from collections import deque

### Sample Input ###
# n,m = 5,6
# graph = [[1,0,1,0,1,0], [1,1,1,1,1,1], [0,0,0,0,0,1], [1,1,1,1,1,1], [1,1,1,1,1,1]]

# N, M을 공백으로 구분하여 입력하기
n,m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]  
def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()

    # 상,하,좌,우 네 가지 방향 확인
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]

      # 그래프 범위를 넘어가는 경우는 무시
      if nx<=-1 or nx>=n or ny<=-1 or ny>=m: 
        continue
      
      # 괴물이 있는 경우 무시
      if graph[nx][ny]==0:
        continue

      # 처음 방문하는 경우에만 최단거리 기록
      if graph[nx][ny]==1:
        graph[nx][ny] += graph[x][y]
        queue.append((nx,ny))

  # 출구 좌표에 해당하는 값 반환
  return graph[n-1][m-1]

print(bfs(0,0))
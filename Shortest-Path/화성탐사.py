import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
# 동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    graph = []
    N = int(input())
    
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    distance = [[INF]*N for _ in range(N)]
    
    x, y = 0, 0
    # 시작점 0,0으로 초기화 및 큐 삽입
    que = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]
    while que:
        # 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, x, y = heapq.heappop(que)
        if distance[x][y] < dist: # 이미 처리된 경우 건너뛰기
            print(f"Jump! :{distance[x][y]}, {dist}")
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 이탈시 무시
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(que, (cost, nx, ny))
    print(distance[N-1][N-1])
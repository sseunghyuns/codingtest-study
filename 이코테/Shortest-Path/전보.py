# 다익스트라 예시
import heapq
import sys

# INF = int(1e9)
# N, M, start = map(int, input().split())

# graph = [[] for _ in range(N+1)] 
# distance = [INF] * (N+1) # 최단 거리 초기화

# # 모든 간선 정보 입력 받기
# for _ in range(M):
#     x, y, z = map(int, input().split())
#     graph[x].append((y, z))

### Sample Input ###
INF = int(1e9)
N, M, start = 3, 2, 1
graph = [[], [(2, 4), (3, 2)], [], []]
distance = [INF] * (N+1) # 최단 거리 초기화

def dijkstra(start):
    q = []
    # 시작 노드 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dst, now = heapq.heappop(q)
        
        if distance[now] < dst:
            continue
        
        # 현재 노드와 연결된 노드들 확인
        for i in graph[now]:
            cost = dst + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 결과 출력
count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count+=1
        max_distance = max(d, max_distance)

# 시작 노드 제외
count -= 1
print(count, max_distance)
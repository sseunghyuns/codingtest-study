import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
# n: 헛간의 개수, m: 통로의 개수
n, m = map(int, input().split())

start = 1
# 연결 그래프 초기화
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# 연결 정보 업데이트
for _ in range(m):
    a, b = map(int, input().split())
    # 서로의 이동 거리가 1
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

dijkstra(1)
print(distance)

# distance = [1000000000, 0, 1, 1, 2, 2, 2]
max_dist = 0
to_hide = 0
nums_hide = []
for i in range(2, len(distance)):
    print(i, distance[i])
    if max_dist < distance[i]:
        max_dist = distance[i]
        nums_hide = [i]
        to_hide = i
    elif max_dist == distance[i]:
        nums_hide.append(i)

### Output ### 
print(to_hide, max_dist, len(nums_hide))
    
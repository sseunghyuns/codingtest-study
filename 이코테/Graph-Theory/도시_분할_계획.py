import heapq

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

N, M = map(int, input().split())

parent = [i for i in range(N+1)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(edges, (c, a, b))

result = 0 # 전체 비용
max_cost = 0 # edge 중 최대 비용

for i in range(M): 
    c, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result+=c
        if max_cost<c:
            max_cost=c
            
print(result-max_cost) # 마지막으로 추가된 edge 비용 제외
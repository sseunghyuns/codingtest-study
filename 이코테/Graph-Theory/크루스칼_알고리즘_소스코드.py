# find 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
# union 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
v,e = map(int, input().split())
parent = [i for i in range(v+1)]

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    
# 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a)!=find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost
    
print(result)

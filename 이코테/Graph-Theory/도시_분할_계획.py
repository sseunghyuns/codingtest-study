import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
    
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        parent[b] = a 
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
edges = [] # 최소 신장 트리 

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

def solution(parent, edges):
    result = 0 # 최종 유지비
    max_cost = 0
    for e in edges:
        cost, a, b = e
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost
            if max_cost < cost:
                max_cost = cost
    print(result-max_cost)
    
solution(parent, edges)
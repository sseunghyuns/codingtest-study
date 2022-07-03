def find(parent, x):
    if parent[x]!=x:
        parent[x] = find(parent, parent[x])
    return x # x
    
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
N, M = map(int, input().split())
parent = [i for i in range(N+1)]    
    
for _ in range(M):
    op = list(map(int, input().split()))
    if op[0]==0:
        union(parent, op[1], op[2])
    else:
        if find(parent, op[1])==find(parent, op[2]):
            print("YES")
        else:
            print("NO")
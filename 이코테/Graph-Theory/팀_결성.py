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

N, M =map(int, input().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    o, a, b = input().split()
    a, b = int(a), int(b)
    if o == '0':
        union(parent, a, b)
    else:
        if find(parent, a) == find(parent, b):
            print('YES')
        else:
            print("NO")
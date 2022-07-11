import sys
sys.setrecursionlimit(500000000)
input = sys.stdin.readline

n, m = map(int, input().split())

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
    
parent = [i for i in range(n+1)]

for _ in range(m):
    inputs = list(map(int, input().split()))
    if inputs[0]==0:
        union(parent, inputs[1], inputs[2])
    else:
        if find(parent, inputs[1]) == find(parent, inputs[2]):
            print('YES')
        else:
            print('NO')
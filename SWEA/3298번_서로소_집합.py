def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    answer = ['#'+str(i+1), ' ']
    for _ in range(m):
        data = list(map(int, input().split()))
        if data[0]==0:
            union(parent, data[1], data[2])
        else:
            if find(parent, data[1])==find(parent, data[2]):
                answer.append('1')
            else:
                answer.append('0')
    print(''.join(answer))

from itertools import combinations
from copy import deepcopy


n, m = map(int, input().split())
graph = []
answer= []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 0인 인덱스 찾기
combs = []
virus = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 0:
            combs.append((i,j))
        elif graph[i][j] == 2:
            virus.append((i,j))


def dfs(temp_graph, v):
    x, y = v
    
    if x<0 or x>=n or y<0 or y>=m:
        return False
    
    if temp_graph[x][y]==0:
        temp_graph[x][y] = 2
        
        dfs(temp_graph, (x+1, y))
        dfs(temp_graph, (x-1, y))
        dfs(temp_graph, (x, y+1))
        dfs(temp_graph, (x, y-1))
        
        return True
    
    return False

combs = combinations(combs, 3)



for comb in combs:

    temp_graph = deepcopy(graph)
    
    for i in range(3):
        temp_graph[comb[i][0]][comb[i][1]]=1
        
    for v in virus:
        temp_graph[v[0]][v[1]] = 0
        dfs(temp_graph, v)

    counter=0
    for i in range(len(temp_graph)):
        for j in range(len(temp_graph[0])):
            if temp_graph[i][j]==0:
                counter+=1
    
    answer.append(counter)

print(max(answer))
    
    
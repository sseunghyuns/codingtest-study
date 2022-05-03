'''
https://www.acmicpc.net/problem/4963
'''

# 1:땅
# 0:바다
# 섬의 개수(가로,세로, 대각선 연결) - dfs

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,-1,1,1,-1]

def dfs(x,y, graph):
    if graph[x][y]==1:
        graph[x][y]=0
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=len(graph) or ny<0 or ny>=len(graph[0]):
                continue
            if graph[nx][ny]==1:
                dfs(nx, ny, graph)
        return True
    return False

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    islands = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                dfs(i,j,graph)
                islands+=1
    print(islands)
    
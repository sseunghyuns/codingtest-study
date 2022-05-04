'''
https://www.acmicpc.net/problem/2178
'''

from collections import deque

n,m = map(int, input().split())
maze = []
for _ in range(n):
    a = input()
    maze.append([int(i) for i in a])


q = deque()
q.append((0,0)) # start

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x,y = q.popleft()
    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]
        if 0<=new_x<len(maze) and 0<=new_y<len(maze[0]):
            if maze[new_x][new_y] == 1: ###  방문하지 않은 경우만
                cost = maze[x][y] + 1
                maze[new_x][new_y] = cost
                q.append((new_x, new_y)) # 한 스텝 이동

                
print(maze[n-1][m-1])        
            
            
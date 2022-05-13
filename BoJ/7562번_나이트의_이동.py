'''
https://www.acmicpc.net/problem/7562
'''

from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

n = int(input())

for _ in range(n):
    l = int(input())
    now = list(map(int, input().split()))
    target =  list(map(int, input().split()))
    
    visited = [[0]*(l) for _ in range(l)]
    queue = deque([now])
    visited[now[0]][now[1]]=1
    while queue:
        now = queue.popleft()
        if now==target: # 정답 찾았을 경우 
            break
        
        for i in range(8):
            nx, ny = now[0]+dx[i], now[1]+dy[i]
            if nx<0 or nx>=l or ny<0 or ny>=l: # 범위를 벗어나면 무시
                continue
            if visited[nx][ny]==0: # 방문하지 않은 경우
                visited[nx][ny] = visited[now[0]][now[1]]+1 # 해당 칸으로의 이동 횟수 업데이트  업데이트
                queue.append([nx, ny]) # 큐에 추가
    
    print(visited[target[0]][target[1]]-1)

                
        

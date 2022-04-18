'''
bfs 너비 탐색으로 가능할 듯 
몇개의 그룹이 있는지 반환하는 문제
풀이시간: 25분
'''

from collections import deque

def solution(n, computers):
    answer = 0
    
    queue = deque([])
    visited = [False] * (n)
    
    # bfs
    queue.append((0, computers[0]))
    visited[0] = True
    
    
    while queue:
        index, link_info = queue.popleft() # 2, [0,0,1]
        
        for i in range(len(link_info)):
            if i != index and link_info[i]==1 and not visited[i]: # 자기 자신은 제외
                queue.append((i, computers[i]))
                visited[i] = True
        
        # que가 비었는데 visited에 False가 있으면 아직 탐색 범위가 남아있다는 것.
        if not queue:
            answer += 1
            for v in range(len(visited)):
                if not visited[v]:
                    queue.append((v, computers[v]))
                    visited[v] = True
                    break
        
        
    return answer
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    
    # 현재 노드 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
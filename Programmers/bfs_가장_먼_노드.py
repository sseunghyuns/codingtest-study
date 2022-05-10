from collections import deque

def solution(n, edge):
    node_list = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for e in edge:
        if e[0] not in node_list[e[1]]:
            node_list[e[1]].append(e[0])
        if e[1] not in node_list[e[0]]:
            node_list[e[0]].append(e[1])        
    
    queue = deque()
    queue.append([1,0])
    visited[1] = True
    answer = 0
    dist = 0
    
    while queue:
        now, level = queue.popleft()
        
        for v in node_list[now]:
            if not visited[v]:
                visited[v] = True
                queue.append([v, level+1])
                if level > dist:
                    answer=1
                    dist = level
                elif level == dist:
                    answer +=1
                
    return answer
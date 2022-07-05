from collections import deque

v,e = map(int, input().split())

indegree = [0] * (v+1) # 모든 진입차수 0으로 초기화

graph = [[] for _ in range(v+1)] # 모든 노드의 간선 정보 초기화

# 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # a -> b
    indegree[b] +=1 # 진입차수 증가
  
def topology_sort():
    result = [] 

    q = deque()
    
    for i in range(1, v+1):
            if indegree[i]==0: # 전입차수가 0인 노드 큐에 삽입
                    q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
                indegree[i] -= 1
                if indegree[i] == 0: # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                        q.append(i)

    # 결과 출력
    for i in result:
            print(i, end=' ')

topology_sort()

# N, M을 공백으로 구분하여 입력받기
n,m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

### Sample Input ###
# n,m = 4,5
# graph = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y]==0:
    graph[x][y]=1 # 방문처리
    # 현재 노드를 기준으로 상,하,좌,우 모두 재귀적으로 호출하여 확인
    # 아래 4번의 재귀 호출은, (상,하,좌,우)에 대하여 모두 방문처리를 하기 위함
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    return True
  return False

result=0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True: # 해당 노드와 연결된 모든 노드들도 방문처리할 수 있게끔 함. 그 시작점 노드가 방문처리가 되었다면 그때만 result값을 증가시킨다.
      result+=1
print(result)
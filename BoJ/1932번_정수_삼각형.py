'''
다이나믹 프로그래밍 문제
삼각형의 윗부분부터 차례대로 for loop을 돌며 최대 합을 업데이트해주는 방식.
양 끝의 점들은 이전 row의 하나의 값만 더할 수 있으므로 따로 처리해준다.
'''

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(len(graph)):
    if i == 0:
        continue
        
    for j in range(len(graph[i])):
        if j ==0:
            graph[i][j] += graph[i-1][0]
        elif j == len(graph[i])-1:
            graph[i][j] += graph[i-1][-1]
        else:
            graph[i][j] += max(graph[i-1][j-1], graph[i-1][j])

print(max(graph[-1]))
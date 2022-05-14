'''
문제: https://programmers.co.kr/learn/courses/30/lessons/43164
dfs 접근
풀이 참고: https://wwlee94.github.io/category/algorithm/bfs-dfs/travel-route/
'''

from collections import defaultdict

def solution(tickets):
    path_dict = defaultdict(list)
    for t in tickets:
        path_dict[t[0]].append(t[1])
    for k in path_dict:
        path_dict[k] = sorted(path_dict[k])
    
    stack = ["ICN"]
    answer = []
    
    while stack:
        now = stack[-1]
        
        # 더이상 이동할 곳이 없거나, 티켓 모두 사용한 경우
        if now not in path_dict or len(path_dict[now])==0:
            answer.append(stack.pop())
        else:
            stack.append(path_dict[now].pop(0))
            
    return answer[::-1] # 역순으로 정렬
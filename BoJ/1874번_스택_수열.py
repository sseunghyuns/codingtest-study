# [1,2,3,4,5,6,7,8] [4,3,6,8,7,5,2,1]

# [stack], [answer]
# [1,2,3,4] []
# [1,2] [4,3]
# [1,2,5,6] [4,3]
# [1,2,5] [4,3,6]
# [1,2,5,7,8] [4,3,6]
# [] [4,3,6,8,7,5,2,1]

'''
stack 자료구조의 특징 잘 이용하기(LIFO)

주요 포인트
- Stack에 Push하는 순서는 반드시 오름 차순
    - 위 조건을 잘 생각해보자.     
    
생각했던 접근 방식
1. dfs로 모든 경우의 수를 확인해보기?
2. 만들어야하는 수열에서 시작하여, [1,2, ... ,n]으로 복원하기 
-> 위 두 방식 모두 어떤 식으로 구현해야할지 감이 안와 결국 아래의 풀이로 진행했다.
'''
import sys
input = sys.stdin.readline

n = int(input())
max_num=1
stack = []
answer = []
for i in range(n):
    now = int(input()) # 4
    while max_num <= now: # [1,2,3,4]까지.
        stack.append(max_num)
        answer.append('+') # +,+,+,+
        max_num+=1
    
    if stack[-1] == now: # 4==4,
        stack.pop() 
        answer.append('-') 
        
if stack:
    print('NO')
else:
    for i in answer:
        print(i)

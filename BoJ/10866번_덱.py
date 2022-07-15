from collections import deque
import sys

input = sys.stdin.readline
def operation(data):
    op = data[0]
    if op=='push_front':
        num = int(data[1])
        q.appendleft(num)
    elif op=='push_back':
        num = int(data[1])
        q.append(num)
    elif op=='pop_front':
        if not q:
            print(-1)
        else:
            a = q.popleft()
            print(a)
    elif op=='pop_back':
        if not q:
            print(-1)
        else:
            a =q.pop() 
            print(a)  
    elif op=='size':
        print(len(q))
    elif op=='empty':
        if q:
            print(0)
        else:
            print(1)
    elif op=='front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
        
        
N = int(input())
q = deque()
for _ in range(N):
    data = input().split()
    operation(data)

    
# que: FIFO
# 버스 대기줄
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
queue = deque()

for _ in range(N):
    order = input().split()
    order_ = order[0]
    if order_ == 'back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])  
    elif order_ == 'pop':
        if len(queue)==0:
            print(-1)
        else:
            out = queue.popleft()
            print(out)
    elif order_ == 'size':
        print(len(queue))
    elif order_ == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif order_ == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    else:
        queue.append(int(order[1]))


'''
class 사용
'''

# que: FIFO
# 버스 대기줄
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

class Queue:
    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        self.q.append(x)
    
    def pop(self):
        if len(self.q)>0:
            out = self.q.popleft()
            return out
        else:
            return -1
    
    def size(self):
        return len(self.q)
        
    def empty(self):
        if len(self.q)>0:
            return 0
        else:
            return 1
    
    def front(self):
        if len(self.q)>0:
            return self.q[0]
        else:
            return -1
    
    def back(self):
        if len(self.q)>0:
            return self.q[-1]
        else:
            return -1

q = Queue()
for _ in range(N):
    orders = input().split()
    order = orders[0]
    if order == 'push':
        q.push(orders[1])
    elif order == 'pop':
        print(q.pop())
    elif order == 'size':
        print(q.size())
    elif order =='empty':
        print(q.empty())
    elif order =='front':
        print(q.front())
    else:
        print(q.back())

    

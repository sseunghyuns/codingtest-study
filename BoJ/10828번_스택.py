'''
https://www.acmicpc.net/problem/10828
'''

import sys
input = sys.stdin.readline

N = int(input())

def push(X):
    stack.append(X)

def pop():
    if stack:
        out = stack.pop()
        print(out)
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if stack:
        print(0)
    else:
        print(1)

def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

stack = []
for _ in range(N):
    orders = input().split()
    order = orders[0]
    if order == 'push':
        push(int(orders[1]))
    elif order == 'pop':
        pop()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    else:
        top()
        
    
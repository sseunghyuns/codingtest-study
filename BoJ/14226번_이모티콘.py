'''
https://www.acmicpc.net/problem/14226
'''

from collections import deque

s = int(input())

screen = 1 
visited = [[False]*2001 for _ in range(2001)]

q = deque()
q.append((1, 0, 0)) # screen, clipboard, level

while q:
    screen, clipboard, level = q.popleft()
    if screen == s:
        break
    if not visited[screen][clipboard]:
        visited[screen][clipboard]=True
        
        if 0<=screen+clipboard<=2000 and clipboard>0:
            q.append((screen+clipboard, clipboard, level+1))
        if screen>0:
            q.append((screen, screen, level+1))
            q.append((screen-1, clipboard, level+1))
            
print(level)
    
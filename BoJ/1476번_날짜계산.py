'''
https://www.acmicpc.net/problem/1476
'''

E, S, M = map(int, input().split())

e=s=m=0
year=0
while True:
    year+=1
    e+=1
    s+=1
    m+=1
    
    if e>15:
        e=1
    if s>28:
        s=1
    if m>19:
        m=1
    
    if e==E and s==S and m==M:
        break

print(year)
    
'''
중간값 떠올리기
'''

n = int(input())
loc = list(map(int, input().split()))

loc = sorted(loc)
mid = (len(loc)-1)//2
print(loc[mid])
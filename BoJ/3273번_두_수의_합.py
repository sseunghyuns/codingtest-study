'''
https://www.acmicpc.net/problem/3273

정렬 후, 투 포인터 알고리즘 적용
start + end < x 이면, start+1
start + end > x 이면, end-1
start + end == x 이면, count+1, start+1
'''

n = int(input())
array = map(int, input().split())
x = int(input())

array = sorted(array)

count = 0
start = 0
end = len(array)-1

while start < end:
    now = array[start] + array[end]
    if now < x:
        start +=1
    elif now > x:
        end -=1
    else:
        count+=1
        start +=1
print(count)
    

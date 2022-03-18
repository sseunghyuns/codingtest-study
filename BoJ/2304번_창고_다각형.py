"""

2022/03/18 페어프로그래밍으로 함께 풀었던 문제 복습
입력받을 때 max height값을 저장해놓고, 앞/뒤에서 차례대로 비교해오면서 면적을 업데이트하는 방식으로 코드 작성.
| 앞에서부터 출발하여 첫 max height를 만나는 지점 - 뒤에서부터 출발하여 첫 max height를 만나는 지점 | * max height를 최종적으로 더해준다. 

"""

n = int(input())
data = []
max_l, max_h = 0,0
for i in range(n):
    l,h = map(int, input().split())
    if h > max_h:
        max_h = h
        max_l = l
    data.append([l,h])
    
data = sorted(data)

area = 0
now_l = data[0][0]
now_h = data[0][1]

for i in data:
    if i[1]>now_h:
        area += (i[0]-now_l)*now_h
        now_h = i[1]
        now_l = i[0]
    if now_h == max_h:
        front_max_l = now_l
        break

now_l = data[-1][0]
now_h = data[-1][1]

for i in data[::-1]:
    if i[1]>now_h:
        area += (now_l - i[0])*now_h
        now_h = i[1]
        now_l = i[0]
    if now_h == max_h:
        back_max_l = now_l+1
        break
    
area += (back_max_l - front_max_l)*max_h
print(area)




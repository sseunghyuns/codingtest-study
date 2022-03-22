# 조건
# 1 <= n <= 1,000,000
# 1 < len(array) <= 1,000,000 
# 1 <= m <= 100,000
# 1 < len(x) <= 1,000,000

### Sample input ###
n = 5
my_items = [8, 3, 7, 9, 2]

m = 3
x = [5, 7, 9]

array = [0] * 1000001
for i in my_items:
    array[i] = 1

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for j in x:
    # 해당 부품이 존재하는지 확인
    if array[j]==1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
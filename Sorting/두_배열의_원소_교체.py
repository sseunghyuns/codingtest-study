# Sample input
# n,k = 5,3
# a = [1,2,5,4,3]
# b = [5,5,6,6,5]

n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))
n, m = map(int, input().split())

min_val = 0

# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  min_val = max(min(data), min_val) # 작은 수들 중 가장 큰 수 찾기

print(min_val)
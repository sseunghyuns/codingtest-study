n, m, k = map(int, input().split())
data = list(map(int, input().split())

data.sort() # 입력받은 수 정렬

first = data[n-1]
second = data[n-2]

# 반복되는 수열을 이용
numbers_sum = first*k + second # 하나의 수열의 합
answer = m//(k+1)* numbers_sum + m%(k+1)*first

print(answer)

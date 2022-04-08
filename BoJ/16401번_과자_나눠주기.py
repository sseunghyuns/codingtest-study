m, n = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

answer = 0

while start <= end:
    mid = (start + end) // 2

    if mid == 0:
        break

    people = sum([i//mid for i in data])        

    if people >= m: # 나눠줄 수 있는 조카 수가 target보다 큰 경우
        answer = mid # answer 업데이트
        start = mid + 1 # 나눠줄 수 있는 더 큰 길이의 막대과자가 있는지 탐색

    else: # people < m  # 나눠줄 수 있는 조카 수가 target보다 작은 경우
        end = mid - 1 # 길이를 낮춰 더 많은 막대 과자의 범위에서 다시 탐색 

print(answer)


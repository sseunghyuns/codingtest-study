'''
투 포인터: 리스트에 순차적으로 접근해야할 때 2개의 점의 위치(start, end)를 기록하면서 처리하는 알고리즘

알고리즘
1. start와 end가 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
2. 현재 부분합이 M과 같다면 count+=1
3. 현재 부분합이 M보다 작으면 end를 1만큼 증가시킨다.
4. 현재 부분합이 M보다 크거다 같다면 start를 1만큼 증가시킨다.
5. 모든 경우를 확인할 때까지 2~4를 반복한다.

예시 문제
n개의 데이터가 주어졌다고 할 때, 합이 m인 부분 연속 수열의 개수를 구하라.
'''

n = 5 # 데이터 개수
m = 5 # 타겟 값
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):

    # 현재 부분합이 m보다 작을 때까지 end 업데이트
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    
    if interval_sum == m:
        count+=1  
            
    # start가 한칸 옆으로 이동하므로 현재 부분합에서 start에 해당하는 값 제외
    interval_sum -= data[start]
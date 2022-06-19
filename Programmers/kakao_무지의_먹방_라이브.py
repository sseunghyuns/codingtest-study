'''
처음 접근법
- k 시점까지 while 문을 계속 돌며 체크하는 방식
- 효율성 탈락
'''

def solution(food_times, k):
    length = len(food_times)
    while True:
        for i in range(length):

            if food_times[i]==0:
                continue
                
            if k!=0:
                food_times[i]-=1
                k-=1
            else:
                return (i%length)+1
            
'''
답지 참고
- 우선순위 큐 사용
'''

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    que = []
    for i in range(len(food_times)):
        heapq.heappush(que, (food_times[i], i+1))
    
    sum_ = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times)
    
    # print("que: ", que)
    # now = heapq.heappop(que)
    # print(now[0]*length) # 시간이 가장 적게 필요한 2번 음식을 다 먹기까지 3초 걸림.
    
    while sum_ + ((que[0][0] - previous)*length) <= k:
        now = heapq.heappop(que)[0]
        sum_ += (now-previous)*length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 직전에 다 먹은 음식 시간 업데이트

    answer = sorted(que, key=lambda x : x[1])
    return answer[(k-sum_)%length][1]
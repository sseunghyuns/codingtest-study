n = int(input())
fears = list(map(int, input().split()))
fears.sort() # 오름차순 정렬

# 정보 초기화
group_nums = 0 # 그룹 수 
count = 0 # 현재 그룹에 포함된 모험가의 수

for idx, i in enumerate(fears, start=1):
    count+=1
    # print(f"{idx}번째: {i} 공포도")
    if i <= count: # 공포도보다 인원수가 같거나 많으면 그룹 결성.
        # print(f"그룹 결성: {i} 공포도, {count}명")
        group_nums+=1
        count=0 # 현재 그룹의 모험가의 수 초기화

print(group_nums)
    

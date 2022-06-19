# 1. 각 user가 어떤 user를 신고했는지에 대한 dictionary 생성
# 2. 각 user가 신고당한 횟수에 대한 dictionary 생성
# 3. report_dict를 돌면서, 각 유저별로, 정지 메일을 받는 횟수를 count

def solution(id_list, report, k):
    
    report_dict = {} # 신고당한 횟수 기록
    user_dict = {} # 각 유저가 신고한 기록
    
    for r in report:
        user, repo = r.split()
    
        if user in user_dict:
            if repo not in user_dict[user]: # 중복 무시
                user_dict[user].append(repo)
        else:
            user_dict[user] = [repo]
            
    for user in user_dict: # 신고 당한 각 user별로 횟수 count
        for u in user_dict[user]:
            if u in report_dict:
                report_dict[u]+=1
            else:
                report_dict[u]=1

    answer = []
    for id_ in id_list:
        if id_ not in user_dict: # 신고한 유저가 없다면 정지 메일 받지 않음
            answer.append(0)
        else:
            count = 0
            for report_id in user_dict[id_]:
                if report_dict[report_id]>=k: # k보다 많이 신고를 받았을 경우
                    count+=1
            answer.append(count)
            
    return answer


'''
다른 사람의 풀이 참고
- set 사용해서 중복 지우기
- index() 사용해서 answer의 인덱스에 수 더해주기
'''

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}
    for r in set(report):
        reports[r.split()[1]]+=1
    # print(reports)
    
    for r in set(report):
        user, repo = r.split()
        if reports[repo]>=k:
            answer[id_list.index(user)]+=1
    return answer
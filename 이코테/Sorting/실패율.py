def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        answer.append((i, fail))
        length -= count
    answer = sorted(answer, key=lambda x: -x[1])
    answer = [x[0] for x in answer]
    return answer


# def solution(N, stages):
#     answer = []
    
#     answer_dict = {}
#     for i in range(1, N+1):
#         stages_new = [x for x in stages if x>i]
        
#         if not stages:
#             fail_rate = 0
#         else:
#             fail_rate = (len(stages)-len(stages_new)) / len(stages)
#         stages = stages_new
#         answer_dict[i] = fail_rate
        
#     return [x[0] for x in sorted(answer_dict.items(), key =lambda x: -x[1])]
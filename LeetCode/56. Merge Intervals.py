from typing import List
'''
https://leetcode.com/problems/merge-intervals/
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key=lambda x: x[0])
        answer = []
        
        for i in intervals:
            now_start, now_end = i[0], i[1]
            
            # 미리 정렬했기 때문에 for loop을 돌면서 now_start은 자동적으로 ascending
            if not len(answer) or answer[-1][1] < now_start: # 아예 겹치지 않거나 answer가 비어있는 경우
                answer.append([now_start, now_end])
            
            else: # answer가 비어있지 않고 구간이 겹치는 경우
                answer[-1][1] = max(answer[-1][1], now_end)

#             if len(answer) and answer[-1][1] >= now_start:
#                 # new_start = answer[-1][0] # answer 내의 값 자체를 바꿔야함
#                 answer[-1][1] = max(answer[-1][1], now_end)
        
        return answer
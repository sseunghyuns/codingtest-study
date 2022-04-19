'''
첫 번째 시도
Indexing 활용하는 코드로 개선 필요
'''

def solution(citations):
    h_index = 0
    citations = sorted(citations)
    
    for h in range(max(citations), -1, -1):
        up_count = 0 # h
        lower_max = 0
        for i in citations:
            if i>=h:
                up_count+=1
            else:
                lower_max = max(lower_max, i) # 나머지 논문 각각이 모두 h번 이하 인용되어야함.
        if up_count >= h and lower_max<=h:            
            if h > h_index:
                h_index = h
    return h_index
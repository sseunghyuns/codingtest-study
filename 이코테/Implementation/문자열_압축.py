def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2+1):
        
        now = s[0:step] # 처음 시작
        counter=1
        length = 0
        
        for i in range(step, len(s), step):
            if now == s[i:i+step]:
                counter+=1
            else:
                if counter==1:
                    length+=len(f"{now}")
                else:
                    length+=len(f"{counter}{now}")
                now = s[i:i+step]
                counter=1
        if counter==1:
            length+=len(f"{now}")
        else:
            length+=len(f"{counter}{now}")    
        answer = min(length, answer)
    return answer

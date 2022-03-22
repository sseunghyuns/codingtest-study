'''
문제: https://programmers.co.kr/learn/courses/30/lessons/43105
AI Boostcamp CanVas 팀원들과 페어프로그래밍으로 해결했던 문제
삼각형의 row를 하나씩 확인하면서, index에 따라 값을 업데이트해주는 방식.
이전 row의 하나의 값만 참조할 수 있는 양 끝에 있는 값들을 각각 if/elif로 처리해주고, 이전 row의 두 값을 모두 참조할 수 있는 경우를 else로 처리해주었다.

return으로는 최종 업데이트된 triangle의 마지막 row의 max값을 반환한다.

'''

def solution(triangle):
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
                
            elif j==len(triangle[i])-1:
                
                triangle[i][j] += triangle[i-1][-1]
                
            else:
                triangle[i][j] = max(triangle[i][j]+ triangle[i-1][j-1], triangle[i][j]+triangle[i-1][j])
    
    return max(triangle[-1])
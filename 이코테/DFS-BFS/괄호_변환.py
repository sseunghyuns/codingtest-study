'''
https://programmers.co.kr/learn/courses/30/lessons/60058#

처음 문제를 이해하는데 시간이 조금 걸렸다.
문제에 주어진 조건들을 실수없이 구현하면 되는 문제.

'''

def solution(p):
    # 1. 
    if p=='':
        return p
    if is_complete(p):
        return p    
    
    # 2. u: '(', ')' 하나씩 존재. 
    u, v = split_w(p)
    # 3.
    if is_complete(u):
        # 문자열 v에 대해 1단계부터 다시 수행
        return u + solution(v)
    
    # 4. 
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:]
        u = u[:-1]
        new_u = ''
        for i in u:
            if i==')':
                new_u+='('
            else:
                new_u+=')'
        answer += new_u
        
        return answer

# p가 올바른 문자열인지 판단하는 함수
def is_complete(p):
    
    if p[0]==')' or p[-1]=='(':
        return False
    
    stack = []
    for i in p:
        if not stack:
            stack.append(i)
        elif i==')' and stack[-1]=='(':
            stack.pop()
        else:
            stack.append(i)
    if stack:
        return False
    else:
        return True

# 문자열을 u,v로 분리하는 함수
def split_w(w): # ))((() -> u=))((, v=()
    count = 0
    for i in range(len(w)):
        if w[i] == '(':
            count+=1
        else:
            count-=1
        if count == 0:
            u, v = w[:i+1], w[i+1:]
            if u == '':
                u, v = v, u
            return u, v
    return w, ''
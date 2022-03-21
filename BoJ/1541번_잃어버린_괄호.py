'''
양수 +, -
1. 첫 "-" 나올 때 괄호 열기 (최대한 많은 수 빼기?)
2. 두 번째 "-"가 나오면 열린 괄호 먼저 닫고, 다시 열기
'''

eq = input()

temp = ''
answer = ''
is_open = False

for i in eq:
    if i not in ['+', '-']:
        temp += i 

    elif i=='-': 
        if is_open: # 두 번째 "-"
            answer += str(int(temp))
            answer += ')'+i+'('
            temp = ''
            
        else: # 첫 "-"
            answer +=str(int(temp))
            answer += i
            answer += '('
            temp = ''
            is_open=True
    else:
        answer += str(int(temp))
        answer += i
        temp = ''

answer += str(int(temp)) # 마지막 숫자

if is_open:
    answer +=')'
print(eval(answer))
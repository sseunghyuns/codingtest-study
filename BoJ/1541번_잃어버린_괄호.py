eq = input()

data = []
temp = ''
is_open = False

for i in eq:
    if i not in ['+', '-']:
        temp+=i
        
    elif i == '-':
        if is_open: # 괄호가 열린 적이 있으면
            data.append(str(int(temp)))
            data.append(')') # 괄호 닫기
            data.append(i)
            data.append('(') # 괄호 열기    
            temp= ''
        else: # 괄호가 열린 적이 없으면
            data.append(str(int(temp)))
            data.append(i)
            data.append('(') # 괄호 열기    
            temp = ''
            is_open = True
    else:
        data.append(str(int(temp)))
        data.append(i)
        temp = ''
data.append(str(int(temp))) # 마지막 숫자
if is_open:
    data.append(')')
print(data)

answer = "".join(data)
print(eval(answer))

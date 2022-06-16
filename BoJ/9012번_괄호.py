T = int(input())

def isVPS(ps):
    stack = []
    stack.append(ps[0])
    for i in ps[1:]:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1]!=')':
                stack.pop()
            else:
                return "NO"
    if stack:
        return "NO"
    else:
        return "YES"
    

for _ in range(T):
    ps = input()
    print(isVPS(ps))

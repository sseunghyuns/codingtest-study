'''
이코테 답지 참고 코드
dfs 풀이
'''


n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mult, div = list(map(int, input().split()))

min_value = int(1e9)
max_value = -int(1e9)

def dfs(i, now, plus, minus, mult, div):
    global min_value, max_value
    
    if i == n:
        min_value = min(now, min_value)
        max_value = max(now, max_value)
    else:
        if plus>0:
            dfs(i+1, now+numbers[i], plus-1, minus, mult, div)
        if minus>0:
            dfs(i+1, now - numbers[i], plus, minus-1, mult, div)
        if mult>0:
            dfs(i+1, now * numbers[i], plus, minus, mult-1, div)
        if div>0:
            if now<0:
                dfs(i+1, -(-now // numbers[i]), plus, minus, mult, div-1)
            else:
                dfs(i+1, (now // numbers[i]), plus, minus, mult, div-1)

dfs(1, numbers[0], plus, minus, mult, div)

print(max_value)
print(min_value)
    
###############
###############

from itertools import permutations
'''
1차 시도: permutation을 사용해 모든 경우의 수 구해보기
=> 시간 초과
'''
ref_operators = ['+', '-', '*', '/']

n = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))

operators = []
for i in range(len(ops)):
    operators += [ref_operators[i]] * ops[i]

# print(operators)
# 모든 경우의 수를 구해보면?
perm = list(permutations(operators, len(operators)))

visited = []
answer = []
for p in perm:
    if p not in visited:
        visited.append(p)
        result = numbers[0]
        for num, op in zip(numbers[1:], p):
            if op == '+':
                result += num
            elif op == '-':
                result -= num
            elif op == '*':
                result *= num
            else:
                if result>0:
                    result = result // num
                else:
                    result = -(-result // num)
        answer.append(result)

print(max(answer))
print(min(answer))


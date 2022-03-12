# S = input()
S = "00110011010011010"

# 연속된 0 혹은 1의 블록 수를 구해서, 그 중 더 작은 값이 행동의 최소 횟수가 될 것이다.

now = S[0]
zero_block = 0
one_block = 0

if now =='0':
    zero_block+=1
else:
    one_block+=1

for i in range(1, len(S)):
    if S[i] != now:
        
        if S[i]=='0':
            zero_block+=1
        else:
            one_block+=1
        now = S[i]
        
assert min(zero_block, one_block)==5

'''
이코테 풀이: 나의 풀이 방식과 동일
'''
S = input()
# 매 단계마다 +/x를 둘 다 계산해봐서, 더 높은 수를 찾으면 되지 않을까?

start = S[0]
result = int(start)
for i in range(1, len(S)):
    i = int(S[i])
    result = max(result+i, result*i)

print(result)

'''
이코테 정답:
0,1인 경우 더하고, 2~9인 경우 곱하자.
'''
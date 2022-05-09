'''
2022/05/09 CanVas 조원들과 pair programming으로 진행했던 문제.
아래 코드로 접근시, 
ABADE
CCEFG
와 같은 케이스를 처리하지 못하는 문제 발생.(C가 9가 되어야 한다.)
따라서 
A = 10100
B = 11000 과 같이 자리수에 따라 sorting 후, 숫자를 할당하는 방식으로 접근하면 훨씬 간단해진다.
'''

# 실패 코드
n = int(input())
alph = []
for _ in range(n):
    alph.append(input())
alph = sorted(alph, key=lambda x: len(x), reverse=True)

num_dict = {}
max_n = 9
if len(alph)==1:
    for s in alph[0]:
        if s not in num_dict:
            num_dict[s] = max_n
            max_n -= 1
else:
    for i in range(len(alph)-1):
        x1, x2 = alph[i], alph[i+1]
        for s in range(len(x1)):
            temp_x = x1[s:]
            if len(temp_x) == len(x2):
                for a,b in zip(temp_x, x2):
                    if a not in num_dict:
                        num_dict[a] = max_n
                        max_n -=1
                    if b not in num_dict:
                        num_dict[b] = max_n
                        max_n -=1

            elif len(temp_x) > len(x2):
                if x1[s] not in num_dict:
                    num_dict[x1[s]] = max_n
                    max_n -=1
answer = 0
for w in alph:
    val = ''
    for i in w:
        val+=str(num_dict[i])
    answer+= int(val)
print(answer)


'''
pair-programming 코드(성공)
'''
n = int(input())

strings = []
for _ in range(n):
    strings.append(input())

num_dict = dict()

# 길이가 같을때?
# 각 알파벳의 자리수에 따라 정렬 후 9~0까지 값 할당하는 방식

for string in strings:
    for i in range(len(string)):
        l = len(string) - i
        if string[i] not in num_dict:
            num_dict[string[i]] = 10**(l-1)
        else:
            num_dict[string[i]] += 10**(l-1)

num_dict = sorted(num_dict.items(), key=lambda x: -x[1])

max_ = 9
answer = 0
for v in num_dict:
    answer += max_*(v[1])
    max_ -=1
print(answer)
'''
https://www.acmicpc.net/problem/2309
'''

h = []
for _ in range(9):
    h.append(int(input()))
    
def remove_fake(h):
    total = sum(h)
    for i in range(len(h)):
        for j in range(i+1, len(h)):
            if  total - (h[i]+h[j]) == 100:
                new_h = [x for x in h if x not in [h[i], h[j]]]
                return sorted(new_h)
answer = remove_fake(h)
for i in answer:
    print(i)
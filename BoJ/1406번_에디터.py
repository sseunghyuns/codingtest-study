import sys

word = input()
'''
시간 초과.
 list.pop()과 list.append(v)를 이용해서 다시 풀어보자.
'''

M = int(input())
answer = [w for w in word]
now = len(answer)

for _ in range(M):
    orders = input().split()
    order = orders[0]
    if order == 'P':
        if now > 0:
            answer = answer[:now] + [orders[1]] + answer[now:]
        else:
            answer = [orders[1]] + answer
        now+=1
    elif order == 'L':
        if now > 0:
            now-=1
    elif order == 'D':
        if now < len(answer):
            now+=1
    else: # B
        if now > 0:
            answer = answer[:now-1] + answer[now:]
            now -= 1

print("".join(answer))


'''
드디어 시간초과 해결.. 결국 다른 풀이를 참고했음.
https://seongonion.tistory.com/53

깨달은 포인트

1. a[:n]과 같은 슬라이싱을 진행할 경우 복잡도가 자른 크기만큼 변한다(복잡도=n이 됨.)
2. pop의 인자로 인덱스를 보내주면 더이상 복잡도가 1이 아니게 된다. 관련 링크: https://hyun-am-coding.tistory.com/entry/Python-list-%EC%97%B0%EC%82%B0%EC%97%90-%EB%94%B0%EB%A5%B8-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84

따라서, push/pop만을 이용하여 복잡도가 1인 프로그램을 작성해야 한다.
두 개의 스택을 만들어, 각각 맨 끝과 처음 인자를 주고 받는 식으로 코드를 작성하자!
'''

import sys
input = sys.stdin.readline

stack_left = list(input().strip()) # 공백 제거 후 리스트화
stack_right = []

N = int(input())

for _ in range(N):
    orders = input().split()
    order = orders[0]
    
    if order == 'P':
        stack_left.append(orders[1])
    elif order == 'L':
        if len(stack_left)>0: 
            stack_right.append(stack_left.pop()) # stack_right = [stack_left.pop()] + stack_right  이런 식으로 코드를 작성했는데, 시간 초과가 갈렸다. 
    elif order == 'D':
        if len(stack_right)>0:
            stack_left.append(stack_right.pop()) 
    elif order == 'B':
        if len(stack_left)>0:
            stack_left.pop()
            
# reversed(list)를 하면 list가 반환이 되는 게 아니라  listreverseiterator 객체를 반환
print("".join(stack_left+list(reversed(stack_right))))





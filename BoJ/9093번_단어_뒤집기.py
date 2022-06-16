import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sentence = input().split()
    sentence = " ".join([w[::-1] for w in sentence])
    print(sentence)
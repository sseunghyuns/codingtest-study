from itertools import permutations

def isPrime(num):
    for i in range(2, int(num**(1/2))+1):
        if num%i==0:
            return False
    return True


def solution(numbers):
    answer = []
    numbers = [i for i in numbers]

    for i in range(1, len(numbers)+1):
        perms = permutations(numbers, i)
        for perm in perms:
            num = int("".join(perm))
            if num in [0, 1] or num in answer:
                continue
            if isPrime(num):
                answer.append(num)

    return len(answer)
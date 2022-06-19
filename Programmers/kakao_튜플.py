def solution(s):
    answer = []
    s = s.lstrip("{").rstrip("}").split("},{")
    s = sorted(s, key=lambda x: len(x))

    for i in s:
        for t in i.split(","):
            if int(t) not in answer:
                answer.append(int(t))

    return answer
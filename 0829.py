def is_perf(st):
    close = [']', '}', ')']
    op = ['[', '{', '(']
    if st[0] in close:
        return False

    que = []
    for e in st:
        if e in op:
            que.append(e)
        elif e in close and que == []:
            return False

        elif e in close and que != []:
            if op.index(que[-1]) != close.index(e):
                return False
            que.pop()

    if que == []:
        return True
    return False


def solution(s):
    answer = 0
    temp = s
    for i in range(len(s)):
        if is_perf(temp):
            answer += 1
        temp = temp[1:] + temp[0]
    return answer
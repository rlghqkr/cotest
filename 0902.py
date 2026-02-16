def solution(s):
    
    tmp = []
    for i in s:

        if len(tmp) == 0:
            tmp.append(i)

        elif tmp[-1] == i:
            tmp.pop()

        else:
            tmp.append(i)

    if len(tmp) == 0:
        return 1
    return 0
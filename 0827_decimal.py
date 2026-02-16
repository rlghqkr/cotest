def solution(d):
    decimal=[]
    while d>1:
        decimal.append(d%2)
        d=d//2
    decimal.append(d)

    decimal.reverse()

    return decimal

print(solution(10))
print(solution(12345))
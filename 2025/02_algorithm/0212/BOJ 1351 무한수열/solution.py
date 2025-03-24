def solution(N):
    if N==0:
        return 1
    if N//P in dic:
        p = dic[N//P]
    else :
        p = solution(N//P)
    if N//Q in dic:
        q = dic[N//Q]
    else : q = solution(N//Q)

    dic[N]=p+q
    return p+q


N, P, Q = map(int, input().split())
dic = {0:1}
print(solution(N))
def solution(idx, cnt, ans):
    if cnt==M:
        print(ans)
        return
    for i in range(idx+1, N+1):
        solution(i, cnt+1, ans+str(i)+" ")

N, M = map(int, input().split())
solution(0, 0, '')
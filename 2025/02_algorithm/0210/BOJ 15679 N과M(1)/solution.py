def solution(visited, cnt, arr):
    if cnt==M:
        print(*arr)
    for i in range(1, N+1):
        if visited&(1<<i)==0:
            solution(visited|(1<<i), cnt+1, arr+[i])

N, M = map(int, input().split())
solution(0, 0, [])

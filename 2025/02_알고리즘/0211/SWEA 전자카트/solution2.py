# 백트레킹
def solution(cnt, before, summ):
    global ans
    if cnt == N:
        ans = min(ans, summ+arr[before][0])
        return
    for i in range(N):
        if visited[i]: continue
        visited[i] = True
        solution(cnt+1, i, summ+arr[before][i])
        visited[i]=False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False]*N
    visited[0]=True
    ans = (N+1)*100
    solution(1, 0, 0)
    print(f'#{tc} {ans}')
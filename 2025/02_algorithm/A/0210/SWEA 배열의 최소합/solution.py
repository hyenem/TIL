def solution(visited,idx, summ):
    global ans
    if summ>ans:
        return
    if idx==N:
        ans = min(ans, summ)
        return
    for i in range(N):
        if visited&(1<<i)==0:
            solution(visited|(1<<i), idx+1, summ+arr[idx][i])

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    com = []
    ans = 10*N
    solution(0, 0, 0)
    print(f'#{tc} {ans}')

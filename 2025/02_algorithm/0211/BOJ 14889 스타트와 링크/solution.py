def solution(idx, cnt, dist):
    global ans
    if cnt == N//2:
        for i in range(N):
            for j in range(i+1, N):
                if not start[i] and not start[j]:
                    dist -= S[i][j]+S[j][i]
        ans = min(abs(dist), ans)
        return
    for i in range(idx+1, N):
        start[i]=True
        startset.add(i)
        solution(i, cnt+1, dist+sum([S[s][i]+S[i][s] for s in startset]))
        startset.remove(i)
        start[i]=False

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
start = [False]*(N)
startset={0}
start[0] = True
ans = 100*N
solution(0, 1, 0)
print(ans)
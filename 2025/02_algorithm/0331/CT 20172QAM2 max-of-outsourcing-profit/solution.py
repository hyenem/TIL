N = int(input())
work = [tuple(map(int, input().split())) for _ in range(N)]

DP = [0]*(N+2)
for i, (t, p) in enumerate(work):
    if i+t>(N+2): continue
    for j in range(i+t, N+2):
        DP[j] = max(DP[j], DP[i]+p)
print(DP[N+1])
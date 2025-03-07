N = int(input())
DP = [0] * (N + 1)
for i in range(N):
    t, c = map(int, input().split())
    if i + t < N + 1:
        DP[i + t] = max(DP[i] + c, DP[i+t])
    DP[i+1]= max(DP[i], DP[i+1])

print(DP[-1])

N = int(input())
arr = [[1]*(N)]+[list(map(int, input().split())) for _ in range(N)]
DP = [[[0, 0, 0] for _ in range(N)] for _ in range(N+1)]
DP[1][1][0] = 1
for i in range(1, N+1):
    for j in range(2, N):
        if arr[i][j]==1 : continue
        DP[i][j][0] = DP[i][j-1][0]+DP[i][j-1][2]
        DP[i][j][1] = DP[i-1][j][1]+DP[i-1][j][2]
        if arr[i-1][j]+arr[i][j-1]==0 : DP[i][j][2] = sum(DP[i - 1][j - 1])
print(sum(DP[N][N-1]))
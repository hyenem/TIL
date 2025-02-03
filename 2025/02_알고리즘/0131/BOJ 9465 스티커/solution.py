T = int(input())
for _ in range(T):
    N = int(input())
    arr= [list(map(int, input().split())) for _ in range(2)]
    DP = [[0,0,0] for _ in range(N)]
    DP[0] = [arr[0][0], arr[1][0], 0]
    for i in range(1, N):
        DP[i][0]=max(DP[i-1][1], DP[i-1][2])+arr[0][i]
        DP[i][1] = max(DP[i - 1][0], DP[i - 1][2]) + arr[1][i]
        DP[i][2] = max(DP[i - 1][0], DP[i - 1][1], DP[i - 1][2])
    print(max(DP[N-1]))
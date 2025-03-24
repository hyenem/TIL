N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]
for i in range(N-2,-1, -1):
    DP[i][i+1]=arr[i][0]*arr[i][1]*arr[i+1][1]
    for j in range(i+2, N):
        # for ele in DP:
        #     print(ele)
        # print('_____________-')
        for k in range(i, j):
            tmp = DP[i][k]+DP[k+1][j]+arr[i][0]*arr[k][1]*arr[j][1]
            # print(i, k, j, tmp)
            if DP[i][j]==0:
                DP[i][j]=tmp
            else :
                DP[i][j]=min(DP[i][j], tmp)
print(DP[0][N-1])

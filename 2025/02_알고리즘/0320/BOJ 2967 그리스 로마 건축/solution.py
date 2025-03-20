N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
DP = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='x':
            if i==0 or j==0:
                DP[i][j]=1
            else :
                if DP[i-1][j] and DP[i][j-1] and DP[i-1][j-1]:
                    DP[i][j]=DP[i-1][j-1]+1
                else : DP[i][j]=1

for ele in DP:
    print(ele)
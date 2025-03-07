N = int(input())
arr = [0]+list(map(int, input().split()))
sortedarr = sorted(list(set(arr)))
M = len(sortedarr)

DP = [[0]*(M) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M):
        if arr[i]==sortedarr[j]:
            DP[i][j]=DP[i-1][j-1]+1
        else :
            DP[i][j]=max(DP[i][j-1], DP[i-1][j])

print(DP[N][M-1])
ans = []
x, y = N, M-1
while DP[x][y]!=0:
    if arr[x]==sortedarr[y]:
        ans.append(arr[x])
        x-=1
        y-=1
    elif DP[x][y-1]>DP[x-1][y]:
        y-=1
    else :
        x-=1
print(*reversed(ans))
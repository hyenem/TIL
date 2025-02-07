N = int(input())
arr = [0]+list(map(int, input().split()))
sarr = sorted(list(set(arr)))
DP = [[0]*(N+1) for _ in range(len(sarr))]
for i in range(1, len(sarr)):
    for j in range(1, N+1):
        if arr[j]==sarr[i]:
            DP[i][j]=DP[i-1][j-1]+1
        else :
            DP[i][j]=max(DP[i][j-1], DP[i-1][j])

newDP = [[0]*(N+1) for _ in range(len(sarr))]
arr.reverse()
arr = [0]+arr
arr.pop()
for i in range(1, len(sarr)):
    for j in range(1, N+1):
        if arr[j] == sarr[i]:
            newDP[i][j] = newDP[i - 1][j - 1] + 1
        else:
            newDP[i][j] = max(newDP[i][j - 1], newDP[i - 1][j])

ans = 0
for i in range(1, N+1):
    ans = max(ans, DP[len(sarr)-1][i]+newDP[len(sarr)-1][N+1-i])
print(ans-1)

N = int(input())
arr = [0] + list(map(int, input().split()))
sarr = sorted(list(set(arr)))
DP = [[0]*(len(sarr)) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, len(sarr)):
        if arr[i]==sarr[j]:
            DP[i][j]=DP[i-1][j-1]+arr[i]
        else :
            DP[i][j]=max(DP[i][j-1], DP[i-1][j])
print(DP[N][len(sarr)-1])
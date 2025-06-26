N = int(input())
arr = list(map(int, input().split()))
DP = [1000000]*N
for i in range(0, N):
    DP[i]= (i)*(1+abs(arr[i]-arr[0]))
    for j in range(1, i):
        DP[i]=min(DP[i], max(DP[j], (i-j)*(1+abs(arr[i]-arr[j]))))
print(DP[N-1])
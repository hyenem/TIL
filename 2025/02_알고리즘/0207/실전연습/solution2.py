N, K = map(int, input().split())
arr = [0]+list(map(int,input().split()))
for i in range(1, N+1):
    arr[i]+=arr[i-1]

ans = -100*K
for i in range(K, N+1):
    ans = max(ans , arr[i]-arr[i-K])
print(ans)
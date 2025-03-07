N = int(input())
DP = [0]*(N+1)
# 2에서 부터 올라가면서 최솟값 갱신
for i in range(2,N+1):
    DP[i]=DP[i-1]+1
    if i%3==0: DP[i]= min(DP[i//3]+1, DP[i])
    if i%2==0: DP[i]=min(DP[i//2]+1, DP[i])
print(DP[N])
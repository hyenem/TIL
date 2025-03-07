N =int(input())
arr = [0]+list(map(int, input().split()))
# 해당 수열을 순서바꿔서 만들 수 있는 증가수열을 만들어둠
sortedarr = sorted(list(set(arr)))
M = len(sortedarr)
DP=[[0]*(M) for _ in range(N+1)]
#arr의 i와 sortedarr[j]가 같으면 길이가 하나 추가됨
for i in range(1,N+1):
    for j in range(1,M):
        if arr[i]==sortedarr[j]:
            DP[i][j]=DP[i-1][j-1]+1
        else :
            DP[i][j]=max(DP[i-1][j],DP[i][j-1])
print(DP[N][M-1])
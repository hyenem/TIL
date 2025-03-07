data1 = [0]+list(input())
data2 = [0]+list(input())
N = len(data1)
M = len(data2)
DP = [[0]*M for _ in range(N)]
for i in range(1, N):
    for j in range(1, M):
        if data1[i]==data2[j]:
            DP[i][j]=DP[i-1][j-1]+1
        else :
            DP[i][j]=max(DP[i-1][j], DP[i][j-1])

lenth = DP[-1][-1]

print(lenth)
if lenth!=0:
    x, y = N-1, M-1
    ans = []
    while DP[x][y]!=0:
        if data1[x]==data2[y]:
            ans.append(data1[x])
            x-=1
            y-=1
        elif DP[x-1][y]==DP[x][y]:
            x-=1
        else:
            y-=1
    print(''.join(reversed(ans)))


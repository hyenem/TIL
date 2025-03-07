def calDP(i, j):
    x1, y1 = arr[i]
    x2, y2 = arr[j]
    if x1>x2 or y1>y2: return 0
    newDP=[[0]*(y2-y1+2) for _ in range(x2-x1+2)]
    newDP[1][1]=1
    for x in range(1, x2-x1+2):
        for y in range(1, y2-y1+2):
            if (x1+x-1, y1+y-1) in dic and dic[(x1+x-1, y1+y-1)] not in {i,j}: continue
            newDP[x][y]+=newDP[x-1][y]+newDP[x][y-1]
    return newDP[-1][-1]


N, M, C = map(int, input().split())
DP = [[0]*(C+2) for _ in range(C+2)]
arr = [(1,1)]+[tuple(map(int, input().split())) for _ in range(C)]+[(N, M)]
dic ={}
for i in range(1, C+1):
    dic[arr[i]]=i
for i in range(0, C+2):
    for j in range(i+1, C+2):
        DP[i][j]=calDP(i, j)
if (1, 1) in dic:
    for i in range(C+2):
        if i!=dic[(1,1)] : DP[0][i]=0
if (N, M)in dic:
    for i in range(C + 2):
        if i != dic[(N, M)]: DP[i][C+1] = 0

finalDP = [DP[0]]+[[0]*(C+2) for _ in range(C+1)]
for i in range(1, C+2):
    for j in range(i+1, C+2):
        for k in range(0, j):
            finalDP[i][j] += finalDP[i-1][k]*DP[k][j]
ans = []
for i in range(C+1):
    ans.append(finalDP[i][C+1]%1000007)
print(*ans)
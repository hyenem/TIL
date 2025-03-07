DP = [[[1]*21 for _ in range(21)] for _ in range(21)]
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i<j<k:
                DP[i][j][k]=DP[i][j][k-1]+DP[i][j-1][k-1]-DP[i][j-1][k]
            else :
                DP[i][j][k] = DP[i-1][j][k]+DP[i-1][j-1][k]+DP[i-1][j][k-1]-DP[i-1][j-1][k-1]

while True:
    a, b, c = map(int, input().split())
    if a==b==c==-1: break

    print(f'w({a}, {b}, {c}) = ', end='')
    if a<=0 or b<=0 or c<=0:
        print(1)
    elif a>20 or b>20 or c>20:
        print(DP[20][20][20])
    else :
        print(DP[a][b][c])
for ele in DP:
    print(ele)
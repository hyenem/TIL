N, M = map(int, input().split())
day = [list(map(int, input().split())) for _ in range(M)]
lst = [1]*(2*N-1)

for n in range(M):
    zero, one, two = day[n]
    for i in range(zero, zero+one):
        lst[i]+=1
    for i in range(zero+one, 2*N-1):
        lst[i]+=2

arr = [[0]*N for _ in range(N)]
for i in range(N-1, -1, -1):
    arr[i][0] = lst[N-1-i]
for i in range(N):
    for j in range(1, N):
        arr[i][j]=lst[N-1+j]

for ele in arr:
    print(*ele)
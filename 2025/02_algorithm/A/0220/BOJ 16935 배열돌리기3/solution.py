def fill(i, j, ni, nj):
    for x in range(N//2):
        for y in range(M//2):
            newarr[ni+x][nj+y] = arr[i+x][j+y]

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for do in map(int, input().split()):
    if do == 1:
        arr.reverse()
    elif do==2:
        for i in range(N):
            arr[i].reverse()
    elif do==3:
        arr.reverse()
        arr = [list(ele) for ele in zip(*arr)]
        N, M = M, N
    elif do==4:
        for i in range(N):
            arr[i].reverse()
        arr = [list(ele) for ele in zip(*arr)]
        N, M = M, N
    elif do==5 :
        newarr = [[0]*M for _ in range(N)]
        fill(0,0,0,M//2)
        fill(N//2, 0, 0, 0)
        fill(N//2, M//2, N//2, 0)
        fill(0, M//2, N//2, M//2)
        arr = newarr
    else :
        N, M = M, N
        newarr = [[0]*M for _ in range(N)]
        arr = [list(ele) for ele in zip(*arr)]
        fill(0,0,0,M//2)
        fill(N//2, 0, 0, 0)
        fill(N//2, M//2, N//2, 0)
        fill(0, M//2, N//2, M//2)
        arr = [list(ele) for ele in zip(*newarr)]
        N, M = M, N

for ele in arr:
    print(*ele)

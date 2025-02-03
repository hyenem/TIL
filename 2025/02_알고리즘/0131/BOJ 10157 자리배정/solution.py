C, R = map(int, input().split())
K = int(input())
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
arr = [[1]*(C+2)]+[[1]+[0]*(C)+[1] for _ in range(R)]+[[1]*(C+2)]
if K>C*R:
    print(0)
else :
    nx = R
    ny = 1
    arr[nx][ny]=1
    K-=1
    direction = 0
    while K>0:
        if arr[nx+dx[direction]][ny+dy[direction]]==1:
            direction = (direction+1)%4
        nx += dx[direction]
        ny += dy[direction]
        arr[nx][ny]=1
        K-=1
    print(ny, R+1-nx)
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dxdy = ((1, 0), (-1, 0), (0, 1), (0, -1))
ncnt = 0
ycnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]=='@':
            sx, sy = i, j
        elif arr[i][j] in {'*', '#'}:
            ncnt += 1

broken = []
for dx, dy in dxdy:
    for k in range(1,3):
        nx, ny = sx+k*dx, sy+k*dy
        if not(0<=nx<N and 0<=ny<M): break
        if arr[nx][ny]=='|': break
        if arr[nx][ny]=='*':
            broken.append((nx, ny))
            arr[nx][ny]='.'
        elif arr[nx][ny]=='#':
            arr[nx][ny]='*'

while broken:
    x, y = broken.pop()
    ycnt += 1
    ncnt -= 1
    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M): continue
        if arr[nx][ny]=='*':
            broken.append((nx, ny))
            arr[nx][ny]='.'
        elif arr[nx][ny]=='#':
            arr[nx][ny]='*'
print(ycnt, ncnt)
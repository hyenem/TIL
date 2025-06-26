N, M = map(int,input().split())
arr = [list(map(int, input())) for _ in range(N)]

# 해당 점까지의 거리와 점의 좌표를 저장
q = [(1, 0, 0)]
arr[0][0]=0

dx=(-1, 1, 0, 0)
dy=(0, 0, -1, 1)
while q:
    c, x, y = q.pop(0)
    if (x, y)==(N-1, M-1):
        ans = c
        break
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<N and 0<=ny<M and arr[nx][ny]==1:
            arr[nx][ny]=0
            q.append((c+1, nx, ny))
print(ans)
def btk(x, y, cnt):
    global ans
    ans = max(cnt, ans)
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and not num[arr[nx][ny]]:
            visited[nx][ny]=True
            num[arr[nx][ny]]=True
            btk(nx, ny, cnt+1)
            visited[nx][ny]=False
            num[arr[nx][ny]]=False

N, M = map(int, input().split())
arr = [list(map(lambda x:ord(x)-ord('A'),input())) for _ in range(N)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[False]*M for _ in range(N)]
num = [False]*26

ans = 0
visited[0][0]=True
num[arr[0][0]]=True
btk(0, 0, 1)

print(ans)
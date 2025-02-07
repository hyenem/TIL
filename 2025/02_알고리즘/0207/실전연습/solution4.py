from collections import deque

N, M = map(int, input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

cnt = 0
maximum = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]==0: continue
        cnt+=1
        q=deque()
        q.append((i, j))
        arr[i][j]=0
        thiscnt = 1
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0<=nx<N and 0<=ny<M and arr[nx][ny]==1:
                    arr[nx][ny]=0
                    q.append((nx, ny))
                    thiscnt +=1
        maximum = max(maximum, thiscnt)
print(cnt)
print(maximum)
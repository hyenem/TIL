from collections import deque

M, N = map(int,input().split())
q = deque()
arr = [list(map(int, input().split())) for _ in range(N)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 남은 익은 토마토 개수를 저장
cnt = N*M

for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            # 며칠 지나서, 어느좌표의 토마토가 익는지
            q.append((0, i, j))
            # 이미 익은 토마토 반영
            cnt-=1
        elif arr[i][j]==-1:
            # 토마토가 안들어있는 칸 반영
            cnt -= 1

while q:
    t, x, y = q.popleft()
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<N and 0<=ny<M and arr[nx][ny]==0:
            arr[nx][ny] = 1
            q.append((t+1, nx, ny))
            cnt -= 1

# 안익은 토마토가 남았으면
if cnt!=0:
    print(-1)
else :
    print(t)
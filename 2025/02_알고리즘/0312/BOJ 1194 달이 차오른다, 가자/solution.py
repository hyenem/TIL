from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='0':
            x, y = i, j
            break

q = deque([(0, x, y, 0)])
visited = [[set() for _ in range(M)] for _ in range(N)]
visited[x][y].add(0)
while q:
    t, x, y, key = q.popleft()
    if arr[x][y]=='1':
        print(t)
        break
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M): continue
        if key in visited[nx][ny]: continue
        if arr[nx][ny]=='#': continue
        if ord('A')<=ord(arr[nx][ny])<=ord('F'):
            if not (key>>ord(arr[nx][ny])-ord('A'))&1: continue
        if ord('a')<=ord(arr[nx][ny])<=ord('f'):
            q.append((t+1, nx, ny, key|(1<<(ord(arr[nx][ny])-ord('a')))))
            visited[nx][ny].add(key|(1<<(ord(arr[nx][ny])-ord('a'))))
        else:
            visited[nx][ny].add(key)
            q.append((t+1, nx, ny, key))
else :
    print(-1)

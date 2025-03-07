from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


visited= [[0]*M for _ in range(N)]
visited[0][0]=2
q = deque([(0, 0)])
time = -1

while q:

    time += 1

    tmparr = [ele[:] for ele in arr]
    nq = deque()
    while q:
        x, y = q.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M): continue
            if visited[nx][ny]==2: continue

            if tmparr[nx][ny]==0:
                q.append((nx, ny))
                visited[nx][ny]=2
            else :
                visited[nx][ny]+=1
                if visited[nx][ny]==2:
                    nq.append((nx, ny))
                    arr[nx][ny]=0
    q = nq


print(time)

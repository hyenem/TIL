from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

beforecheese = sum(map(sum, arr))

visited= [[0]*M for _ in range(N)]
visited[0][0]=1
q = deque([(0, 0)])
time = 0
while True:

    tmparr = [ele[:] for ele in arr]
    thischeese = 0
    nq = deque()
    while q:
        x, y = q.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M): continue
            if visited[nx][ny]: continue

            if tmparr[nx][ny]==0:
                q.append((nx, ny))
                visited[nx][ny]=1
            else :
                visited[nx][ny]=1
                nq.append((nx, ny))
                thischeese += 1
                arr[nx][ny]=0
    if thischeese==0:
        break
    else :
        q = nq
        time += 1
        beforecheese = thischeese

print(time)
print(beforecheese)
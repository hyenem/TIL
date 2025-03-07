from collections import deque

N, M, T = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dxdy = ((1, 0), (-1, 0), (0, 1), (0, -1))
for i in range(N):
    for j in range(M):
        if arr[i][j]=='G':
            x, y = i, j

q = deque([(T, x, y, 0, set())])
ans = 0
while q:
    t, x, y, cnt, s = q.popleft()
    if t==0:
        ans = max(ans, cnt)
        continue
    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M): continue
        if arr[nx][ny]=='#': continue
        if arr[nx][ny]=='S':
            if (nx, ny) in s: continue

            ns = set()
            for ele in s:
                ns.add(ele)
            ns.add((nx, ny))
            q.append((t-1, nx, ny, cnt+1, ns))
        else :
            q.append((t-1, nx, ny, cnt, s))

print(ans)
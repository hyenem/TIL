import heapq

M, N, K = map(int, input().split())
switch = [list(map(int, input().split())) for _ in range(K)]+[[M, N]]
switchidx = [[[] for _ in range(N)], [[] for _ in range(M)]]
visited = [-1]*(K+1)

for i in range(K+1):
    y, x = switch[i]
    switch[i] = (x-1, y-1)
    switchidx[0][x - 1].append(i)
    switchidx[1][y - 1].append(i)

q = []
for i in switchidx[1][0]:
    heapq.heappush(q, (switch[i][0], 1, i, 1))
    visited[i] = switch[i][0]
switchidx[1][0].clear()

ans = -1
while q:
    t, d, idx, flag = heapq.heappop(q)
    x, y = switch[idx]
    if x==N-1 and y==M-1:
        ans = t
        break

    if visited[idx]!=-1 and visited[idx]<t: continue

    delidx = []
    if d==1:
        for k in range(len(switchidx[0][x])):
            ni = switchidx[0][x][k]
            ny = switch[ni][1]
            if flag and y<=ny:
                delidx.append(k)
            else : flag=0

            nt = t+1+abs(y-ny)
            if visited[ni]==-1 or visited[ni]>nt:
                visited[ni]= nt
                heapq.heappush(q, (nt, 0, ni, flag))
        while delidx:
            k = delidx.pop()
            del switchidx[0][x][k]
    else:
        for k in range(len(switchidx[1][y])):
            ni = switchidx[1][y][k]
            nx = switch[ni][0]
            if flag and x<=nx:
                delidx.append(k)
            else : flag = 0
            nt = t+1+abs(x-nx)
            if visited[ni]==-1 or visited[ni]>nt:
                visited[ni]=nt
                heapq.heappush(q, (nt, 1, ni, flag))
        while delidx:
            k = delidx.pop()
            del switchidx[1][y][k]

print(ans)
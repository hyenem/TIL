import heapq

def check_visited(x, y, l, r):
    for i in range(l+1):
        for j in range(r+1):
            visited[x][y][l][r]=True

def bfs():
    global ans
    while q:
        rest, x, y, l, r = heapq.heappop(q)
        thisd = direction[arr[x][y]]
        for d in range(4):
            nx, ny = x + dxdy[d][0], y + dxdy[d][1]
            if not (0 <= nx < R and 0 <= ny < C): continue
            if d == thisd:
                if nx == R - 1 and ny == C - 1:
                    ans = 'Yes'
                    return
                if visited[nx][ny][l][r]: continue
                check_visited(nx,ny,l,r)
                heapq.heappush(q, (rest, nx, ny, l, r))
            else:
                rdist = (d - thisd + 4) % 4
                if r >= rdist:
                    if nx == R - 1 and ny == C - 1:
                        ans = 'Yes'
                        return
                    if not visited[nx][ny][l][r - rdist]:
                        check_visited(nx, ny, l, r-rdist)
                        heapq.heappush(q, (rest+rdist, nx, ny, l, r - rdist))
                if l >= 4 - rdist:
                    if nx == R - 1 and ny == C - 1:
                        ans = 'Yes'
                        return
                    if not visited[nx][ny][l - 4 + rdist][r]:
                        check_visited(nx, ny, l-4+rdist,r)
                        heapq.heappush(q,(rest+4-rdist, nx, ny, l - 4 + rdist, r))

direction ={'U':0, 'D':2, 'L':3, 'R':1}
dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[[[False]*(K+1) for _ in range(K+1)] for _ in range(C)] for _ in range(R)]
check_visited(0,0,K,K)
q =[(-2*K, 0, 0, K, K)]
ans = 'No'
bfs()
print(ans)
import heapq
from collections import deque

def gotoanother(xy):
    i, j = xy
    q = [(0, i, j)]
    visited = [[0] * (M + 2) for _ in range(N + 2)]
    visited[i][j] = 1

    while q:
        cnt, x, y = heapq.heappop(q)
        if (x, y)!=(i, j) and arr[x][y] == '$':
            return cnt

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny]: continue
            if arr[nx][ny] == '*': continue

            visited[nx][ny] = 1
            if arr[nx][ny] in {'.', '$'}:
                heapq.heappush(q, (cnt, nx, ny))
            else:
                heapq.heappush(q, (max(cnt, arr[nx][ny]), nx, ny))
    return N * M

def gotogoal(xy):
    x, y = xy
    q = [(x, y)]
    visited = [[0]*(M+2) for _ in range(N+2)]
    visited[x][y]=1

    cnt = M*N

    while q:
        x, y = q.pop()
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if nx in {0, N+1} or ny in {0, M+2}:
                return 0

            if visited[nx][ny] or arr[nx][ny]=='*': continue

            visited[nx][ny]=1
            if arr[nx][ny] in {'.', '$'}:
                q.append((nx, ny))
            else:
                cnt = min(cnt, arr[nx][ny])

    return cnt


T = int(input())
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
for _ in range(T):
    N, M = map(int, input().split())
    arr = [[0]*M]+[[0]+list(input())+[0] for _ in range(N)]+[[0]*M]

    q = deque([(0, 0, 0)])
    visited = [[0]*(M+2) for _ in range(N+2)]
    visited[0][0]=1

    while q:
        x, y, cnt = q.popleft()
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M) or visited[nx][ny]: continue
            if arr[nx][ny] == '*': continue

            visited[nx][ny]=1
            if arr[nx][ny] == '#':
                arr[nx][ny]=cnt+1
                q.append((nx, ny, cnt+1))
            else :
                q.appendleft((nx, ny, cnt))

    prisoner = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='$':
                prisoner.append((i, j))

    ans1 = gotoanother(prisoner[0])

    ans2 = gotogoal(prisoner[0])
    ans2 += gotogoal(prisoner[1])

    print(ans1, ans2)
    print(min(ans1, ans2))

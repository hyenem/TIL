from collections import deque

T = int(input())
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
for _ in range(T):
    N, M = map(int, input().split())
    arr = [['.']*(M+2)] + [['.']+list(input())+['.'] for _ in range(N)] + [['.']*(M+2)]
    prisoner = []
    door = []
    for i in range(N+2):
        for j in range(M+2):
            if arr[i][j]=='$':
                prisoner.append((i, j))
            elif arr[i][j]=='#':
                door.append((i, j))
                arr[i][j]=0

    q = deque([(0, 0, 0)])
    visited = [[0]*(M+2) for _ in range(N+2)]
    visited[0][0]=1
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<N+2 and 0<=ny<M+2) or visited[nx][ny]: continue
            if arr[nx][ny]=='*': continue

            visited[nx][ny]=1
            if arr[nx][ny] in {'.', '$'}:
                q.appendleft((nx, ny, cnt))
            else:
                arr[nx][ny]=cnt+1
                q.append((nx, ny, cnt+1))

    visited = [[0]*(M+2) for _ in range(N+2)]

    ans1 = M*N
    q = deque([(prisoner[0][0], prisoner[0][1], 0)])
    visited = [[0]*(M+2) for _ in range(N+2)]
    visited[prisoner[0][0]][prisoner[0][1]]=1
    while q:
        x, y, cnt = q.popleft()
        if x in {0, N+1} or y in {0, M+1}:
            ans1 = min(ans1, cnt)
            continue

        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < N+2 and 0 <= ny < M+2) or visited[nx][ny]: continue
            if arr[nx][ny] == '*': continue

            visited[nx][ny] = 1
            if arr[nx][ny] in {'.', '$'}:
                q.appendleft((nx, ny, cnt))
            else:
                arr[nx][ny]+=cnt
                q.append((nx, ny, cnt + 1))

    ans2 = M * N
    q = deque([(prisoner[1][0], prisoner[1][1], 0)])
    visited[prisoner[1][0]][prisoner[1][1]] += 2
    while q:
        x, y, cnt = q.popleft()
        if x in {0, N + 1} or y in {0, M + 1}:
            ans2 = min(ans2, cnt)
            continue

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N+2 and 0 <= ny < M+2) or visited[nx][ny]>1: continue
            if arr[nx][ny] == '*': continue

            visited[nx][ny] += 2
            if arr[nx][ny] in {'.', '$'}:
                q.appendleft((nx, ny, cnt))
            else:
                arr[nx][ny]+=cnt
                q.append((nx, ny, cnt + 1))

    ans3 = M*N
    for x, y in door:
        if visited[x][y]!=3: continue
        ans3 = min(arr[x][y], ans3)
    print(min(ans1+ans2, ans3))
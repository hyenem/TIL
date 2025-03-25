from collections import deque

switch = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

while True:
    N, M = map(int, input().split())
    if N==M==0: break

    arr = [list(map(lambda x: switch[x], input())) for _ in range(N)]
    K = int(input())
    box = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(K)]

    visited = [[set() for _ in range(M)] for _ in range(N)]
    q = deque([(0, 0, 0, 0, 0)])

    while q:
        t, x, y, b, r = q.popleft()
        if x==N-1 and y==M-1 and b==((1<<len(box))-1):
            print(t)
            break

        if r<3: q.append((t+1, x, y, b, r+1))

        d = (arr[x][y]+t)%4
        dx, dy = dxdy[d]
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < M): continue
        if b in visited[nx][ny]: continue

        visited[nx][ny].add(b)
        for i in range(len(box)):
            if (nx, ny) == box[i]:
                q.append((t + 1, nx, ny, b | (1 << i), 0))
                break
        else:
            q.append((t + 1, nx, ny, b, 0))


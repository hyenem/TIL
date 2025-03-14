N, M = map(int, input().split())
arr = list(map(list, zip(*[list(map(int, input())) for _ in range(N)][::-1])))
while True:
    stack = []
    visited = [[0]*N for _ in range(10)]
    for i in range(10):
        for j in range(N):
            if arr[i][j]==0:
                break
            if visited[i][j]: continue

            q = [(i, j)]
            visited[i][j]=1
            idx = 0
            while idx<len(q):
                x, y = q[idx]
                idx += 1
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nx, ny = x+dx, y+dy
                    if not(0<=nx<10 and 0<=ny<N): continue
                    if visited[nx][ny]: continue
                    if arr[nx][ny]==arr[x][y]:
                        visited[nx][ny]=1
                        q.append((nx, ny))
            if len(q)<M: continue

            stack.extend(q)

    if len(stack)==0:
        break

    stack.sort()
    while stack:
        x, y = stack.pop()
        del arr[x][y]
        arr[x].append(0)

for ele in list(zip(*arr))[::-1]:
    print(''.join(map(str, ele)))
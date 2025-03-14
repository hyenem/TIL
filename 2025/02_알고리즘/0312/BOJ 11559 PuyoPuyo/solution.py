arr = list(map(list, zip(*[list(input()) for _ in range(12)][::-1])))

ans = 0
while True:
    stack = []
    visited = [[0]*12 for _ in range(6)]
    for i in range(6):
        for j in range(12):
            if arr[i][j]=='.':
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
                    if not(0<=nx<6 and 0<=ny<12): continue
                    if visited[nx][ny]: continue
                    if arr[nx][ny]==arr[x][y]:
                        visited[nx][ny]=1
                        q.append((nx, ny))
            if len(q)<=3: continue

            stack.extend(q)

    if len(stack)==0:
        break
    ans += 1
    stack.sort()
    while stack:
        x, y = stack.pop()
        del arr[x][y]
        arr[x].append('.')

print(ans)
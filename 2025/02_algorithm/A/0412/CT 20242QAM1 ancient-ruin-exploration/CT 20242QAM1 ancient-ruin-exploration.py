from collections import deque

K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
next = deque(map(int, input().split()))

anss = []
for _ in range(K):
    ans = 0

    rotate = (-1, -4, -1, -1)
    narr, stack = arr, []
    for sx in range(3):
        for sy in range(3):
            for r in range(4):
                tmparr = [ele[:] for ele in arr]
                for x in range(3):
                    for y in range(3):
                        tmparr[sx+x][sy+y] = arr[sx+2-y][sy+x]
                arr = tmparr

                if r==3: continue

                visited = [[0]*5 for _ in range(5)]
                tmpstack = []
                for i in range(5):
                    for j in range(5):
                        if visited[i][j]: continue
                        visited[i][j]=1
                        q = [(i, j)]
                        qidx = 0
                        while qidx<len(q):
                            x, y = q[qidx]
                            qidx += 1

                            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                                nx, ny = x+dx, y+dy
                                if not(0<=nx<5 and 0<=ny<5): continue
                                if visited[nx][ny]: continue
                                if arr[i][j]==arr[nx][ny]:
                                    visited[nx][ny]=1
                                    q.append((nx, ny))
                        if len(q)>=3:
                            tmpstack.extend(q)
                if rotate<(len(tmpstack), -r, -sy, -sx):
                    rotate = (len(tmpstack), -r, -sy, -sx)
                    narr = [ele[:] for ele in arr]
                    stack = tmpstack

    if not stack: break

    arr = narr
    ans += len(stack)
    for x, y in stack:
        arr[x][y]=0

    for j in range(5):
        for i in range(4, -1, -1):
            if arr[i][j]==0:
                arr[i][j]=next.popleft()

    while True:
        visited = [[0]*5 for _ in range(5)]
        flag = 0
        for i in range(5):
            for j in range(5):
                if visited[i][j]: continue
                visited[i][j]=1
                num = arr[i][j]
                q = [(i, j)]
                qidx = 0
                while qidx<len(q):
                    x, y = q[qidx]
                    qidx += 1

                    for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                        nx, ny = x+dx, y+dy
                        if not(0<=nx<5 and 0<=ny<5): continue
                        if visited[nx][ny]: continue
                        if arr[nx][ny]==num:
                            q.append((nx, ny))
                            visited[nx][ny]=1

                if len(q)>=3:
                    flag = 1
                    ans += len(q)
                    for x, y in q:
                        arr[x][y]=0

        if not flag: break
        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j]==0:
                    arr[i][j]=next.popleft()
    anss.append(ans)
print(*anss)
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = set()
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0: continue
            visited.add((i, j))
            q.append((i, j, arr[i][j], arr[i][j]))

    for _ in range(K):
        if len(q)==0: break
        dic = {}
        nq = deque()
        while q:
            x, y, life, cnt = q.popleft()
            if cnt-1>-life:
                nq.append((x, y, life, cnt-1))

            if cnt==0:
                for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nx, ny = x+dx, y+dy
                    if (nx, ny) in visited: continue
                    if (nx, ny) not in dic:
                        dic[(nx,ny)]=0
                    dic[(nx, ny)]=max(dic[(nx, ny)], life)


        for x, y in dic:
            visited.add((x, y))
            nq.append((x, y, dic[(x, y)], dic[(x, y)]))

        q = nq

    print(f'#{tc} {len(q)}')
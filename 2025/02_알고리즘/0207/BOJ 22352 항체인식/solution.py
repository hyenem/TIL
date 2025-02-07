# 차로 접근해서 0이 아닌애들이 나뉘어져있는지 아닌지를 채크하면 되겠다고 생각했는데
# 2에서 4, 1에서 3으로 바뀌는 애들이 인접해있거나 그런경우도 있나 싶어서,, 위험하다생각
from collections import deque

def solution():
    cnt = 0
    dxdy = ((0, 1), (0, -1), (1, 0), (-1, 0))
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if before[i][j] == after[i][j] or visited[i][j]:
                continue
            cnt += 1
            if cnt==2:
                return 'NO'
            q = deque()
            q.append((i, j))
            visited[i][j]=True
            while q:
                x, y = q.popleft()
                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < N and 0 <= ny < M):
                        continue
                    if before[nx][ny] == before[x][y] and not visited[nx][ny]:
                        if after[nx][ny] == after[i][j]:
                            visited[nx][ny]=True
                            q.append((nx, ny))
                        else:
                            return 'NO'
    return 'YES'

N, M = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(N)]
after = [list(map(int, input().split())) for _ in range(N)]

ans = solution()
print(ans)

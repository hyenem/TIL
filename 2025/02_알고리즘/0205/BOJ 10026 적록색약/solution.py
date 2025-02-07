from collections import deque

N = int(input())

arr = [input() for _ in range(N)]
visited_distinct = [[False]*N for _ in range(N)]
visited_mix = [[False]*N for _ in range(N)]
distinct = 0
mix = 0


dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

q = deque()
for i in range(N):
    for j in range(N):

        # 적록색약이 없는 경우
        if not visited_distinct[i][j]:
            distinct += 1
            q.append((i, j))
            visited_distinct[i][j]=True
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if not(0<=nx<N and 0<=ny<N) or visited_distinct[nx][ny]:
                        continue
                    if arr[nx][ny] != arr[x][y]:
                        continue
                    visited_distinct[nx][ny]=True
                    q.append((nx, ny))

        # 적록색약이 있는 경우
        if not visited_mix[i][j]:
            mix += 1
            visited_mix[i][j]=True
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if not(0<=nx<N and 0<=ny<N) or visited_mix[nx][ny]:
                        continue
                    # 적록색약이 있는 경우는 B와 비교
                    if (arr[nx][ny]=='B')!=(arr[x][y]=='B'):
                        continue
                    visited_mix[nx][ny]=True
                    q.append((nx, ny))
print(distinct, mix)
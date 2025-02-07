# 나이트의 이동 방향
dx = (1, 1, 2, 2, -1, -1, -2, -2)
dy = (2, -2, 1, -1, 2, -2, 1, -1)

T = int(input())
for _ in range(T):
    I = int(input())
    sx, sy = map(int, input().split())
    end = tuple(map(int, input().split()))
    q = [(0, sx, sy)]
    visited = [[False]*I for _ in range(I)]
    visited[sx][sy]=True
    while q:
        c, x, y = q.pop(0)
        if (x, y)==end:
            ans = c
            break
        for k in range(8):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<I and 0<=ny<I:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append((c+1, nx, ny))
    print(ans)
from collections import deque

T = int(input())
# 각 파이프 번호 별 빠져 나갈 수 있는 방향
dir = [0, ((0,1), (0, -1), (1, 0), (-1, 0)),\
       ((1, 0),(-1, 0)),\
       ((0,1), (0, -1)),\
       ((0,1), (-1, 0)),\
       ((0,1), (1, 0)),\
       ((0, -1), (1, 0)),\
       ((0, -1), (-1, 0))]

for tc in range(1, T+1):
    N, M, R, C, L = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited=[[0]*M for _ in range(N)]

    # 멘홀 뚜껑부터 1시간 뒤
    q = deque([(1, R, C)])
    visited[R][C]=1
    ans = 1
    while q:
        t, x, y = q.popleft()
        # 시간이 L이 되면 더이상 추가할 일이 없음
        if t==L: break

        for dx, dy in dir[arr[x][y]]:
            nx, ny = x+dx, y+dy
            if not (0<=nx<N and 0<=ny<M): continue
            if visited[nx][ny]: continue
            if arr[nx][ny]==0: continue
            # 다음칸이 아직 방문 안한 파이프 일 떄,
            # 그 파이프에서 지금 파이프로 오는 길이 뚫려 있으면
            if (-dx, -dy) in dir[arr[nx][ny]]:
                # 답 한 칸 추가, 방문 표시, q에 추가
                ans += 1
                visited[nx][ny]=1
                q.append((t+1, nx, ny))
    print(f'#{tc} {ans}')

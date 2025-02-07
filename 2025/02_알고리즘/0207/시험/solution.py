from collections import deque

T = int(input())


def bfs(si, sj):
    q = []
    q = deque()
    v = [[0] * N for _ in range(N)]
    q.append((si, sj))
    v[si][sj] = 1
    arr[si][sj] = 0

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                arr[ni][nj] = 0
    for ele in v:
        print(ele)
    return v[ci][cj]


for tc in range(1, T + 1):
    # N이 행, M이 열
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 처음 걸린 교육생 좌표
    si, sj = map(int, input().split())
    # 좌표 처리
    si = si - 1
    sj = sj - 1
    ans = bfs(si, sj)

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
    print(f'#{tc} {ans} {cnt}')

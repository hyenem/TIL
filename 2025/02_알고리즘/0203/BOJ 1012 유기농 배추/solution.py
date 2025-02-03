import sys
sys.setrecursionlimit(10000)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def dfs(i, j):
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
            visited[ni][nj]=True
            dfs(ni, nj)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    location = []
    visited = [[True]*M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        # 배추가 있는 곳은 미방문으로 설정
        visited[i][j] = False
        # 배추 위치도 저장
        location.append((i, j))
    ans = 0
    # 배추위치를 돌면서
    # 아직 방문 안한 배추면 dfs로 연결된 애를 다 방문표시
    # 한 덩어리 돌때마다 답 하나씩 올려주기
    for loc in location:
        if not visited[loc[0]][loc[1]]:
            ans += 1
            visited[loc[0]][loc[1]] = True
            dfs(loc[0], loc[1])

    print(ans)
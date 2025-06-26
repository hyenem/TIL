# 문제,,,꼼꼼히,,,읽기,,,
# 제일 왼쪽에서만 출발함!!!

N, M = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = [list(map(int, input().split())) for _ in range(N)]
# 각 뱡향별로 무한루프도는 길이면 1, 안도는 길이면 -1 저장
visited = [[[0] * 4 for _ in range(M)] for _ in range(N)]
ans = []
for i in range(N):
    if visited[i][0][0] != 0: continue
    # 아직 방문하지 않았으면
    d = 0
    stack = [(i, 0, 0)]
    x, y = i, 0
    visited[i][0][0] = 1
    while True:
        x, y = x + arr[x][y] * dx[d], y + arr[x][y] * dy[d]
        d = (d + 1) % 4

        # 범위 바깥으로 나가면 지금까지 왔던 길 다 -1로 만들기
        if not (0 <= x < N and 0 <= y < M):
            while stack:
                x, y, d = stack.pop()
                visited[x][y][d] = -1
            break
        # 가다가 -1 만나면 어차피 빠져나가는 길
        # 지금까지 왔던 길 다 -1 만들기
        if visited[x][y][d] == -1:
            while stack:
                x, y, d = stack.pop()
                visited[x][y][d] = -1
            break
        # 이번에 진행중인 길이거나 이미 무한루프를 도는 칸, 방향임이 확인되면
        # 정답에 해당 길 중에서 방향도 0, 열도 0인 경우 다 추가해주기
        elif visited[x][y][d] == 1:
            while stack:
                x, y, d = stack.pop()
                if d == 0 and y == 0: ans.append(x + 1)
            break
        # 아직 해당칸을 해당 방향으로 안가봤으면
        # 이번에 가는 길 1로 표시하고 stack에 추가
        else:
            visited[x][y][d] = 1
            stack.append((x, y, d))

print(len(ans))
print(*sorted(ans))
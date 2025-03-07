N, M = map(int, input().split())
x, y, d = map(int, input().split())
# 방향이 반시계방향으로 설정해놨는데, 입력은 시계방향으로 주어짐
d = (4-d)%4
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
ans = 0

while True:
    # 내 칸을 아직 청소 안했으면 청소하기
    if not arr[x][y]:
        ans += 1
        arr[x][y]=2
    # 반시계방향으로 보기
    for _ in range(4):
        d = (d + 1) % 4
        dx, dy = dxdy[d]
        nx, ny = x+dx, y+dy
        if arr[nx][ny]: continue
        x, y = nx, ny
        break
    else :
        # 네 방향이 다 청소안된 빈칸이 아니면
        # 후진 할 수 있으면 하고 아니면 끝내기
        if arr[x-dxdy[d][0]][y-dxdy[d][1]]!=1:
            x, y = x - dxdy[d][0], y - dxdy[d][1]
        else : break
print(ans)
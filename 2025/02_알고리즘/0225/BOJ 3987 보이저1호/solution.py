N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
px, py = map(lambda x: int(x) - 1, input().split())
dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = ['U', 'R', 'D', 'L']
maxd = -1
maxtime = 0

for sd in range(4):
    time = 0
    d = sd
    x, y = px, py
    # 전체를 가로 또는 세로로 지나가는(2번)것 이상으로 지나갈 수 없음
    # 그 이상이면 무조건 무한 루프이므로 2*N*M까지만 while문 돌기
    while time < 2 * N * M + 1:
        time += 1
        x, y = x + dxdy[d][0], y + dxdy[d][1]

        # 블랙홀을 만나거나 범위 바깥으로 나가면 끝내기
        if not (0 <= x < N and 0 <= y < M) or arr[x][y] == 'C':
            break

        # 방향전환
        if arr[x][y] == '/':
            if d == 2 or d == 3:
                d = 5 - d
            else:
                d = 1 - d
        elif arr[x][y] == '\\':
            d = 3 - d

    # 무한 반복
    if time == 2 * N * M + 1:
        print(direction[sd])
        print('Voyager')
        break
    # 최대시간, 방향 갱신
    if time > maxtime:
        maxtime = time
        maxd = sd
else:
    print(direction[maxd])
    print(maxtime)
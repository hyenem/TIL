def btk(cnt, bx, by):
    global ans

    if cnt == goal:
        for j in range(1, N + 1):
            res = j
            for i in range(1, H + 1):
                res = res + move[i][res]
            if res != j:
                return False
        return True

    for j in range(by + 1, N):
        if move[bx][j] or move[bx][j + 1]: continue

        move[bx][j], move[bx][j + 1] = 1, -1
        if btk(cnt + 1, bx, j):
            return True
        move[bx][j], move[bx][j + 1] = 0, 0

    for i in range(bx + 1, 1 + H):
        for j in range(1, N):
            if move[i][j] or move[i][j + 1]: continue

            move[i][j], move[i][j + 1] = 1, -1
            if btk(cnt + 1, i, j):
                return True
            move[i][j], move[i][j + 1] = 0, 0

    return False


N, M, H = map(int, input().split())
ladder = [tuple(map(int, input().split())) for _ in range(M)]
move = [[0] * (N + 2) for _ in range(H + 1)]
visited = [[0] * (N + 2) for _ in range(H + 1)]

# 사다리 표시
for x, y in ladder:
    move[x][y] = 1
    move[x][y + 1] = -1

for goal in range(4):
    if btk(0, 1, 0):
        ans = goal
        break
else:
    ans = -1

print(ans)
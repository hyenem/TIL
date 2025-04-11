dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
def solution(game_board, table):

    N = len(game_board)
    blocks= []
    for i in range(N):
        for j in range(N):
            if table[i][j]==0: continue
            minx, maxx, miny, maxy = i, i, j, j
            q = [(i,j)]
            table[i][j]=0
            idx = 0
            while idx<len(q):
                x, y = q[idx]
                minx, maxx = min(minx, x), max(maxx, x)
                miny, maxy = min(miny, y), max(maxy, y)
                idx += 1

                for dx, dy in dxdy:
                    nx, ny = x+dx, y+dy
                    if not(0<=nx<N and 0<=ny<N): continue
                    if table[nx][ny]==1:
                        table[nx][ny]=0
                        q.append((nx, ny))

            block = [[0]*(maxy-miny+1) for _ in range(maxx-minx+1)]
            for x, y in q:
                block[x-minx][y-miny]=1
            blocks.append(block)

    blanks = []
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 1: continue
            minx, maxx, miny, maxy = i, i, j, j
            q = [(i, j)]
            game_board[i][j] = 1
            idx = 0
            while idx < len(q):
                x, y = q[idx]
                minx, maxx = min(minx, x), max(maxx, x)
                miny, maxy = min(miny, y), max(maxy, y)
                idx += 1

                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < N and 0 <= ny < N): continue
                    if game_board[nx][ny] == 0:
                        game_board[nx][ny] = 1
                        q.append((nx, ny))

            blank = [[0] * (maxy - miny + 1) for _ in range(maxx - minx + 1)]
            for x, y in q:
                blank[x - minx][y - miny] = 1
            blanks.append((len(q), blank))

    ans = 0
    for cnt, blank in blanks:
        for idx, block in enumerate(blocks):
            for _ in range(4):
                if len(block)==len(blank) and len(blank[0])==len(block[0]):
                    for i in range(len(block)):
                        for j in range(len(block[0])):
                            if blank[i][j]!=block[i][j]:
                                break
                        else:
                            continue
                        break
                    else:
                        del blocks[idx]
                        ans += cnt
                        break

                blank = list(map(list, zip(*blank[::-1])))
            else:
                continue
            break

    return ans

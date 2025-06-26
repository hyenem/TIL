dice = [[0]*4 for _ in range(3)]

N, M, x, y, K = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

direction = [(0,0), (0,1), (0, -1), (-1, 0), (1, 0)]
for d in map(int,input().split()):
    dx, dy = direction[d]
    nx, ny = x+dx, y+dy
    if not(0<=nx<N and 0<=ny<M):
        continue
    x, y = nx, ny
    if d==1:
        dice[1].insert(0, dice[1].pop())
    elif d==2:
        dice[1].append(dice[1].pop(0))
    elif d==3:
        dice[0][1], dice[1][1], dice[2][1], dice[1][-1]=dice[1][1], dice[2][1], dice[1][3], dice[0][1]
    else :
        dice[2][1], dice[1][1], dice[0][1], dice[1][-1] = dice[1][1], dice[0][1], dice[1][3],dice[2][1]
    if arr[x][y]==0:
        arr[x][y]=dice[1][-1]
    else :
        dice[1][-1], arr[x][y] = arr[x][y], 0
    print(dice[1][1])

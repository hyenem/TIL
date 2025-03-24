def move(direction):
    dx, dy = move_direction[direction]
    nx, ny = location[0]+dx, location[1]+dy
    # 가려는 칸이 범위 내이고 평지면 내 칸 평지로 만들고 옮기기
    if 0<=nx<N and 0<=ny<M and arr[nx][ny]=='.':
        arr[location[0]][location[1]]='.'
        location[0], location[1]=nx, ny
    # 있어야하는 칸에 주어진 방향으로 배치
    arr[location[0]][location[1]]=head_direction[direction]

def shoot():
    x, y = location
    d = head_shape[arr[location[0]][location[1]]]
    while 0<=x<N and 0<=y<M and arr[x][y] not in {'*', '#'}:
        x += d[0]
        y += d[1]
    # 멈췄는데, 벽이면 부수기
    if 0<=x<N and 0<=y<M:
        if arr[x][y]=='*':
            arr[x][y]='.'

move_direction = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}
head_direction = {'U':'^', 'D':'v', 'L':'<', 'R':'>'}
head_shape = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] in head_shape:
                location = [i, j]
    L = int(input())
    info = input()
    for data in info:
        if data!='S':
            move(data)
        else :
            shoot()

    print(f'#{tc} ', end='')
    for ele in arr:
        print(''.join(ele))
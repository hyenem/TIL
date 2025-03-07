

def move_zombie():
    # 현재 위치 다 빈칸 만들기
    for x, y, d in zombie:
        arr[x][y]='O'

    # 모든 좀비 이동
    # 바보같이 여기서 for x, y, d in zombie로 받고
    # x, y, d 를 갱신함 ㅠ 그럼 당연히 안바뀌지
    for i in range(len(zombie)):
        nx = zombie[i][0]+dxdy[zombie[i][2]][0]
        if not(0<=nx<N):
            zombie[i][2] = 2-zombie[i][2]
        else :
            zombie[i][0] = nx

    # 좀비 표시하기
    for x, y, d in zombie:
        arr[x][y]='Z'

    # 이렇게 세 단계로 나눈 이유는 한 줄에 좀비가 두마리 있을 때
    # 원래 있던 칸으로 좀비가 이동하면 이동한 좀비가 지워질수도 있기 때문

N = int(input())
move = list(input())
arr = [list(input()) for _ in range(N)]
dxdy = ((1, 0), (0, -1), (-1, 0), (0, 1))
ax, ay, ad= 0, 0, 0
zombie = []
switch = [[0]*N for _ in range(N)]
# 스위치는 좀비가 이동하면서 arr에 있는 S를 지워버릴 수도 있기 대문에
# 따로 set에 저장하여 관리
switchstart = set()
for i in range(N):
    for j in range(N):
        if arr[i][j]=='Z':
            zombie.append([i, j, 0])
        elif arr[i][j]=='S':
            # 불 켜기
            switch[i][j]=1
            # 스위치 있는 점
            switchstart.add((i,j))

for c in move:
    # 갈 수 있으면 전진
    if c=='F':
        nx, ny = ax+dxdy[ad][0], ay+dxdy[ad][1]
        if 0<=nx<N and 0<=ny<N:
            ax, ay = nx, ny
    # 회전
    elif c=='R':
        ad = (ad+1)%4
    else :
        ad = (ad+3)%4

    # 스위치 만나면 팔방 켜기
    if (ax, ay) in switchstart:
        for dx, dy in ((1, 0), (0, -1), (-1, 0), (0, 1), (1, 1),(1,-1),(-1,1),(-1,-1)):
            snx, sny = ax+dx, ay+dy
            if 0<=snx<N and 0<=sny<N:
                switch[snx][sny]=1

    # 불 안켜져 있고, 좀비 만나면
    if not switch[ax][ay] and arr[ax][ay]=='Z':
        print("Aaaaaah!")
        break

    # 좀비 이동
    move_zombie()

    # 좀비 이동하고 나서도 상태 채크
    if not switch[ax][ay] and arr[ax][ay]=='Z':
        print("Aaaaaah!")
        break
else :
    print("Phew...")
'''
제출횟수 : 1회
풀이시간 : 59분

실행시간 : 92ms
메모리 : 109544KB

[고전한 이유]
* 백트랙킹 하면서 기존 상태를 잘 원복해줘야하는데,
* arr는 잘 원복해놓고, fish 배열을 원복하지 않아서 오래걸림

[ 시간 복잡도 ]
재귀횟수 * 16*상수
재귀는 무조건 3^15보다 작음
시간 안전

[ 엣지 케이스 ] : 시작하자마자 끝나는 경우
7 1 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2

구상 : 5분
* 인풋이 어떻ㅎ게 주진건지, 맵이 항상 4*4인지 파악
구현 : 22분
* 물고기 이동하고 먹힐 떄 갱신해줘야하는 값들이 많아서 고전함
디버깅 : 32분
[1] 물고기 배열을 해당 인덱스에 그 인덱스의 물고기 저장학려고했는데 무작정 append해서 순서꼬임
    -> fish[idx]=(i, j, d)로 수정
[2] 아무리봐도 맞다고 생각했는데 openTC가 답이 안나옴
    -> 배열 다 찍어보다가 신내림 받은것 처럼 fish 배열도 원복해야지!!!!
    -> 수정 -> 맞았습니다
'''

def btk(sx, sy, cnt):
    global ans, arr, fish

    # 기존 상태 저장
    tmp = [ele[:] for ele in arr]
    tmpfish = fish[:]

    # 물고기 먹기( 물고기 죽고, 지도 비우고, 답 올리고, 내 방향 바꾸고 )
    dfish = arr[sx][sy]
    die[dfish] = 1
    arr[sx][sy]=0
    cnt += dfish
    sd = fish[dfish][2]

    # 정답 갱신
    ans = max(ans, cnt)

    # 물고기 이동
    for i in range(1, 17):
        if die[i]: continue             # 죽은 물고기는 건너뛰고
        x, y, d = fish[i]
        for k in range(8):
            nd = (d-1+k)%8+1            # 반시계방향으로 45도씩 돌면서
            dx, dy = dxdy[nd]
            nx, ny = x+dx, y+dy         # 범위 안이고, 상어가 아니면
            if 0<=nx<4 and 0<=ny<4 and (nx, ny)!=(sx, sy):
                fish[i] = (nx, ny, nd)  # 물고기 정보 갱신
                if arr[nx][ny]!=0 :     # 옮긴 칸에도 물고기 있으면 거기 정보도 갱신
                    fish[arr[nx][ny]] = (x, y, fish[arr[nx][ny]][2])
                arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]     # 물고기 옮기기
                break

    # 상어 이동하기
    dx, dy = dxdy[sd]
    sx, sy = sx+dx, sy+dy
    # 끝까지 가면서 갈 수 있는 칸 다 가보기
    while 0<=sx<4 and 0<=sy<4:
        if arr[sx][sy]!=0:
            btk(sx, sy, cnt)
        sx, sy= sx+dx, sy+dy

    # btk을 위해 기존 상태 복구
    die[dfish]=0
    arr = tmp
    fish = tmpfish


dxdy = ((0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
data = [list(map(int, input().split())) for _ in range(4)]
arr = [[0]*4 for _ in range(4)]     # 해당 칸에 몇번 물고기가 있는지
fish = [0]*17                       # 인덱스 별 물고기의 좌표, 방향 저장
die = [0]*17                        # 먹힌 물고기
for i in range(4):
    for j in range(4):
        idx, d = data[i][2*j], data[i][2*j+1]
        fish[idx]=(i, j, d)
        arr[i][j] = idx

ans = 0
btk(0, 0, 0)
print(ans)
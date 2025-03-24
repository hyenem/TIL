'''
제출횟수 : 1회
풀이시간 : 38분

실행시간 : 3720ms -> 524ms
메모리 : 118024KB

[오해했던 것]
* 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
    >> 내 열에 없으면 내 오른쪽 열 가서 잡는건 줄 알았음
* 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다.
    이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
    >> 모든 상어가 이동을 마친 후가 아니라, 각각의 상어가 이동을 마친 후 인줄 알았음

[시간복잡도]
O(C*(R+M*(R+C)))
100*(100*100)*100 = 10^8

[엣지케이스] : 이동 이후 상어가 한 칸에 여러개 있는 경우
3 4 4
1 3 1 2 2
2 2 1 3 3
2 4 1 4 4
3 3 1 1 5

구상 : 3분
* 같은 칸에 있는 상어의 크기가 중요하니까 배열에 상어의 인덱스와 크기를 저장
* 상어의 상태는 따로 관리

구현 : 16분
디버깅 : 19분
* 오해했던 점 두가지 수정
* 다행히 오픈 테케에 다 걸려서 수정해서 제출할 수 있었음


리팩토링
* 시간 초과 났어도 이상하지 않았을 상황
* 이동을 다 하는게 아니라 주기성을 띄고 이동하도록 바꿈
'''


# 내 열에 있는 물고기잡기
# 내열에 없으면 오른쪽으로 가서 잡는게 아니라 못잡는것
def catch():
    global ans
    for i in range(N):
        if arr[i][kangtegong]:
            idx, size = arr[i][kangtegong]
            ans += size
            die[idx] = 1
            arr[i][kangtegong] = 0
            return


# 물고기 이동하기
# 다 이동하고 서로 잡아먹는 것
def move():
    global arr
    # 이동시킬 배열
    narr = [[0] * M for _ in range(N)]
    for i in range(K):

        # 살아있는 물고기에 대해서만
        if die[i]: continue

        x, y, s, d, z = shark[i][:]
        dx, dy = dxdy[d]
        for _ in range(s):
            x, y = x + dx, y + dy

            # 범위 벗어나면 방향 바꿔서ㅓ 뒤로가기
            if not (0 <= x < N and 0 <= y < M):
                d = changed[d]
                shark[i][3] = d
                dx, dy = dxdy[d]
                x, y = x + 2 * dx, y + 2 * dy
        # 위치 갱신
        shark[i][0], shark[i][1] = x, y

        # 물고기 겹치면 먹고 먹히기
        if narr[x][y]:
            nidx, nsize = narr[x][y]
            if nsize < z:
                die[nidx] = 1
                narr[x][y] = (i, z)
            else:
                die[i] = 1
        else:
            narr[x][y] = (i, z)
    # 복사~
    arr = [ele[:] for ele in narr]


N, M, K = map(int, input().split())
shark = [tuple(map(int, input().split())) for _ in range(K)]
die = [0] * K
arr = [[0 for _ in range(M)] for _ in range(N)]
dxdy = (0, (-1, 0), (1, 0), (0, 1), (0, -1))
changed = (0, 2, 1, 4, 3)

for i in range(K):
    x, y, s, d, z = shark[i]

    # 상하로 움직이면 행주기, 좌우로 움직이면 열주기
    if d <= 2:
        s %= 2 * (N - 1)
    else:
        s %= 2 * (M - 1)
    shark[i] = [x - 1, y - 1, s, d, z]

    # 지도에 인덱스, 크기 표시
    arr[x - 1][y - 1] = (i, z)

ans = 0
for kangtegong in range(M):
    catch()
    move()

print(ans)
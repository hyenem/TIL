'''

[ 선정 이유 ]
* 도망자 이동할 때 전체 배열을 복사하는 것이 아니라,
    움직인 애들을 move에 넣은 뒤에 하나씩 이동해서 효율성
* 술래 이동 방향 미리 찾아두고 mode처리함
* 2칸 이내만 보면되니까 도망자를 1차원으로 관리해서 다 보지않고
    2차원으로 관리해서 움직여야하는 칸만 옮기기

[ 오해할 만한 것 ]
* 시작하자 마자 잡고 가나? -> 아닌가봐
* 같은 칸이어도 나무는 고려해야함
* 술래 칸에 도망자 들어갈 수 있다!
* 0, 0에서 두번 머무나? -> 한번만 머물고 바로 뒤도나봐
* 제로베이스일까 원베이스일까?

[ 시간 복잡도 ]
도망자 이동의 볼륨을 따라올 자가 없음
대강 M^2 -> 최대 10^8 정도? -> 시간 제한 5초 -> 가능

[ 테스트 케이스 ] : 도망자가 겹치는 경우
5 3 1 1
3 4 2
5 4 2
4 3 1
2 4

'''


def make_snail():
    for repeat in range(2, 2 * N + 3):
        nd = (med[-1] + 1) % 4
        dx, dy = dxdy[nd]
        for _ in range(repeat // 2 - 1):
            nx, ny = mexy[-1][0] + dx, mexy[-1][1] + dy
            mexy.append((nx, ny))
            med.append(nd)
            if nx == 0 and ny == 0: break
    # 바라보는 방향은 다음 이동방향이므로
    # 앞으로 하나씩 옮겨져야함
    med.pop(0)

    # 역순으로 가면서 위치는 그대로, 방향은 반대로 저장
    for i in range(len(mexy) - 2, -1, -1):
        mexy.append(mexy[i])
        med.append((med[i] + 2) % 4)
    mexy.pop()

def run():
    # 나(술래)랑 거리가 3이하인 애들을 move에 저장
    # x, y, 방향으로 저장
    # 저장하면서 원래 위치는 비워주기

    move = []
    for h in range(-3, 4):
        rx = mx+h
        if not(0<=rx<N): continue
        for w in range(abs(h)-3, 4-abs(h)):
            ry = my+w
            if not(0<=ry<N): continue
            while runner[rx][ry]:
                move.append((rx, ry, runner[rx][ry].pop()))


    # 움직여서 지도에 표시해주기
    for rx, ry, rd in move:
        nrx, nry = rx+dxdy[rd][0], ry+dxdy[rd][1]
        if not(0<=nrx<N and 0<=nry<N):
            rd = (rd+2)%4
            nrx, nry = rx+dxdy[rd][0], ry+dxdy[rd][1]

        if (nrx, nry)!=(mx, my):
            runner[nrx][nry].append(rd)
        else :
            runner[rx][ry].append(rd)

def catch():
    cnt = 0                 # 몇 명 붙잡았는지
    mdx, mdy = dxdy[md]
    for k in range(3):
        sx, sy = mx + k * mdx, my + k * mdy
        if not (0 <= sx < N and 0 <= sy < N): break     # 범위 밖이면 그만
        if tree[sx][sy]: continue                       # 나무면 지나가기
        if len(runner[sx][sy]) != 0:
            cnt += len(runner[sx][sy])
            runner[sx][sy].clear()
    return cnt

#=======================================================================================

N, M, H, K = map(int, input().split())
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
runner = [[[] for _ in range(N)] for _ in range(N)]
tree = [[0]*N for _ in range(N)]
rns = [list(map(int, input().split())) for _ in range(M)]
trs = [list(map(int, input().split())) for _ in range(H)]
for x, y, d in rns:
    runner[x-1][y-1].append(d)
for x, y in trs:
    tree[x-1][y-1]=1

# 나(술래)가 가는 길과 바라볼 방향을 미리 계산해두기
mexy = [(N//2, N//2)]
med = [-1]
make_snail()


ans = 0
# 조기 위치 및 방향
mx, my = mexy[0]
d = med[0]
idx = 1
for turn in range(1, K+1):

    # 도망가기
    run()

    # 나(술래) 이동
    mx, my = mexy[idx]
    md = med[idx]
    idx = (idx+1)%len(med)

    # 보이는 애들 잡기
    cnt = catch()

    # 잡은 수 * 몇번째 턴으로 정답에 더하기
    ans += turn*cnt

print(ans)
'''
제출횟수 : 2회
    -> 틀렸습니다.
        def pick(playeridx, x, y):
            Mg = max(garr[x][y])
            if player[playeridx][4] < Mg:
                garr[x][y].remove(Mg)
                garr[x][y].append(player[playeridx][4])
                player[i][4] = Mg                           <- i가 아니라 playeridx로 가야함
풀이시간 : 1시간 53분

[ 명심할 점 ]
* 함수 안에서 쓰면 안되는 전역변수 끌어다 쓰지 않았는지 확인할 것
* 내가 맞다고 생각하는 부분은 주로 맞으니까,,,
    로직이 맞으면,,, 의심 멈추고,,, 좀 작은 부분 사소한 부분도 살펴보기,,,
* 혜민아 너는 예시를 500회 돌려가면서 검증할 수 없는 사람이야,, 상황만 따와서 작게 만들어서 봐야지

[ 오해할 만한 점 ]
* 진 사람이 이동할 수 있는 칸은 반드시 있는가?
    -> YES(적어도 이동한 사람이 이전에 있던 칸으로 갈 수 있음)

구상 : 4분
* 사람 정보에 위치, 방향, 초기능력치, 총 공격력을 저장해야겠다
* 1based니까 0based로 바꿔줘야겠다
* dydx 시계방향으로 줬네 굳~

구현 : 33분
* 총이 한칸에 여러개 있을 수 있음을 파악하고 3차원으로 수정함

디버깅 : 20분 / 56분
* 테케 여러개 만들어서 검증 했는데 -> 틀렸습니다.
* 오만분 틀린 이유 찾다가 55분쯤 뒤에 깨닫고 수정 -> 맞았습니다.

리팩토링
* 함수화
'''

def move(i):
    # 내가 있던 칸 비워주고, 다음칸으로
    # 다음칸이 경계 밖이면 방향바꾸고 반대로 한칸

    x, y, d, s, g = player[i]

    parr[x][y] = -1

    dx, dy = dxdy[d]
    nx, ny = x + dx, y + dy

    if not (0 <= nx < N and 0 <= ny < N):
        d = (d + 2) % 4
        player[i][2] = d
        dx, dy = dxdy[d]
        nx, ny = x + dx, y + dy

    x, y = nx, ny
    player[i][0], player[i][1] = x, y
    return x, y

def pick(playeridx):
    # 해당 플레이어가 지금 있는 칸의 총 줍기
    # 그 칸의 총 중 최댓값이 나보다 작거나 같으면 안줍고
    # 큰 경우에만 줍고 내껀 거기 넣어주기
    x, y = player[playeridx][0], player[playeridx][1]

    Mg = max(garr[x][y])

    if player[playeridx][4] < Mg:
        garr[x][y].remove(Mg)
        garr[x][y].append(player[playeridx][4])
        player[playeridx][4] = Mg


def fight(p1, p2):
    # 두 플레이어 중 누가 이기는지 결정하기
    s1, g1 = player[p1][3], player[p1][4]
    s2, g2 = player[p2][3], player[p2][4]
    if s1+g1 < s2+g2 or (s1 + g1 == s2+g2 and s1 < s2):
        return enemy, i
    else:
        return i, enemy


def afterfight(win, lose):
    # 이긴사람 점수 더해주기
    # 진사람은 총 버리고 이동하고 총줍기
    # 이긴사람은 그자리에서 총줍기
    wx, wy, wd, ws, wg = player[win]
    lx, ly, ld, ls, lg = player[lose]

    #점수
    points[win] += abs(ws + wg - ls - lg)

    #진사람
    if lg != 0: garr[x][y].append(lg)
    lg = 0

    for _ in range(4):
        dx, dy = dxdy[ld]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and parr[nx][ny] == -1:
            lx, ly = nx, ny
            break
        ld = (ld + 1) % 4

    parr[lx][ly]=lose
    player[lose]=[lx, ly, ld, ls, lg]
    pick(lose)

    #이긴사람
    parr[wx][wy] = win
    player[win]=[wx, wy, wd, ws, wg]
    pick(win)


N, M, K = map(int, input().split())
garr = [list(map(lambda x: [int(x)], input().split())) for _ in range(N)]
parr = [[-1]*N for _ in range(N)]
player = [list(map(int, input().split())) for _ in range(M)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
points = [0]*M
for i in range(M):
    x, y, d, s = player[i]
    parr[x-1][y-1]=i
    player[i]=[x-1, y-1, d, s, 0]

for _ in range(K):
    for i in range(M):
        x, y = move(i)
        if parr[x][y]==-1:
            parr[x][y] = i
            pick(i)
        else :
            enemy = parr[x][y]
            win, lose = fight(i, enemy)
            afterfight(win, lose)

print(*points)

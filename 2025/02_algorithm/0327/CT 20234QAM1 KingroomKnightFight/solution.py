'''
제출횟수 : 1회
풀이시간 : 1시간 30분

[ 헷갈렸던 것 ]
* 기사가 아마 맵 안에 무조건 담기게 주어지겠지?!?
* 데미지가 체력 이상으로 들어간 것도 답에 더해주라는 거겠지?

구상 : 4분
* 밀리는 사람들을 q로 관리해야겠다고 생각함
* 시간 복잡도 널널하니까 그냥 편하게 구현하자는 생각

구현 : 36분
* move함수화해서 이동에 성공한 경우에만 새로운 knight 배열을 받아서 덮어씌우도록 해야겠다

디버깅 및 검증 : 50분
1. opneTC
* 초기 체력과 마지막 체력의 차로 데미지를 계산하려니까,, 죽은애들은 제외해야해서 점수 계산법 수정

2. 추가TC
* 직접 TC만드는데 대부분의 시간을 사용
* 새로 추가되는 칸에 대해서만 가시 처리를 해주어 전체를 돌도록 수정
* 이후 다시 openTC 돌리니,,, 체력 감소시키면서 그려서,, 이번턴에 죽는 애도 그려짐
    -> 두단계 나눠서 체력감소, 이후 색칠로 로직 바꿈

리팩토링
* 함수화
* 누적합 사용

[ 시간 복잡도 ]
Q*(L*L + N*N*L)

[ 테스트 케이스 ] : 상하좌우 검증 및 한 칸짜리 검증
6 3 3
0 0 0 0 0 0
1 1 1 1 1 2
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
2 1 1 2 10
2 3 2 1 10
2 4 1 2 10
1 1
1 1
1 1


6 3 3
0 0 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
2 1 1 2 10
3 2 2 1 10
5 2 1 2 10
1 2
1 2
1 2

6 3 3
0 0 0 0 0 0
1 1 1 1 1 1
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
2 2 1 2 10
2 4 2 1 10
2 5 1 2 10
3 3
3 3
3 3

6 3 3
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
3 1 1 2 10
4 2 2 1 10
6 2 1 2 10
3 0
3 0
3 0

6 3 3
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
3 1 1 1 10
4 2 1 1 10
6 2 1 1 10
3 0
3 0
3 0
'''

def move():
    new_knight = knight[:]

    dx, dy = dxdy[kd]
    visited = [0] * len(knight)
    visited[ki] = 1
    q = [ki]
    qi = 0
    while qi < len(q):
        ni = q[qi]
        qi += 1

        sx, sy, h, w, k, a = knight[ni]

        # 각 방향 별 새로 추가되는 행 또는 열의 시작 인덱스, 행/열 방향, 채크해야하는 길이
        if kd == 0:
            nx, ny, ndx, ndy, R = sx - 1, sy, 0, 1, w
        elif kd == 1:
            nx, ny, ndx, ndy, R = sx, sy + w, 1, 0, h
        elif kd == 2:
            nx, ny, ndx, ndy, R = sx + h, sy, 0, 1, w
        else:
            nx, ny, ndx, ndy, R = sx, sy - 1, 1, 0, h

        for r in range(R):
            nnx, nny = nx + r * ndx, ny + r * ndy

            # 다음칸이 범위 밖이거나 벽이면 실패 결과 반환
            if not (0 <= nnx < L and 0 <= nny < L) or arr[nnx][nny] == 2:
                return knight, []

            # 내가 밀려난 칸에 다른 기사가 있으면 큐에 넣어주기
            if karr[nnx][nny] and not visited[karr[nnx][nny]]:
                q.append(karr[nnx][nny])
                visited[karr[nnx][nny]] = 1


        ex, ey = sx + h - 1, sy + w - 1

        # 기사의 범위에 가시 개수 세기
        c = acc[ex][ey]
        if sx > 0: c -= acc[x - 1][ey]
        if sy > 0: c -= acc[ex][y - 1]
        if sx > 0 and sy > 0: c += acc[x - 1][y - 1]

        # 기사 정보 업데이트
        if ki!=ni:
            new_knight[ni] = (sx+dx, sy+dy, h, w, max(0, k - c), a + c)
        else :
            new_knight[ni] = (sx + dx, sy + dy, h, w, k, a)


    # q는 밀려서 다친애들 처리하기 위함인데
    # 첫번째 애는 밀리질 않음
    q.pop(0)
    return new_knight, q


# 밀린 기사 아프기
def attack(q):
    for i in q:
        x, y, h, w, k, a = knight[i]
        ex, ey = x + h - 1, y + w - 1

        # 기사의 범위에 가시 개수 세기
        c = acc[ex][ey]
        if x > 0: c -= acc[x - 1][ey]
        if y > 0: c -= acc[ex][y - 1]
        if x > 0 and y > 0: c += acc[x - 1][y - 1]

        # 기사 정보 업데이트
        knight[i] = (x, y, h, w, max(0, k - c), a + c)


def draw():
    narr = [[0] * L for _ in range(L)]
    for i in range(1, N + 1):
        x, y, h, w, k, a = knight[i]
        if k <= 0: continue
        for kx in range(x, x + h):
            for ky in range(y, y + w):
                narr[kx][ky] = i
    return narr

L, N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(L)]
acc = [[0] * L for _ in range(L)]

# 가시 누적합으로 조금 효율적으로
for i in range(L):
    for j in range(L):
        if arr[i][j] == 1: acc[i][j] = arr[i][j]
        if i > 0: acc[i][j] += acc[i - 1][j]
        if j > 0: acc[i][j] += acc[i][j - 1]
        if i > 0 and j > 0: acc[i][j] -= acc[i - 1][j - 1]

knight = [0] + [tuple(map(int, input().split())) for _ in range(N)]
karr = [[0] * L for _ in range(L)]

for i in range(1, N + 1):
    x, y, h, w, k = knight[i]
    knight[i] = (x - 1, y - 1, h, w, k, 0)

cmds = [tuple(map(int, input().split())) for _ in range(Q)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

for ki, kd in cmds:

    # 죽은 기사면 그냥 넘어가기
    if knight[ki][4] <= 0: continue

    # karr에 각 기사가 차지하고 있는 칸 표시해주기
    karr = draw()

    # 해당 기사 옮기기
    # 반환값
    # 옮기기 성공했을 때 : 갱신된 기사 정보, 밀린 기사 인덱스
    # 실패했을 때 : 기존 기사 배열, 빈배열
    knight, q = move()
ans = 0
knight.pop(0)
for x, y, h, w, k, a in knight:
    if k <= 0: continue
    ans += a

print(ans)



'''리팩토링 전
def move():
    new_knight = knight[:]

    dx, dy = dxdy[kd]
    visited = [0] * len(knight)
    visited[ki] = 1
    q = [ki]
    qi = 0
    while qi < len(q):
        ni = q[qi]
        qi += 1

        sx, sy, h, w, k, a = knight[ni]

        if kd == 0:
            nx, ny, ndx, ndy, R = sx - 1, sy, 0, 1, w
        elif kd == 1:
            nx, ny, ndx, ndy, R = sx, sy + w, 1, 0, h
        elif kd == 2:
            nx, ny, ndx, ndy, R = sx + h, sy, 0, 1, w
        else:
            nx, ny, ndx, ndy, R = sx, sy - 1, 1, 0, h

        for r in range(R):
            nnx, nny = nx + r * ndx, ny + r * ndy
            if not (0 <= nnx < L and 0 <= nny < L) or arr[nnx][nny] == 2:
                return knight, []

            if karr[nnx][nny] and not visited[karr[nnx][nny]]:
                q.append(karr[nnx][nny])
                visited[karr[nnx][nny]] = 1

        new_knight[ni] = (sx + dx, sy + dy, h, w, k, a)

    q.pop(0)
    return new_knight, q


L, N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(L)]
knight = [0] + [tuple(map(int, input().split())) for _ in range(N)]
karr = [[0] * L for _ in range(L)]

for i in range(1, N + 1):
    x, y, h, w, k = knight[i]
    for kx in range(x - 1, x - 1 + h):
        for ky in range(y - 1, y - 1 + w):
            karr[kx][ky] = i
    knight[i] = (x - 1, y - 1, h, w, k, 0)

cmds = [tuple(map(int, input().split())) for _ in range(Q)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

for ki, kd in cmds:

    if knight[ki][4] <= 0: continue

    knight, q = move()
    q = set(q)
    karr = [[0] * L for _ in range(L)]
    for i in range(1, N + 1):
        x, y, h, w, k, a = knight[i]
        for kx in range(x, x + h):
            for ky in range(y, y + w):
                if i in q and i != ki and arr[kx][ky] == 1:
                    k = max(0, k - 1)
                    a += 1
        if i in q and i != ki:
            knight[i] = (x, y, h, w, k, a)
        if k <= 0: continue
        for kx in range(x, x + h):
            for ky in range(y, y + w):
                karr[kx][ky]=i
ans = 0
knight.pop(0)
for x, y, h, w, k, a in knight:
    if k <= 0: continue
    ans += a

print(ans)

'''
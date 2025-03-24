'''
제출횟수 : 1회
풀이시간 : 33분

실행시간 : 264ms -> 108ms
메모리 : 110960KB

[오해할만한 부분]
* 구슬이 도착칸에 구멍이 있어야 빠지는건가? 간는길에 구멍 있어도 빠지는건가? -> 테케로 확인가능

[시간 복잡도]
2*8*10*4*2^9 대강 2^15*10 = 327_680
(M+N)*10*(2^11)
두 구슬 * 최대이동 8칸 * 10번 * 첫번째는 네방향 * 나머지는 두방향

[엣지케이스] : 10번만에 도착하는 경우(맵 사이즈가 문제 조건에 맞지는 않음)
11 12
############
#........#B#
#.######.#R#
#.#....#.#.#
#.#.##.#.#.#
#.#.#O.#.#.#
#.#.####.#.#
#.#......#.#
#.########.#
#..........#
############


구상 : 2분
* 최대 횟수가 10번이라 백트랙킹 하라는 소리군
* 네 방향 다 해보면 되겠는데, 방향을 다 저장하고 일일이 돌려보면 시간 손해니까,
* 검증하고, 좌표 갱신하고, 다음단계로 넘어가는게 이득

구현 : 18분
디버깅 : 13분
[1] check함수
    while문을 쓰면서 '#'을 만날때까지 갔는데,
    그러면 구슬의 좌표는 '#'좌표의 한칸 전이니까 nrx-dx, nry-dy 인데, 그냥 nrx, nry로 써서 오류
    배열 출력해봐서 바로 눈에 띔
[2] rx, ry, bx, by 갱신
    구슬 이동이 영 이상하게 돼서 왜지? 하고 봣더니
    이차원 배열에만 B과 R을 옮기고 rx, ry, bx, by 갱신을 안해줌


리팩토링
[1] 실행시간 단축
* 네 방향 중 왔던 방향만 안보게 처리했는데,
* 왔던 방향의 반대방향도 안보게 처리할 수 있음
* 또 맵에 직접 구슬을 옮겨가면서 btk을 진행했는데, 앱에 구슬이 없어도 됨
* 그래서 좌표만 들고다니게 처리

[2] BFS로도 구현
* 좌표만 들고 다니게 처리하니까 백트랙킹을 할 필요가 없다는거 알게됨
* 그래서 BFS로 풀이함
'''

# DFS 풀이

# 판 기울여서 구슬 굴리기
def check(d):
    dx, dy = dxdy[d]
    nrx, nry, nbx, nby = rx, ry, bx, by

    # 파랑부터 굴리기
    bcnt = 0
    while arr[nbx+dx][nby+dy]!='#':
        bcnt += 1
        nbx, nby = nbx+dx, nby + dy
        # 파랑이 구멍 만나면 실패
        if arr[nbx][nby]=='O':
            return 0, -1, -1, -1, -1

    # 파랑이 구멍 안만날때
    rcnt = 0
    while arr[nrx+dx][nry+dy]!='#':
        rcnt += 1
        nrx, nry = nrx+dx, nry + dy
        # 빨강이 구멍 만나면 성공
        if arr[nrx][nry]=='O':
            return 1, -1, -1, -1, -1

    # 두 구슬 다 구멍 안만났는데,
    # 두 구슬이 같은 위치에 있으면
    if nbx==nrx and nby==nry:
        # 움직인 횟수가 많은 애가 한칸 뒤로 물러서야함
        if rcnt<bcnt:
            nbx, nby = nbx-dx, nby-dy
        else:
            nrx, nry = nrx-dx, nry-dy

    return 2, nrx, nry, nbx, nby

def btk(cnt, bd):
    global ans
    # 가지치기
    if cnt+1>=ans: return

    for d in range(4):
        global rx, ry, bx, by
        # 이전에 왔던 방향이나 그 반대방향으로는 굴릴 필요 없음
        if bd!=-1 and d%2==bd%2: continue

        res, nrx, nry, nbx, nby = check(d)
        if res==0: continue
        # 성공했으면 정답 갱신. 그리고 더이상 갈 필요 없음.
        if res==1:
            ans = cnt+1
            return
        else:
            # 아직 성공도 실패도 아니면, 그리고 좌표가 바꼈으면 btk
            if rx==nrx and ry==nry and bx==nbx and by==nby: continue
            tmp = (rx, ry, bx, by)
            rx, ry, bx, by = nrx, nry, nbx, nby
            btk(cnt+1, d)
            # 상태 복원
            rx, ry, bx, by = tmp



N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='R':
            rx, ry = i, j
        elif arr[i][j]=='B':
            bx, by = i, j

dxdy = ((0, -1), (-1, 0), (0, 1), (1, 0))
ans = 11
btk(0, -1)

# 정답 한번도 갱신 안됐으면 -1
if ans==11: ans = -1
print(ans)

#========================================================================
#========================================================================

# BFS 풀이

from collections import deque

# 판 기울여서 구슬 굴리기
def check(d):
    dx, dy = dxdy[d]
    nrx, nry, nbx, nby = rx, ry, bx, by

    # 파랑부터 굴리기
    bcnt = 0
    while arr[nbx+dx][nby+dy]!='#':
        bcnt += 1
        nbx, nby = nbx+dx, nby + dy
        # 파랑이 구멍 만나면 실패
        if arr[nbx][nby]=='O':
            return 0, -1, -1, -1, -1

    # 파랑이 구멍 안만날때
    rcnt = 0
    while arr[nrx+dx][nry+dy]!='#':
        rcnt += 1
        nrx, nry = nrx+dx, nry + dy
        # 빨강이 구멍 만나면 성공
        if arr[nrx][nry]=='O':
            return 1, -1, -1, -1, -1

    # 두 구슬 다 구멍 안만났는데,
    # 두 구슬이 같은 위치에 있으면
    if nbx==nrx and nby==nry:
        # 움직인 횟수가 많은 애가 한칸 뒤로 물러서야함
        if rcnt<bcnt:
            nbx, nby = nbx-dx, nby-dy
        else:
            nrx, nry = nrx-dx, nry-dy

    return 2, nrx, nry, nbx, nby


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='R':
            rx, ry = i, j
        elif arr[i][j]=='B':
            bx, by = i, j

dxdy = ((0, -1), (-1, 0), (0, 1), (1, 0))
q = deque([(-1, 0, rx, ry, bx, by)])

ans = 0
while q:
    # 이전 방향, 몇번 움직였는지, 각 구슬의 좌표
    bd, cnt, rx, ry, bx, by = q.popleft()

    # 10올때까지 빨강 구슬이 구멍 못만났으니 실패
    if cnt==10:
        print(-1)
        break

    for d in range(4):
        # 이전에 왔던 방향이나 그 반대방향으로는 굴릴 필요 없음
        if bd!=-1 and d%2==bd%2: continue
        res, nrx, nry, nbx, nby = check(d)
        if res==0: continue
        # 성공했으면 정답 뽑고 끝내기
        if res==1:
            ans = cnt+1
            print(ans)
            break
        else:
            # 아직 성공도 실패도 아니면, 그리고 좌표가 바꼈으면 큐에 넣어주기
            if rx==nrx and ry==nry and bx==nbx and by==nby: continue
            q.append((d, cnt+1, nrx, nry, nbx, nby))
    if ans:
        break
# 정답 한번도 안뽑혔으면 -1 출력 멈추기
else:
    print(-1)
'''
[코드 선정 이유]
* BFS, DFS 모두 풀이
* 파랑, 빨강 순으로 처리해서 RETURN해서 연산량을 줄임
* 겹치는 칸을 이동한 횟수를 바탕으로 한 칸 전으로 돌아가서 처리함
* 왼쪽 방문 이후 오른쪽으로 갈 필요 없음
  위 방문 이후 아래로 갈 필요 없음     (가지치기)


[오해할만한 부분]
* 구슬이 도착칸에 구멍이 있어야 빠지는건가? 간는길에 구멍 있어도 빠지는건가? -> 테케로 확인가능
* 아랫방향으로 중력이 작용하나? : 아니다!
* 처음부터 구슬이랑 구멍 위치 같으면 어떡하지? -> 맵이 주어지기에 한칸에 두 글자가 써질 수 업어서 불가능

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
---
10 10
##########
#OR.....B#
#.########
#.#......#
#.#......#
#.#......#
#.#......#
#.########
#.#......#
##########

ans: -1
구멍에 빠지는 구슬 처리를 잘하지 않았다면 B가 O에 들어가지 못해 정답처리
---
10 10
##########
#........#
#........#
#........#
#........#
#........#
#........#
#........#
#OBR.....#
##########

ans: -1

---
10 10
##########
#........#
#........#
#........#
#........#
#........#
#........#
##B......#
#O#R.....#
##########
ans: -1
가장 오래 걸리는 경우
    - 시작하자마자 BFS로 R의 접근 가능 여부 확인?
---
10 10
##########
#B#.....R#
###.######
###....###
######...#
########.#
#..#...#.#
#..#.#.#.#
#..O.#...#
##########

ans = -1
그냥 나만 틀린 테케..
---
3 7
#######
#B.O.R#
#######

---
방향이 하나밖에 없고 무조건 둘다 죽음
10 3
###
#.#
#O#
#.#
#.#
#R#
#B#
#.#
#.#
###
ans : -1

문제 조건은 아니지만 절대 못가는 경우
3 10
##########
#.O..#.RB#
##########
ans : -1

5 5
#####
#B.O#
#...#
#..R#
#####
ans : 1 (위로 기울이면 정답)

4 4
####
#RO#
#.B#
####
ans : 1 (구슬/구멍이 다 배치될 수 X.. 라고 생각했다가 문제를 믿기로 함)
.. ㅠㅠ 근데 문제에서 구슬 1개씩 꼭 준다했어..
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
'''
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
'''

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
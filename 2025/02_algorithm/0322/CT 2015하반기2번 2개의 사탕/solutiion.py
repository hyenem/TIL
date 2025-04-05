'''2회독
제출횟수 : 2회
    * 틀렸습니다 1회 : 방향별로 파랑 사탕이나와서 못갈때 for문 continue를 해야하는데,
                    return을 해서 다른 방향도 못보게함
풀이시간 : 21분

디버깅
[1] 빨강 사탕 나오는지 채크하는 로직을, 파랑 사탕 나오는지 채크하는 코드 복붙했는데
    모든 변수를 수정한게 아니라 문제가 생김
[2] 틀렸습니다 수정(btk안 for문에서는 return이 아니라 continue)

<check list>
[] return, contine, break 혼동하지 않았나
[] 모듈 복사하고, 변수 완벽히 수정했나
'''

def check(rx, ry, bx, by, d):

    dx, dy = dxdy[d]
    rcnt, bcnt =0, 0

    while arr[bx+dx][by+dy]!='#':
        bcnt+=1
        bx, by = bx+dx, by+dy
        if arr[bx][by]=='O':
            return 0, -1, -1, -1, -1

    while arr[rx+dx][ry+dy]!='#':
        rcnt+=1
        rx, ry = rx+dx, ry+dy
        if arr[rx][ry]=='O':
            return 1, -1, -1, -1, -1

    if (rx, ry)==(bx, by):
        if rcnt<bcnt:
            bx, by = bx-dx, by-dy
        else :
            rx, ry = rx - dx, ry - dy

    return 2, rx, ry, bx, by


def btk(rx, ry, bx, by, d, cnt):
    global ans

    if cnt+1>=ans: return

    for nd in range(4):
        if d!=-1 and nd in {d, (d+2)%4}: continue
        res, nrx, nry, nbx, nby = check(rx, ry, bx, by, nd)
        if res==1:
            ans = min(ans, cnt+1)
            return
        elif res==0: continue
        else:
            btk(nrx, nry, nbx, nby, nd, cnt+1)

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='R':
            rx, ry = i, j
        elif arr[i][j]=='B':
            bx, by = i, j

dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
ans = 11
btk(rx, ry, bx, by, -1, 0)
if ans==11: ans = -1
print(ans)



'''1회독 코드

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
'''
'''
제출횟수 : 6회
풀이시간 : 1시간 53분

실행시간 : 150ms -> 88ms
메모리 : 20MB -> 18MB

[ 명심할 것! ]
* 모든 것을 의심하기
* 의심해으면 검증하기

[ 엣지 케이스 ]
3 1 5
4 4 4
1 0 4
3 4 4

3 1 5
2 2 2
1 0 2
3 2 2

구상 : 7분
* 팀을 어떻게 관리할지 고민함(다 데리고 다녀야하나?)
* 머리랑 꼬리만 저장하기로 결정(중간에 공 맞은 애는 머리까지 가는 거리 매번 계산)

구현 : 34분
디버깅 : 1시간 12분
* 꼬리를 무는 경우를 처리를 잘못함
* move() 내부 꼬리 무는 경우 처리 수정 -> 틀렸습니다
* move() 내부 꼬리 무는 경우 다시 수정 -> 틀렸습니다
* score() 내부 꼬리 무는 경우 수정 -> 시간 초과
* score() 함수의 문제인 줄 알고 해당 부분 수정 -> 인덱스 에러
* score() 함수 내부 다시 수정 -> 시간 초과
* 입력 받을 때 꼬리 물면 무한 루프 돈다는 것을 깨닫고 수정 -> 맞았습니다

리펙토링
* 매번 줄을 따라가면서 양방향으로 보면서 머리랑 몇칸차인지 계산하는 로직이 비효율적
* 팀별 길이랑 머리/꼬리 위치를 저장하고 한길로 쭉 가서 머리 몇번째 사람인지 계싼

'''
from collections import deque

# 모든 사람 움직이기
def move():
    for i in range(M):
        hx, hy, tx, ty, length = team[i]

        # 다음 머리 찾기
        for dx, dy in dxdy:
            nhx, nhy = hx+dx, hy+dy
            if not(0<=nhx<N and 0<=nhy<N): continue
            if arr[nhx][nhy] in {3, 4}:
                break

        # 다음 꼬리 찾기
        for dx, dy in dxdy:
            ntx, nty = tx+dx, ty+dy
            if not(0<=ntx<N and 0<=nty<N): continue
            if arr[ntx][nty]==2:
                break

        # 머리꼬리 움직이기
        arr[hx][hy]=2
        arr[tx][ty]=4
        arr[nhx][nhy]=1
        arr[ntx][nty]=3
        team[i]=(nhx, nhy, ntx, nty, length)

def throw():
    # 던질 위치, 방향 찾기
    if (round//N)%4==0:
        sx, sy = round%(4*N), -1
        dx, dy = 0, 1
    elif (round//N)%4==1:
        sx, sy = N, round%(4*N)-N
        dx, dy = -1, 0
    elif (round//N)%4==2:
        sx, sy = 3*N-round%(4*N) -1, N
        dx, dy = 0, -1
    else:
        sx, sy = -1, 4*N - round%(4*N) -1
        dx, dy = 1, 0

    # 던지기
    while 0<=sx+dx<N and 0<=sy+dy<N:
        sx, sy = sx+dx, sy+dy
        # 맞았으면 그만하기
        if arr[sx][sy] in {1, 2, 3}:
            return sx, sy
    return -1, -1

def score(sx, sy):
    visited = [[0]*N for _ in range(N)]
    visited[sx][sy]=1
    cnt = 1

    # 한 길로 1이나 3이 나올때까지 쭈우욱가기
    while arr[sx][sy] not in {1, 3}:
        cnt += 1
        for dx, dy in dxdy:
            nx, ny = sx+dx, sy+dy
            if not(0<=nx<N and 0<=ny<N): continue
            if visited[nx][ny]: continue
            if arr[nx][ny] not in {0, 4}:
                visited[nx][ny]=1
                sx, sy = nx, ny
                break

    # 1이면 누적 칸수의 제곱이 점수
    # 3이면 길이에서 누적 칸 수 뺸것의 제곱이 점수
    # 추가되는 점수랑 추가된 팀 인덱스 반환
    if arr[sx][sy]==1:
        return cnt**2, teamarr[sx][sy]
    else :
        teamidx = teamarr[sx][sy]
        hx, hy, tx, ty, length = team[teamidx]
        return (length-(cnt-1)) ** 2, teamidx

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
team = []
teamarr = [[-1]*N for _ in range(N)]

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:                # 머리 발견!

            teamidx = len(team)

            q = deque([(i, j)])
            teamarr[i][j]=teamidx       # 팀어레이에는 몇번째 팀이 다니는 길인지 표시
            cnt = 1                     # 그 팀에 있는 사람 수
            while q:
                x, y = q.popleft()
                for dx, dy in dxdy:
                    nx, ny = x+dx, y+dy
                    if not (0<=nx<N and 0<=ny<N): continue
                    if teamarr[nx][ny]!=-1: continue
                    if arr[nx][ny]==0: continue
                    if arr[nx][ny]!=4: cnt+=1
                    if arr[nx][ny]==3:
                        tx, ty = nx, ny
                    teamarr[nx][ny]=teamidx
                    q.append((nx, ny))

            # 머리 좌표, 꼬리좌표, 사람 수
            team.append((i, j, tx, ty, cnt))

ans = 0
for round in range(K):
    # [1] 이동
    move()

    # [2] 공던지기 ( 공 맞은 사람의 인덱스 )
    sx, sy = throw()

    # [3] 공 맞은 사람이 있으면 점수 계산하고 머리 꼬리 바꾸기
    if sx!=-1:

        # 점수계산
        point, teamidx = score(sx, sy)
        ans += point

        # 머리꼬리 바꾸기
        hx, hy, tx, ty, length = team[teamidx]
        arr[hx][hy], arr[tx][ty] = arr[tx][ty], arr[hx][hy]
        team[teamidx]=(tx, ty, hx, hy, length)

print(ans)
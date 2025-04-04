'''
제출횟수 : 7회
    -> 틀렸습니다 3회 + 런타임에러 1회 + 틀렸습니다 1회 (애먼곳 고치다가)
    -> 이후 계시 받은 것 처럼 틀린 부분 깨달음
    -> 메모리 초과 1회
    -> 시야에서 전사만났을때 미리 방문표시 하는 것에서 visited continue를 안함
    -> 추가해서 맞았습니다
풀이시간 : 3시간 28분

실행시간 : 243ms
메모리 : 25MB

구상 : 12분
* 와 시야 어떻게 처리해;;;;;;;; 귀찮은 일이네,,, 방문처리로 처리해야지,,,
* 가려지는 시야 방향 뭐 어쩌라는거야?!?!?!?

구현 및 검증: 1시간 30분
* 모듈별로 검증하면서 구현

디버깅 : 1시간 46분
* hiddenTC 틀렸습니다 -> 이유 파악을 못함 -> 모든 모듈을 다른 로직으로 짜봄
* 그러다가 바뀐 모듈들에서 여러번 틀렸습니다
* 2시간 15분이 지났을 떄 틀린 이유를 드디어 찾고 해당 부분을 수정함 -> 메모리초과
* 메모리 초과날만한 부분이 뻔해서 바로 수정하고 제출

[ 시간 복잡도 ]
O(N^2*(N^2+M))

[ 테스트 케이스 ]
9 3
0 5 0 0
4 2 4 4 6 6
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

9 6
5 4 0 4
2 2 4 2 4 5 4 6 4 7 4 8
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

4 1
0 0 3 3
1 1
0 0 0 0
1 1 1 1
1 1 1 1
0 0 0 0
'''

from collections import deque

# BFS로 메두사 길 찾아주기
def make_move_medusa():

    q = deque([[(mx, my)]])                 # 지나온 길을 저장
    visited = [[0]*N for _ in range(N)]
    visited[mx][my]=1

    while q:

        root = q.popleft()
        x, y = root[-1]                             # 직전 좌표

        if (x, y)==(ex, ey):                        # 목적지 도착하면 우선순위순서로 왔으니까
            return root                             # 해당길이 최단거리 최고우선순위임

        for d in range(4):
            dx, dy = dxdy[d]
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<N): continue
            if road[nx][ny]!=0: continue            # 길로만 가기
            if visited[nx][ny]: continue

            visited[nx][ny]=1
            q.append(root+[(nx, ny)])

    return []                                       # 못가면 빈배열 반환


# 메두사가 쳐다보는 방향 찾기
def stare():
    cnt = -1
    res = 0
    for d in range(4):                                      # 네 방향 다 보면서
        tmpcnt = 0
        tmparea = [[0]*N for _ in range(N)]
        visited = [[0]*N for _ in range(N)]

        dx, dy = dxdy[d]
        if dx==0: sdxdy = ((-1, dy), (0, dy), (1, dy))      # 진행방향 저장
        elif dy==0: sdxdy = ((dx, -1), (dx, 0), (dx, 1))

        q = deque([(mx, my)])
        visited[mx][my]=1

        while q:
            x, y = q.popleft()

            for sdx, sdy in sdxdy:
                nx, ny = x+sdx, y+sdy
                if not(0<=nx<N and 0<=ny<N): continue
                if visited[nx][ny]: continue

                visited[nx][ny]=1
                tmparea[nx][ny]=1
                q.append((nx, ny))


                # 전사를 만나면 가려지는 부분 미리 방문표시 해두기
                if warrior[nx][ny]:
                    tmpcnt += warrior[nx][ny]

                    # 전사의 8분면에 따른 가려지는 진행방향
                    if dx == 0:
                        if nx < mx:     wdxdy = ((0, dy), (-1, dy))
                        elif nx == mx:  wdxdy = ((0, dy),)
                        else:           wdxdy = ((0, dy), (1, dy))
                    else:
                        if ny < my:     wdxdy = ((dx, 0), (dx, -1))
                        elif ny == my:  wdxdy = ((dx, 0),)
                        else:           wdxdy = ((dx, 0), (dx, 1))

                    # 전사위치부터 wdxdy 따라가면서 방문표시하기
                    wq = deque([(nx, ny)])
                    while wq:
                        wx, wy = wq.popleft()
                        for wdx, wdy in wdxdy:
                            nwx, nwy = wx + wdx, wy + wdy
                            if not (0 <= nwx < N and 0 <= nwy < N): continue
                            # 이거 없어서 메모리초과
                            if visited[nwx][nwy]: continue
                            visited[nwx][nwy] = 1
                            wq.append((nwx, nwy))

        # 전사 수가 더 많으면
        # 돌된 전사 수, 시야 배열 업데이트하기
        if tmpcnt>cnt:
            cnt = tmpcnt
            res = tmparea

    return cnt, res


def warrior_move():

    newwarrior = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if warrior[i][j]==0: continue

            # 메두사의 시야는 안움직이니까 그냥 옮기기
            if stare_area[i][j]:
                newwarrior[i][j] += warrior[i][j]
                continue

            # 첫번쨰 이동
            x, y = i, j
            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy
                if not(0<=nx<N and 0<=ny<N): continue
                if abs(nx-mx)+abs(ny-my)>=abs(x-mx)+abs(y-my): continue
                if stare_area[nx][ny]: continue
                x, y = nx, ny
                break

            # 두번째 이동
            if (x, y)!=(mx, my):
                for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    nx, ny = x+dx, y+dy
                    if not(0<=nx<N and 0<=ny<N): continue
                    if abs(nx-mx)+abs(ny-my)>=abs(x-mx)+abs(y-my): continue
                    if stare_area[nx][ny]: continue
                    x, y = nx, ny
                    break

            # 이동횟수에 더해주기
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!! 전사 수도 곱해서 더해야지 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            ans[0] += (abs(i-x)+abs(j-y))*warrior[i][j]

            # 메두사랑 만나면 공격한 사람 수에 더하기
            if (x, y)==(mx, my):
                ans[2] += warrior[i][j]

            # 아니면 자리 옮기기
            else : newwarrior[x][y] += warrior[i][j]

    return newwarrior


#================================main======================
N, M = map(int, input().split())
dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))
mx, my, ex, ey = map(int, input().split())
wdata = list(map(int, input().split()))
warrior = [[0]*N for _ in range(N)]
for i in range(M):
    wx, wy = wdata[i*2], wdata[i*2+1]
    warrior[wx][wy] += 1

road = [list(map(int, input().split())) for _ in range(N)]

# 매두사 최단경로 미리 찾아두기
move_medusa = make_move_medusa()

if len(move_medusa)==0:                 # 갈 길이 없어요
    print(-1)
else:
    for mx, my in move_medusa[1:-1]:    # 길 따라가면서
        ans = [0]*3

        if warrior[mx][my]!=0:          # 메두사가 공격한 경우
            warrior[mx][my]=0

        cnt, stare_area = stare()       # 메두사 쳐다보고 돌로 만들기
        ans[1] += cnt

        warrior = warrior_move()        # 전사들 움직이기
        print(*ans)

    # 목적지 도착했으니까 0 출력
    print(0)
'''
제출횟수 : 2회
풀이시간 : 41분

* 틀렸습니다 1회 : 또 인덱스를 잘못썻ㅆ다,, arr[i][j]-=amount 해야하는데 arr[x][y]-=amount
'''
from collections import deque

N, M, K = map(int, input().split())
dxdy = ((0, -1), (-1, 0), (0, 1), (1, 0))
arr = [list(map(int, input().split())) for _ in range(N)]
wall = [[[0]*4 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, s = map(int, input().split())
    if s==0:
        wall[x-2][y-1][3]=1
        wall[x-1][y-1][1]=1
    else:
        wall[x-1][y-2][2]=1
        wall[x-1][y-1][0]=1

cool = [[0]*N for _ in range(N)]
check = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==0: continue
        if arr[i][j]==1:
            check.append((i, j))
            continue

        d = arr[i][j]-2
        dx, dy = dxdy[d]
        cool[i+dx][j+dy] += 5
        visited = [[0]*N for _ in range(N)]
        visited[i+dx][j+dy]=1
        q = deque([(i+dx, j+dy, 5)])
        while q:
            x, y, n = q.popleft()

            if wall[x][y][d]==0:
                nx, ny = x+dx, y+dy
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                    visited[nx][ny]=1
                    cool[nx][ny]+=n-1
                    if n-1!=1:
                        q.append((nx, ny, n-1))

            for nd in ((d+1)%4, (d-1)%4):
                if wall[x][y][nd]==0:
                    ndx, ndy = dxdy[nd]
                    nx, ny = x+ndx, y+ndy
                    if 0<=nx<N and 0<=ny<N:
                        if wall[nx][ny][d]==0:
                            nx, ny = nx+dx, ny+dy
                            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                                visited[nx][ny] = 1
                                cool[nx][ny] += n - 1
                                if n - 1 != 1:
                                    q.append((nx, ny, n - 1))

arr = [[0]*N for _ in range(N)]
for time in range(0, 101):

    for x, y in check:
        if arr[x][y]<K: break
    else:
        print(time)
        break

    for i in range(N):
        for j in range(N):
            arr[i][j]+=cool[i][j]

    tmp = [ele[:] for ele in arr]
    for i in range(N):
        for j in range(N):
            for d in range(4):
                if wall[i][j][d]: continue

                dx, dy= dxdy[d]
                nx, ny = i+dx, j+dy
                if not(0<=nx<N and 0<=ny<N): continue
                if tmp[i][j]>tmp[nx][ny]:
                    amount = (tmp[i][j]-tmp[nx][ny])//4
                    arr[i][j]-=amount
                    arr[nx][ny]+=amount

    for i in range(N):
        if arr[i][0]>0: arr[i][0]-=1
        if arr[i][N-1] > 0: arr[i][N-1]-=1
    for j in range(1, N-1):
        if arr[0][j]>0: arr[0][j]-=1
        if arr[N-1][j] > 0: arr[N-1][j]-=1

else:
    print(-1)

'''
제출횟수 : 2회
풀이시간 : 1시간 38분

[ 명심할 것 ]
* 가장 효율적으로 짤 필요 없다고 생각하고 널널하게 짜다간
* 들어가면 안되는 값까지 들어갈 수 있으니
* 그냥 신중하게 가장 타이트한 코드를 만들자
!!!!!!!!!!!!!!!!!!!!!!나를 믿지 말것!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

[ 시간 복잡도 ]
100*(바람나오기 + 바람퍼트리기 + 가생이 식히기 + 채크)
100*(15N^2 + 4*N^2 + 2N + N^2)
100*20N^2
800_000 의 상수배

[ 엣지 케이스 ] : 내가 틀린거...
7 8 1
0 0 1 0 0 0 0 5
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0
0

구상 : 9분
* 벽 어떻게 관리할지 결정
구현 : 36분
* 중간에 함수들 잘 돌아가는지 채크하면서 진행
디버깅 : 53분
[1] (6분) 온도 조절 할 때 벽 안세워서 openTC 틀림 -> 수정하고 제출 -> 틀렸습니다
[2] (32분) 틀렸습니다 원인 찾기,,, 그 과정에서 c의 범위가 c>0일 필요 없다고 생각하고 수정
[3] (15분) [2]번에서 고친게 틀렸습니다의 원인이었는데,,, 인지하지 못하고 계속 디버깅
            아무리봐도 틀린게 없어서 다시 한 번 내봤더니 맞았습니다!
            엥?!?!?!!?!?? 하고 바뀐게 뭐였지 하고 봤더니 아니,,,ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

from collections import deque

def wind():
    for hx, hy, hd in heater:

        # 옆으로 퍼져나가는 방향
        if hd<2: side = {2, 3}
        else : side = {0, 1}

        visited = set()
        dx, dy = dxdy[hd]
        nx, ny = hx+dx, hy+dy

        # 온풍기 다음은 무조건 칸이니까 q에 넣고 시작
        q = deque([(5, nx, ny)])
        visited.add((nx, ny))
        arr[nx][ny] += 5

        while q:
            c, x, y = q.popleft()

            # 진행 방향으로 갈 수 있으면 가기
            if not wall[x][y][hd]:
                nx, ny = x+dx, y+dy
                if 0<=nx<N and 0<=ny<M and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        arr[nx][ny] += c-1
                        ###################################
                        ########### c>0으로 보내면 #########
                        ##### 다음 칸에 -1이 더해지지요 #####
                        ###################################
                        if c > 2:
                            q.append((c-1, nx, ny))

            # 대각선 위 아래로 갈 수 있으면 가기
            # 이때 벽 확인을 위해서 옆으로 이동 -> 진행방향으로 이동
            for sd in side:
                sdx, sdy = dxdy[sd]
                if not wall[x][y][sd]:
                    nx, ny = x+sdx, y+sdy
                    if 0<=nx<N and 0<=ny<M:
                        if not wall[nx][ny][hd]:
                            nx, ny = nx+dx, ny+dy
                            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                                visited.add((nx, ny))
                                arr[nx][ny] += c - 1
                                if c > 2:
                                    q.append((c - 1, nx, ny))


def spread():
    tmp = [ele[:] for ele in arr]
    for i in range(N):
        for j in range(M):
            for d in range(4):
                dx, dy = dxdy[d]
                nx, ny = i+dx, j+dy
                if not(0<=nx<N and 0<=ny<M): continue
                # 내가 더 큰 경우에만 퍼트리기
                if tmp[nx][ny]<tmp[i][j] and not wall[i][j][d]:
                    dist = tmp[i][j]-tmp[nx][ny]
                    arr[i][j]-=dist//4
                    arr[nx][ny]+=dist//4

def cool():
    # 가장자리 식히기
    for i in range(N):
        if arr[i][0]!=0: arr[i][0] -= 1
        if arr[i][M-1]!=0: arr[i][M-1] -= 1

    for j in range(1, M-1):
        if arr[0][j]!=0: arr[0][j] -= 1
        if arr[N-1][j]!=0: arr[N-1][j] -= 1


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((0, 1), (0, -1), (-1, 0), (1, 0))

# 온풍기에는 좌표, 바람방향 / 점검 위치에 좌표 저장
heater = []
check = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==5:
            check.append((i, j))
            arr[i][j]=0
        elif arr[i][j]!=0:
            heater.append((i, j, arr[i][j]-1))
            arr[i][j]=0

W = int(input())
# 각 칸의 어떤 방향이 벽인지 저장
wall = [[[0]*4 for _ in range(M)] for _ in range(N)]
for _ in range(W):
    x, y, d = map(int, input().split())
    if d==0:
        wall[x-1][y-1][2]=1
        wall[x-2][y-1][3]=1
    else :
        wall[x-1][y-1][0]=1
        wall[x-1][y][1]=1

# 온풍기 가동
for ans in range(1, 102):
    wind()
    spread()
    cool()

    # 점검하기
    for x, y in check:
        if arr[x][y]<K:
            break
    else : break

print(ans)

'''
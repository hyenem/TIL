'''
제출횟수 : 2회
    * 틀렸습니다 : 시간 이상 현상이 탈출구로는 안간다는 걸 놓침 -> 5분 디버깅
풀이시간 : 1시간 54분

실행시간 : 51ms
메모리 : 17MB

구상 : 13분
* 와,,,,,,,,,이동 어케해,,,,,,,,,,,,,,,,,
* 험난한 하드코딩이 예상된다,,,,,,,,,,,,,,,,,,,,,,,,,,,
* bfs는 미리 이상 시간 현상 기록하고, 방문 시간보다 작은걸로 가면되겟다

구현 및 디버깅 : 1시간 25분
* move랑 fint_exit 완성해서 이동잘 하는지 확인 가능하는데 39분 걸림 (52분)
* 아래 코드 이용해서 모든 방향 모든 케이스 다 이동해보는데 10분걸림 (62분)
            # print(exit_t, exit_u)
            # x, y, z = 0, 0, 4
            # while True:
            #     res, x, y, z = move(x, y,z, int(input()))
            #     print(x, y, z)
* 시간 이상 현상 도착 시간 기록하는데 구현 10분 검증 20분 (1시간 31분)
* BFS 함수 구현 및 검증 7분

디버깅 및 검증 : 16분
* 코드 한 줄 한 줄 보기
    -> 출구 좌표를 이상하게 처리하게되어있음(x, y, i, j 혼용) -> 수정
* 틀렸습니다 -> 이상 시간 현상이 출구로 못가게 수정

리팩토링
* visited_u(미지의 공간) 과 visited_t(시간의 벽) 을 합침
* 이상 시간 현상이 시간의 벽을 안타고 올라가도 된다는걸 깨달았는데
    그걸 고치는건 너무 대공사라 그냥 두기로함~~~~~~~~


[ 시간 복잡도 ]
O(5*M^2 + N^2)

[ 테스트 케이스 ]
8 4 3
4 0 0 0 0 0 0 0
0 1 1 1 1 1 1 0
0 1 3 3 3 3 1 1
0 0 3 3 3 3 1 1
0 1 3 3 3 3 1 0
0 1 3 3 3 3 1 0
0 1 1 1 1 1 1 0
0 0 0 0 0 0 1 1
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 7 1 14
6 3 3 2
4 5 1 5
-> 이동 검증
-> 다른 방향 출구 확인
-> 시간의 벽으로 이상시간현상 올라가는지 확인

'''

from collections import deque

# 각 위치별 다음 칸을 뱉어내는 함수
def move(x, y, z, d):
    dx, dy = dxdy[d]
    nx, ny = x+dx, y+dy


    # 미지의 공간에 있으면
    # 바깥으로 나가거나 벽인경우 못가고, 3이랑 연결되어있으면 거기가 출구 -> 시간의 벽으로 입성
    if z==5:
        if not(0<=nx<N and 0<=ny<N) or unknown[nx][ny]==1:
            return 0, x, y, z
        if unknown[nx][ny]==3:
            nx, ny, nz= exit_t
            return 1, nx, ny, nz
        return 1, nx, ny, z


    # 그 외의 경우 시간의 벽
    # 같은 면으로 움직이면 벽인지 아닌지만 채크하면 됨
    if 0<=nx<M and 0<=ny<M:
        if timewall[z][nx][ny]==1:
            return 0, x, y, z
        else:
            return 1, nx, ny, z

    # 나머지는 면이 바뀌는 경우
    # 다음 칸 위치 하드코딩
    if z==4:
        nx, nz = 0, d
        if d == 0:
            ny = M-1-y
        elif d==1:
            ny = M-1-x
        elif d==2:
            ny = y
        else :
            ny = x

    else:
        if (x, y, z)==exit_t and d==2:
            return 1, exit_u[0], exit_u[1], exit_u[2]

        if d==0:
            nz = 4
            if z==0: nx, ny = 0, M-1-y
            elif z==1: nx, ny = M-1-y, M-1
            elif z==2: nx, ny = M-1, y
            else : nx, ny = y, 0

        elif d==1:
            nz = (z+3)%4
            nx, ny = x, 0

        elif d==3:
            nz = (z+1)%4
            nx, ny = x, M-1
        else:
            return 0, x, y, z


    if timewall[nz][nx][ny] == 1:
        return 0, x, y, z
    else:
        return 1, nx, ny, nz




def find_exit():
    for i in range(N):
        for j in range(N):
            if unknown[i][j] == 3:
                # 3이 하나라도 나오면 M*M 정사각형 돌면서 출구 찾기
                for x in range(M):
                    for y in range(M):
                        for d in range(4):
                            dx, dy = dxdy[d]
                            nx, ny = x + dx, y + dy
                            if not(0<=i+nx<N and 0<=j+ny<N): continue

                            # 3 주위에 0이 있으면 탈출구!
                            if unknown[i+nx][j+ny] in {0, 4}:
                                exit_u = (i+nx, j+ny, 5)

                                # 탈출구랑 연결되어있는 시간의 벽 좌표 찾기
                                nx = M - 1
                                if dx == 1:
                                    ny, nz = y, 2
                                elif dx == -1:
                                    ny, nz = M-1-y, 0
                                elif dy == 1:
                                    ny, nz = M-1-x, 1
                                else:
                                    ny, nz = x, 3

                                return (nx, ny, nz), exit_u

def bfs(i, j):
    q = deque([(0, i, j, 4)])
    visited[4][i][j] = 0

    while q:
        time, x, y, z = q.popleft()
        if z==5 and unknown[x][y]==4:
            return time

        for d in range(4):
            res, nx, ny, nz = move(x, y, z, d)
            if not res: continue

            # visited 배열에는 이상 시간 현상과 내가 지나간 시간 중 작은게 표시되어있음
            # visited 에 표시되어있는 시간보다 작은 시간엔 이동할 수 있음
            if visited[nz][nx][ny]>time+1:
                visited[nz][nx][ny]=time+1
                q.append((time+1, nx, ny, nz))

    return -1

def go():
    for i in range(M):
        for j in range(M):
            # 윗면에서 타임머신 찾아서 탈출시키기
            if timewall[4][i][j]==2:
                return bfs(i, j)


#=============================================main=================================================
N, M, F = map(int, input().split())
unknown = [list(map(int, input().split())) for _ in range(N)]
timewall = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]
timewall[0], timewall[1], timewall[3] = timewall[3], timewall[0], timewall[1]
strange = [tuple(map(int, input().split())) for _ in range(F)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
visited = [[[800]*M for _ in range(M)] for _ in range(5)] + [[[800]*N for _ in range(N)]]


# move 함수 검증
# 직접 이동 방향 입력해서 순차적으로 이동하는 것 확인할 수 있음

# x, y, z = 0, 0, 4
# while True:
#     res, x, y, z = move(x, y,z, int(input()))
#     print(x, y, z)



# 시공의 벽과 미지의 영역 연결하는 부분 찾아주기
exit_t, exit_u= find_exit()


# 시간 이상 현상 표시하기
# 동서남북 -> 북동남서
changed = [1, 3, 2, 0]
for r, c, d, v in strange:
    d = changed[d]

    x, y, z = r, c, 5
    time = 0
    visited[z][x][y]=0
    while True:
        time += v
        res, nx, ny, nz = move(x, y, z, d)

        if not res: break
        # 탈출구로는 퍼지면 안돼!!!!!!!!!!!!!!
        if nz==5 and unknown[nx][ny]==4: break

        # 시간 이상 현상이 도착하는 시간을 visit배열에 표시
        visited[nz][nx][ny]=min(visited[nz][nx][ny], time)

        # 면이 바뀌면 진행 방향이 바뀐다
        if z==5 and nz!=5: d = 0
        elif 0<=z<4 and nz==4: d = (z+2)%4
        elif 0<=z<4 and nz==5: d = z
        elif z==4 and nz!=4: d = 2

        x, y, z = nx, ny, nz


ans = go()
print(ans)


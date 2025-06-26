'''

[ 시간 복잡도 ]
N*M*K의 상수배

[ 오해할 만한 점 ]
* 공격력 증가가 일시적인것인지 ? 영구적인 것인지?
* 나도 공격 받을 수 있나?
* 레이저는 직진만 할 수 있나? 아니다

[ 선정 이유 ]
* 깔꼼한 함수화
* 수리 대상 set으로 안하고 테이블로 보기
* 종료조건 일일이 안세어보고, 공격받는 터렛이랑 공격 하는 터렛 같으면 으로 처리

'''

from collections import deque



# 공격자와 수비자를 한번에 고르도록 리팩토링
def choose():
    minATT, mtime = 5001, 0
    maxATT, Mtime = 0, time
    atx, aty, bfx, dfy = -1, -1
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0: continue

            # 정해진 우선순위대로 고르기
            if (arr[i][j], -attack_time[i][j], -i-j, -j)<=(minATT, -mtime, -atx-aty, -aty):
                atx, aty = i, j
                minATT, mtime = arr[i][j], attack_time[i][j]

            if (arr[i][j], -attack_time[i][j], -i-j, -j)>=(maxATT, -Mtime, -dfx-dfy, -dfy):
                dfx, dfy = i, j
                maxATT, Mtime = arr[i][j], attack_time[i][j]

    return atx, aty, dfx, dfy





def shoot_laser(root):
    # 피공격칸은 따로 처리할꺼니까 없애주고
    root.pop()

    # 가는 길에 공격력 감소시키기
    for x, y in root:
        arr[x][y] = max(0, arr[x][y]-arr[atx][aty]//2)
        defence_time[x][y] = time

    # 피공격칸 공격력 감소시키기
    arr[dfx][dfy] = max(0, arr[dfx][dfy]-arr[atx][aty])
    defence_time[dfx][dfy]=time

# BFS 돌기
def find_laser():
    lx, ly = atx, aty
    visited = [[0]*M for _ in range(N)]
    visited[lx][ly]=1

    # 좌표와 지나온 길(리스트)을 저장
    q = deque([(lx, ly, [])])

    while q:
        x, y, root = q.popleft()
        if x==dfx and y==dfy:
            shoot_laser(root)
            return 1

        for d in range(4):
            dx, dy = dxdy[d]
            nx, ny = (x+dx)%N, (y+dy)%M
            if visited[nx][ny]: continue
            if arr[nx][ny]<=0: continue

            visited[nx][ny]=1
            q.append((nx, ny, root+[(nx, ny)]))

    return 0


def shoot_bomb():
    # 피공격칸 점수 깍기
    arr[dfx][dfy] = max(0, arr[dfx][dfy] - arr[atx][aty])
    defence_time[dfx][dfy]=time

    # 팔방 보고 공격칸 아니면 점수 깎기
    for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        nx, ny = (dfx+dx)%N, (dfy+dy)%M
        if nx==atx and ny==aty: continue

        defence_time[nx][ny]=time
        arr[nx][ny] = max(0, arr[nx][ny]-arr[atx][aty]//2)




# 이번 시간에 공격받지도, 하지도 않았으면 수리하기
def repair():
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0: continue
            if attack_time[i][j]==time: continue
            if defence_time[i][j]==time: continue
            arr[i][j]+=1


#=========================================================================================
#=========================================================================================

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
attack_time = [[0]*M for _ in range(N)]         # 공격시간 저장(repair 및 우선순위 용)
defence_time = [[0]*M for _ in range(N)]        # 공격 받은 시간 저장(repair 용)
dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))

for time in range(1, K+1):

    # 공격자와 피공격자를 찾음
    atx, aty, dfx, dfy = choose()

    # 공격자와 피공격자가 같다는 것은, 전체가 한 명 뿐이라는 것
    # 종료 조건임
    if (atx, aty) == (dfx, dfy) : break

    # 공격자한테 핸디캡
    arr[atx][aty] += M+N

    # 공격
    attack_time[atx][aty]=time
    if not find_laser():
        shoot_bomb()

    # 수리
    repair()

ans = max(map(max, arr))
print(ans)
'''
제출횟수 : 1회
풀이시간 : 1시간  26분

[ 오해한 점 ]
* 피공격자의 우선순의가 공격 시간이 아니라 공격 받은 시간인 줄 알았음
    => 그럼 레이저 날라가는 길이나 폭탄 주변의 아이들이 공격받은 시간도 포함되나?
* 레이저는 직진만 할 수 있나? 아니다

[ 타임라인 ]
구상 : 16분
* 밑에 레이저 예시 있는지 모르고 레이저 어케 돌아가는지 파악하는데 시간이 오래걸림

구현 : 50분
* 단계별 검증을 위해서 최대한 함수화하려고 노력함
* 함수 하나 만들 때 마다 잘 돌아가는지 검증하고 넘어감

검증 및 디버깅 : 20분
* 아레 엣지 케이스 돌리고 수정하기(10분)
* 코드 정독하기(10분)

[ 시간 복잡도 ]
N*M*K의 상수배

[ 엣지 케이스 ]
[1] 내가 걸린 감사한 엣지케이스

4 4 12
0 0 0 0
0 0 0 0
0 0 0 0
4 0 0 0
-> 정답 12나옴(4인데)
-> 공격자와 피공격자 찾고, 그 좌표 비교해서
-> 공격자를 찾는 과정에서 핸드캡을 줘버려서 4+M+N이 답이 나옴
-> end 조건을 for 문 마치자마자 전체 순회하면서 세어서 해결

4 4 12
0 12 12 12
12 0 0 0
0 12 12 12
4 0 0 0
-> 공격자와 피공격자가 같은 위치가 됨
-> 공격자와 피공격자 찾고, 그 좌표 비교해서
-> 공격자를 찾는 과정에서 핸드캡을 줘버려서
-> 피공격자 선정 과정에서 이미 공격자가 최고 세진애가 되어버릴 수 있음

-> 결국 위의 두 가지를 모두 해결하기 위해서
-> 피공격자까지 고르고, 핸디캡을 종료 조건 채크(공격자 피공격자 같은지) 하고 처리함



[2] 공격자, 피공격자 함수 만든 뒤 우선순위 확인용
4 4 12
0 12 12 4
0 0 0 0
0 0 12 12
4 0 4 0

[3] M, N 다른 경우

1 4 2
1 1 0 0

4 1 2
1
1
0
0
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
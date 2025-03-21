'''
제출 횟수 : 1회
풀이 시간 : 34분

실행 시간 : 99ms
메모리 : 18MB

[ 시간 복잡도 ]
N^2 의 상수배
N최대 29 -> 문제없음

[ 엣지 케이스 ] : 전부 다 같은 색인 경우
5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1

구상 : 4분
* 오케 bfs 랑 배열 회전~
* 경계 세는게 좀 까다로울 것 같은데?
    하지만 전체 다 세면서 경계 다 더해놓으면 되니까 괜찮지
구현 : 27분
* 구현하면서 모듈별 디버깅 같이 함
검증 : 3분
* 5짜리 밖에 없어서 7짜리 만들어서 회전 잘 되나 확인해봄

'''

def make_group():
    for i in range(N):
        for j in range(N):
            if carr[i][j] != -1: continue

            # 아직 방문 안한 칸을 만나면, 그 칸의 번호는 len(group)이다.
            # 왜냐하면 계속 group에 append 해주고 있기 때문
            group_num = len(group)

            # bfs 돌면서, 인접한 같은 숫자 칸에 방문
            carr[i][j] = group_num
            q = [(i, j)]
            idx = 0
            while idx < len(q):
                x, y = q[idx]
                idx += 1
                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < N and 0 <= ny < N): continue
                    if carr[nx][ny] != -1: continue
                    if arr[nx][ny] == arr[i][j]:
                        carr[nx][ny] = group_num    # 방문표시 겸 어떤 구역인지 표시
                        q.append((nx, ny))          # q에 넣어주기

            # group의 group_num 인덱스 칸에, 어떤수/몇개 저장
            group.append((arr[i][j], len(q)))


# 전체를 돌면서 우, 하 방향 살펴보고, 다른 그룹이랑 닿아있으면 경계 면 수에 추가
def make_adj():
    for i in range(N):
        for j in range(N):
            for dx, dy in ((0, 1), (1, 0)):
                nx, ny = i + dx, j + dy
                if not (0 <= nx < N and 0 <= ny < N): continue
                if carr[nx][ny] == carr[i][j]: continue

                # 더 작은 그룹번호가 무조건 앞으로 오도록 설정
                if carr[nx][ny]<carr[i][j]:
                    m, M = carr[nx][ny], carr[i][j]
                else :
                    m, M = carr[i][j],  carr[nx][ny],

                # 두 그룹을 연결하는 변의 수 하나 증가
                if (m, M) not in dic: dic[(m, M)] = 0
                dic[(m, M)] += 1


# 서로 다른 두 그룹에 대해서
# 인접해 있으면 점수 계산해서 추가
# ( 인접 안해있으면,, 어차피 점수가 0임 )
def calculate():
    global ans
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            g1_score, g1_cnt = group[i]
            g2_score, g2_cnt = group[j]
            if (i, j) in dic:
                ans += (g1_cnt + g2_cnt) * g1_score * g2_score * dic[(i, j)]


def rotate():
    tmp = [row[:] for row in arr]
    # 십자가 모양은 반시계
    for i in range(N):
        arr[i][N // 2] = tmp[N // 2][N - 1 - i]
        arr[N // 2][i] = tmp[i][N // 2]

    # 나머지 네 덩어리 시계
    for si, sj in ((0, 0), (N // 2 + 1, 0), (0, N // 2 + 1), (N // 2 + 1, N // 2 + 1)):
        for di in range(N // 2):
            for dj in range(N // 2):
                arr[si + di][sj + dj] = tmp[si + N // 2 - 1 - dj][sj + di]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
ans = 0

for k in range(4):

    group = []
    carr = [[-1] * N for _ in range(N)]
    # [1] 그룹화하기
    # carr에는 어떤 그룹인지 기록하고,
    # 해당 인덱스의 그룹이 어떤수, 몇개로 이루어졌는지 저장
    make_group()

    # [2] 인접한 그룹의 경계 찾기
    # dic에 두 그룹 인덱스 중 (작은것, 큰 것)의 인접한 변의 수를 저장
    dic = {}
    make_adj()

    # [3] 지금까지 찾아둔 정보를 바탕을 계산하기
    calculate()

    if k == 3: break
    # [4] 회전하기
    rotate()

print(ans)

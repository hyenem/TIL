'''
제출횟수 : 1회
풀이시간 : 58분

실행시간 : 226mx
메모리 : 23MB

구상 : 8분
* 굴러가는 것 처리 어떻게 할지 고민
* 내려가는 것, 출구처리 어떻게 할지 고민
* 그래서 정령끼리 겹쳐도 된다는거야!?!?!? 별말 없으니까 그렇다고 하자

구현 : 35분
* 모듈별로 검증하며 구현
    -> 그 과정에서 check 룩업테이블 수정

디버깅 및 검증 : 15분
* openTC 2번 걸림
    -> 디버거로 찍어보니 move의 방문표시가 이상했던 탓 -> 수정
* 코드 흐름 처음부터 끝까지 따라가며 읽던 중
    -> 여유분을 위로 두칸만 둬서 처음 시작할 때 왼위, 오위가 무조건 oob난다는 것을 파악
    -> 그렇게 되면 시작하자마자 왼회전, 오회전 필요한 경우 처리가 안돼서
    -> 위로 세칸 여유로 바꾸고 제출

[ 헷갈렸던 점 ]
* 정령끼리 겹쳐있을 수 있나?
* 골렘의 몸이 내부에 다 안들어왔을 때도 회전 할 수 있나?!?

[ 시간복잡도 ]
O(NMK)

[ 테스트케이스 ]
5 5 15
2 0
2 0
2 0
2 0
2 0
2 0
2 0
2 0
2 0
2 0
2 0
2 0
2 0
2 0
2 0
'''


# 골렘을 떨어트리면서, 해당 골렘의 인덱스를 arr에 표시
# 이떄 출구는 마이너스를 붙여서 표시

from collections import deque

def drop(x, y, d, idx):

    while True:                                             # 가장 밑으로 떨어질 떄까지 반복
        for dx, dy, dd, empty in check:
            for edx, edy in empty:                          # 해당 방향으로 이동하려면 비어있어야하는 칸들 채크
                enx, eny = x+edx, y+edy
                if not(0<=enx<N+3 and 0<=eny<M): break      # 범위 밖이거나
                if arr[enx][eny]!=0: break                  # 이미 다른 블럭이잇으면 break
            else:
                x, y, d = x+dx, y+dy, (d+dd)%4              # break 한 번도 안됐으면
                break                                       # 해당 방향으로 회전 및 이동하고 다음
        else:
            break                                           # break 안됐으면 세 방향 다 못가는거니까 끝


    if x<=3:                                                # 내부에 다 못들어왔으면 실패
        return -1, -1

    arr[x][y]=idx                                           # 들어왔으면 arr에 인덱스 표시해주기
    for nd in range(4):
        dx, dy = dxdy[nd]
        nx, ny = x+dx, y+dy
        if nd==d:
            arr[nx][ny]=-idx                                # 출구만 -idx
        else:
            arr[nx][ny]=idx

    return x, y


def move(x, y):
    res = x
    visited = [[0]*(M) for _ in range(N+3)]
    q = deque([(x, y)])
    visited[x][y]=1

    while q:
        x, y = q.popleft()
        res = max(res, x)                                   # 행 최댓값 갱신

        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not (0<=nx<N+3 and 0<=ny<M) or visited[nx][ny]: continue

            if arr[x][y]<0:                                 # 음수면 출구니까
                if arr[nx][ny]:                             # 주변에 0이 아닌 모든칸으로 옮겨가기
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                continue

            if abs(arr[nx][ny])==abs(arr[x][y]):            # 그 외의 경우
                visited[nx][ny] = 1                         # 나랑 절댓값이 같은(같은 골램)으로만 움직이기
                q.append((nx, ny))

    return res-2                                            # 위에 세칸 늘려줫으니까 행 번호 조정

#================================== main =======================================
N, M, K = map(int, input().split())
start = [tuple(map(int, input().split())) for _ in range(K)]
arr = [[0]*M for _ in range(N+3)]

# 중심의 x 변화, y 변화, 출구 방향 변화, 움직이기 위해 필요한 빈칸
check = [(1, 0, 0, ((2, 0), (1, 1), (1, -1))),
         (1, -1, -1, ((-1, -1), (0, -2), (1, -1), (1, -2), (2, -1))),
         (1, 1, 1, ((-1, 1), (0, 2), (1, 1), (1, 2), (2, 1)))]

dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

ans = 0

for idx, (c, d) in enumerate(start, start=1):

    x, y = drop(1, c-1, d, idx)                     # 골렘 떨어트리기 -> 최종 중심 반환
    if x==-1:                                       # 떨어져도 범위를 넘친 경우 -1, -1 반환
        arr = [[0]*M for _ in range(N+3)]           # 전체 비우기
        continue

    ans += move(x, y)                               # bfs로 중심에 있던 정령 내려가기

print(ans)
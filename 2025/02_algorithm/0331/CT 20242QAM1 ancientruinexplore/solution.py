'''
제출횟수 : 1회
풀이시간 : 1시간

실행시간 : 108ms
메모리 : 20MB

[1] 구상 : 6분
* 회전 우선순위 채크
* 채우기 우선순위 채크
[2] 구현 : 43분
* 모듈별 검증하며 구현
* 회전 우선순위 까먹어서 추가함
[3] 디버깅 및 검증 : 10분
* 무한루프 도는 상황 없는지 고민
* 추가 TC 만들어보기
* 코드 처음부터 끝까지 읽어보기

[ 헷갈릴 만한 점 ]
* 벽에 있는 숫자들을 mode로 반복 사용하는 줄 알았음
* 종료되지 않고 무한루프 도는 경우는 없나?

[ 시간복잡도 ]
N=5
K*(N-2)^2*(36+N^2) + M*N^2
O(K * N**4 + M * N**2)

K*9*(36+25)+M*25

[ 테스트 케이스 ]
2 20
00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
30 31 32 33 34
40 41 42 43 44
3 2 3 5 2 4 6 1 3 2 5 6 2 1 5 6 7 1 2 3
-> 회전 채크용
'''

def turn(arr, x, y, a):
    tmp = [ele[:] for ele in arr]           # 참조할 배열
    tmparr = [ele[:] for ele in arr]        # 실제 반환할 배열
    for _ in range(a):                      # angle번 돌리기
        for i in range(3):
            for j in range(3):
                tmparr[x - 1 + i][y - 1 + j] = tmp[x + 1 - j][y - 1 + i]

        tmp = [ele[:] for ele in tmparr]    # 다음 회전을 위해 참조 배열 업데이트

    return tmparr


def pop(arr):

    visited = [[0] * 5 for _ in range(5)]
    score = 0
    for i in range(5):
        for j in range(5):
            if visited[i][j]: continue


            visited[i][j] = 1
            q = [(i, j)]
            qidx = 0

            while qidx < len(q):
                x, y = q[qidx]
                qidx += 1
                for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < 5 and 0 <= ny < 5) or visited[nx][ny]: continue
                    if arr[nx][ny] == arr[x][y]:            # 네방향 돌면서 색이 같으면
                        visited[nx][ny] = 1                 # 방문표시하고
                        q.append((nx, ny))                  # q에 넣기

            if len(q) >= 3:                                 # 인접한 블럭이 3개 이상이었으면
                score += len(q)                             # 점수 추가하기
                for x, y in q:
                    arr[x][y] = 0                           # 터진 블럭 0으로 바꾸기

    return score


def fill():
    global idx
    for j in range(5):                                      # 왼쪽에서 오른쪽으로 가면서
        for i in range(4, -1, -1):                          # 아래에서 위쪽으로 채워주기
            if arr[i][j] == 0:
                arr[i][j] = sub[idx]
                idx = (idx + 1) % M


# ======================== main =============================
K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
sub = list(map(int, input().split()))
idx = 0

ans = []
for _ in range(K):

    # 점수, -회전각, -중심좌표열
    p = (-1, -5, -6)
    newarr = []
    for i in range(1, 4):
        for j in range(1, 4):
            for a in range(1, 4):
                tmparr = turn(arr, i, j, a)             # i, j 중심으로 회전
                res = pop(tmparr)                       # bfs돌면서 터진블럭 0으로 바꾸고, 점수 계산하기

                if p < (res, -a, -j):                   # 기존 저장돼있는 것 보다 더 좋은 우선순위면
                    newarr = tmparr                     # 배열이랑 우선순위 덮어씌우기
                    p = (res, -a, -j)

    arr = newarr
    score = p[0]
    if score == 0:                                      # 한 점도 못얻으면 그만
        break

    fill()                                              # 0으로 바뀐(터진 블럭)부분 채우기

    while True:
        newscore = pop(arr)                             # bfs
        if newscore == 0: break                         # 추가로 터질 블럭없으면 그만하기

        score += newscore                               # 점수에 추가해주기
        fill()                                          # 새 블럭 채우기

    ans.append(score)                                   # 정답 배열에 이번턴 점수 추가

print(*ans)

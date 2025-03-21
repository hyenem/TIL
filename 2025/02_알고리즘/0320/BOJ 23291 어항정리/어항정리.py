'''
[ 코드 선정 이유 ]
* 반시계로 돌리고 아래로 쌓아서 1차원 만들 때 전치만 하면 된다!!!!!!!
* 전치는 가장 작은 행을 바탕으로 된다는 걸 잘 활용함
* 파이썬의 축복 완벽 활용
* 104ms의 최적화

[ 주의할 점 ]
* 어항 정리를 한번도 안할수도 있지 않을까? -> 백준에는 없었네

[ 시간 복잡도 ]
시행횟수 10000번 이하
매 시행 당 첫번쨰 어항 쌓기 N^2, 나머진 N
100_000_000 의 상수배

[ 엣지 케이스 ]
8 1
5 5 5 5 5 5 5 5
출력: 0
<< 시작하자마자 조건 달성
    이 테케 만족하지 않아도 백준 통과됨
12 1
1 2 3 4 5 6 7 8 9 10 11 12
출력: 4
<< 돌돌 말았을 때 가로세로가 딱 맞는다

'''

def spread():
    tmp = [ele[:] for ele in arr]
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nx, ny = i + dx, j + dy
                if 0 <= nx < len(tmp) and 0 <= ny < len(tmp[nx]):
                    if tmp[i][j] > tmp[nx][ny]:
                        dist = tmp[i][j] - tmp[nx][ny]
                        arr[i][j] -= dist // 5
                        arr[nx][ny] += dist // 5


N, K = map(int, input().split())
arr = list(map(int, input().split()))

time = 0
while True:

    # [1] 최대최소 차 확인 + 최소 인덱스 1씩 올려주기
    # 한번도 안해도 되려나? 하는 생각에
    # 최소인 어항 인덱스 찾기랑 검사 로직을 한번에 함

    m, M = 10001, 0
    midx = []
    for i in range(N):
        if m > arr[i]:
            m = arr[i]
            midx = [i]
        elif m == arr[i]:
            midx.append(i)
        m, M = min(m, arr[i]), max(M, arr[i])

    if M - m <= K:             # 더이상 어항정리 안해도 되는 상황
        print(time)
        break

    time += 1               # 안끝났으면 시간 1 올려주기
    while midx:             # 최소인 어항에 물고기 넣기
        arr[midx.pop()] += 1


    # [2] 어항 쌓기
    arr = [arr[1:], [arr[0]]]
    while True:
        tail = arr[0][len(arr[1]):]                 # 1층짜리
        if len(arr) > len(tail): break
        head = list(map(list, zip(*arr)))[::-1]     # zip은 최소 사이즈 행을 기준이라 2층 이상만 처리됨
        arr = [tail] + head                         # 나는 아래로 쌓으니까 반시계

    # [3] 조정하기
    spread()

    # [4] 다시 1층으로 만들기
    tail = arr[0][len(arr[1]):]
    head = list(map(list, zip(*arr)))           # 반대로 쌓아놓은 덕분에
    arr = []                                    # 전치해서 합쳐주면 됨
    for ele in head:
        arr += ele
    arr += tail

    # [5] 어항 다른 방법으로 쌓기
    l = N // 4                # 뒤집고 뒤집는 작업은 네등분해서 각각 뒤집기로 처리가능
    P1, P2, P3, P4 = arr[:l], arr[l:2 * l], arr[2 * l:3 * l], arr[3 * l:]
    arr = [P4, P1[::-1], P2, P3[::-1]]

    # [6] 조정하기
    spread()

    # [7] 다시 1층으로 만들기
    head = list(map(list, zip(*arr)))
    arr = []
    for ele in head:
        arr += ele

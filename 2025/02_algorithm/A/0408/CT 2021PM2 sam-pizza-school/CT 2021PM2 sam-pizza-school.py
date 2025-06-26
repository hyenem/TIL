'''2회독
제출횟수 : 2회
    * min(lst)값이 변한다는걸 인지를 못함
    * 안하던거 하지말자,,, 그냥 쓰던거 쓰자
풀이시간 : 21분
'''

def spread(arr):
    tmp = [ele[:] for ele in arr]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nx, ny = i+dx, j+dy
                if 0<=nx<len(arr) and 0<=ny<len(arr[nx]):
                    if tmp[nx][ny]<tmp[i][j]:
                        amount = (tmp[i][j]-tmp[nx][ny])//5
                        arr[i][j]-=amount
                        arr[nx][ny]+=amount

N, K = map(int, input().split())
lst = list(map(int, input().split()))
time = 0
while True:
    if max(lst)-min(lst)<=K:
        break

    for i in range(N):
        if lst[i]==min(lst):
            lst[i]+=1

    time += 1
    roll = [lst[1:]]+[[lst[0]]]
    while len(roll)<=len(roll[0])-len(roll[1]):
        tail = roll[0][len(roll[1]):]
        head = list(map(list, zip(*roll)))[::-1]
        roll = [tail]+head

    spread(roll)

    tail = roll[0][len(roll[1]):]
    roll[0] = roll[0][:len(roll[1])]
    roll = list(map(list, zip(*roll)))
    lst = []
    for ele in roll:
        lst.extend(ele)
    lst.extend(tail)

    P1, P2, P3, P4 = lst[:N//4], lst[N//4:N//2], lst[N//2:3*N//4], lst[3*N//4:]
    roll = [P4, P1[::-1], P2, P3[::-1]]
    spread(roll)

    roll = list(map(list, zip(*roll)))
    lst = []
    for ele in roll:
        lst.extend(ele)

print(time)

'''
제출횟수 : 1회
풀이시간 : 50분

실행시간 : 104ms
메모리 : 110960 KB

[ 주의할 점 ]
* 어항 정리를 한번도 안할수도 있지 않을까?

[ 시간 복잡도 ]
시행횟수 10000번 이하
매 시행 당 첫번쨰 어항 쌓기 N^2, 나머진 N
100000000 의 상수배

[ 엣지 케이스 ] : 시작하자마자 끝나는 경우
8 7
5 4 4 14 9 4 11 8

구상 : 10분
* 아래로 쌓기로 결정
* spread 로직은 똑같으니까 그부분 함수화 해야지
* 시작하자마자 끝날수도있다는 것 주의하기
* 두번 뒤집기 규칙 미리 파악해둠

구현 : 37분
* 단계 하나 완성할 때 마다 arr 찍어보면서 진행


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
'''
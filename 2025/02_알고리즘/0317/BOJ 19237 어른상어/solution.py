'''
제출횟수 : 1회
풀이시간 : 55분

실행시간 : 140ms
메모리 : 112020KB

[오해 할 만한 것]
* 갈곳이 아예 없으면 어떡하지?
    -> 적어도 내가 온 칸에는 내 냄새가 뿌려져 있을 테니까 그럴 일은 없음
* 격자에서 쫓아낸다는 말이 무슨말이지? 한칸 더 간다는건가?
    -> 걍 삭제된다는 거였음

[ 시간 복잡도 ]
(상어수)*(적당한 상수)*1000
최대 400_000의 상수배

[ 엣지 케이스 ] : 한 번만에 끝나는 경우
3 4 3
0 1 0
2 0 3
0 4 0
2 4 3 1
1 2 3 4
2 1 3 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
4 1 2 3
1 2 3 4
1 2 3 4
3 1 2 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

구상 : 4분
* 문제 이해하고, 방향 우선순위, 상어 위치 관리법 결정, 문제 모호한 것들 파악하기
* 죽은 상어 그냥 없애버리는 걸로 처리하자
* 인덱스 순서대로 해서 상어 크기 조건문 안만들어도 되게 하자

구현 : 17분
* 죽인 상어 없애버리려면 뒤에서부터 처리해야겠네
* 인덱스 순서대로 해서 조건문 없애려면 크기가 작은애부터 해야겠네
--> 크기 역순으로 정렬하고 뒤에서부터 처리해야겠네

디버깅 : 34분
* 이동시키고 그 이동시킨 배열을 바탕으로 이동 우선순위를 정해서
* 상어들의 이동이 이상하게 이루어짐
    -> before 배열 만들어서 잘 가게 바꿈
'''
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = (0, (-1, 0), (1, 0), (0, -1), (0, 1))
sd = [0]+list(map(int, input().split()))
smell = [[(0, 0) for _ in range(N)] for _ in range(N)]
shark = []
for i in range(N):
    for j in range(N):
        if arr[i][j]!=0:
            # 상어의 번호와 좌표 저장
            shark.append([arr[i][j], i, j])
            # 지금 있는 칸에 냄새 뿌리기
            smell[i][j]=(arr[i][j], 0)

# 번호가 작은 상어부터 처리하기 위한 정렬
# 죽은 상어를 del할껀데 그러면 인덱스 오류가 안나야해서 뒤에서부터 처리
# 그래서 reverse로 정렬
shark.sort(reverse=True)

pdirection = [0]
for _ in range(M):
    # 각 상어의 방향별 우선순위 방향
    dir = [0]+[list(map(int, input().split())) for _ in range(4)]
    pdirection.append(dir)

time = 0
while time<1000:
    time += 1
    # 상어들의 냄새 상태 -> tuple로 저장해서 한단계만 깊게 복사하면 됨
    before = [ele[:] for ele in smell]
    # del 처리 햇을때 인덱스 안망가지게 뒤에서 부터 처리하면서
    for i in range(len(shark)-1, -1, -1):
        idx, x, y = shark[i]
        # 지금 자리 비워주고
        if arr[x][y]==idx:
            arr[x][y]=0

        mx, my = -1, -1
        # 우선순위대로 돌면서
        for d in pdirection[idx][sd[idx]]:
            dx, dy = dxdy[d]
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<N): continue
            # 빈칸이면 거기로 가고 break
            # 빈칸 여부는 냄새에 아무것도 안들어갔거나, 들어간 시간이 지금으로부터 K보다 더 전이면
            if before[nx][ny][0]==0 or (before[nx][ny]!=0 and before[nx][ny][1]<time-K):
                x, y, nd = nx, ny, d
                break
            # 돌면서 동시에 우선순위상 내 냄새가 뿌려진 칸을 저장해둠
            if before[nx][ny][0]==idx and mx==-1:
                mx, my, mnd = nx, ny, d
        # break 안됐으면 mx, my로 보내기
        else :
            x, y, nd = mx, my, mnd

        # 두 상어가 겹치는건 같은 시간 뿐
        # 그런데 상어 번호가 작은것부터 했으니까 무조건 내가 죽기
        if smell[x][y][1]==time:
            del shark[i]
            M-=1
        else :
            # 위치갱신, 냄새뿌리기, 방향갱신
            shark[i][1], shark[i][2] = x, y
            smell[x][y]=(idx, time)
            sd[idx]=nd
            arr[x][y]=idx
    # 상어가 한마리 이하로 남으면 끝내기
    if M<=1:
        print(time)
        break
# 1000초 안에 안끝났으면 -1출력
else:
    print(-1)
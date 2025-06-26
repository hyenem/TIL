'''
제출 횟수 : 1회
풀이시간 : 21분

실행시간 : 156ms
메모리 : 112060 KB

! 명심할 것 !
구하는 것을 잊고 있다가 중간에 길을 잃었다.
구하는 걸 내 마음대로 생각하고 있지 말 것

구상 : 2분
* 백트래킹 이용해야겠다는 생각
* 방문 표시를 원복하기 위한 stack을 사용해야겠다는 생각
* CCTV 방향을 번호대로 어떻게 결정해주지? 이것도 매번 조합을 돌려야하나?
* 아니 ! 몇 가지 없으니까 그냥 배열에 저장해서 뽑아쓰자

구현 : 15분
디버깅 : 4분
[1] CCTV 번호는 1부터 시작하는데, 0번 인덱스부터 넣어놔서 문제가 생김
    0번 인덱스에 빈배열 추가하여 수정
[2] 방향 결정할 때 ds를 direction[type]에서 꺼내야하는데 direction에서 꺼내서 문제 발생


[시간 복잡도]
4^(CCTV의 개수)*(M+N)
최대 대강 2^20,, 10^6 정도?

[엣지케이스]
[1] 죄다 CCTV인 경우
2 4
1 2 3 4
1 2 3 4

[2] 죄다 벽으로 둘러싸인 경우
3 3
0 6 0
6 5 6
0 6 0
'''

def solution(idx, cnt):
    global ans

    # 전체 cctv를 다 봤으면, 정답 갱신
    if idx==len(cctv):
        ans = min(ans, maxans-cnt)
        return

    type, x, y = cctv[idx]
    # CCTV 번호 별 볼 수 있는 방향들 중
    for ds in direction[type]:
        stack = []
        # 각 방향을 보면서 CCTV가 볼 수 있는 칸을 커버해줌
        for d in ds:
            nx, ny = x, y
            # 계속 해당 방향으로 나아가면서
            while True:
                nx, ny = nx+dxdy[d][0], ny+dxdy[d][1]

                # 범위를 벗어나거나 벽을 만나면 멈춤
                if not (0<=nx<N and 0<=ny<M): break
                if arr[nx][ny]==6: break

                # 이미 방문 했거나 cctv인 경우엔 그냥 지나가고
                # 그 외의 경우엔 방문 표시하고 stack에 보관함(btk을 위해)
                if arr[nx][ny]: continue
                arr[nx][ny]=-1
                stack.append((nx, ny))
        # 다음 CCTV로 넘어가기
        solution(idx+1, cnt+len(stack))

        # btk을 위해 방문 표시 원복하기
        while stack:
            nx, ny = stack.pop()
            arr[nx][ny]=0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 각 CCTV번호 별 볼 수 있는 방향을 저장
# 0: 상, 1: 우, 2: 하, 3: 좌
direction = [[], [(0,), (1,), (2,), (3,)], [(0, 2), (1, 3)], [(0, 1), (1,2), (2,3), (3,0)], [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1,2,3)], [(0,1,2,3)]]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

maxans = N*M
cctv = []
# 전체를 돌면서 cctv를 저장하고
# 벽도 아니고 cctv도 아닌 칸의 개수를 세기
for i in range(N):
    for j in range(M):
        if arr[i][j]==0: continue
        maxans -= 1
        if arr[i][j]!=6:
            cctv.append((arr[i][j], i, j))

ans = maxans
solution(0,0)
print(ans)
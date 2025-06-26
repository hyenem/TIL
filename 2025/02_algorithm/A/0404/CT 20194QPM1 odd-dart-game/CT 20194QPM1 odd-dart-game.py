'''2회독
제출횟수 : 2회
풀이시간 : 30분

* 문제를 제대로 안읽어서 고전,,,
    -> 문제 기억에 의존하지 말고 다시 읽을것!!!!
* 코드는 거의 똑같음
* 피드백 없음
'''

N, M, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
idx = [0]*N
cmds = [tuple(map(int, input().split())) for _ in range(Q)]

for x, d, k in cmds:
    for i in range(x-1, N, x):
        idx[i] = (idx[i]+(2*d-1)*k)%M

    visited = [[0]*M for _ in range(N)]
    flag = 1
    for i in range(N):
        for j in range(M):
            if visited[i][j]: continue
            if arr[i][j]==0: continue

            q = [(i, j)]
            qidx = 0
            visited[i][j]=1

            while qidx<len(q):
                x, y = q[qidx]
                qidx += 1
                nxny = [(x, (y-1)%M), (x, (y+1)%M)]
                if x!=0: nxny.append((x-1, (y-idx[x]+idx[x-1])%M))
                if x!=N-1: nxny.append((x+1, (y-idx[x]+idx[x+1])%M))

                for nx, ny in nxny:
                    if visited[nx][ny]: continue
                    if arr[x][y]==arr[nx][ny]:
                        visited[nx][ny]=1
                        q.append((nx, ny))

            if len(q)>1:
                flag = 0
                for x, y in q:
                    arr[x][y]=0
    if flag:
        summ = sum(map(sum, arr))
        cnt = N*M-sum([ele.count(0) for ele in arr])
        if summ==0: break

        avg = summ//cnt
        for i in range(N):
            for j in range(M):
                if arr[i][j]==0: continue
                if arr[i][j]>avg:
                    arr[i][j]-=1
                elif arr[i][j]<avg:
                    arr[i][j]+=1
print(sum(map(sum, arr)))

'''
제출횟수 : 3회
풀이시간 : 53분

실행시간 : 216ms -> 164ms
메모리 : 115932 KB -> 112040KB

!! 명심할 것 !!
오랜만에 마주한 division zero 주의

[빠트린 조건]
* k가 있다는 걸 잊고있었음

[오해한 조건]
>> 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
* 평균이 전체 원판의 평균이 아니라 원판 별 평균인 줄 알았음

구상 : 7분
* 원판 돌리는걸 덱으로 구현할까, 인덱스로 관리할까하다가 인덱스로 하기로함

구현 : 18분
* 구현 과정에서 방문 표시를 0으로 하기로 했던걸 'x'로 하기로 마음을 바꿈

디버깅 : 38분
[1] 평균을 원판별 평균으로 계산했다가 전체 평균 수정
[2] k를 반영
-> 제출 : 틀렸습니다
[3] 열 이동을 M이 아니라 4로 둔걸 발견(마지막 오픈 테케 있는지 모름)
-> 수정 후 제출 : zerodivision
[4] totcnt 가 0이 되는 순간 종료되도록함

리팩토링
[1]
원래는 방문 표시를 0으로 했다가
1에서 1이 빠져서 0이 되는 경우가 있을 것 같아서
'x'로 표시했는데,
평균이 1보다 작아질 수 없다는 사실을 깨닫고
다시 0으로 바꿈

[2]
q를 사용했는데 bfs를 할 필요는 없을 것 같아서
q라는 변수명은 쓰고 deque안쓰고 그냥 리스트로 관리함

[3]
바로 네 방향 보는 것 수정함
반복하지 않도록 처음 보면서 q에 넣도록 수정함

[4]
원래는 원판 별 평균인 줄 알고 원판별 ccnt를 들고다녔는데
전체 평균이라 전체 합이랑 전체 cnt를 들고 다니도록 바꿈

[시간복잡도]
T*N*M

[엣지케이스] : 처음부터 하나도 없었던 경우
4 6 1
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
2 0 1


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int,input().split())) for _ in range(T)]
dxdy = ((0, 1), (0, -1), (-1, 0), (1, 0))
totsum = sum([sum(ele) for ele in arr])
totcnt = M*N
idx = [0]*N
flag = 1

for x, d, k in move:

    # 회전하기
    for i in range(x-1, N, x):
        idx[i] = (idx[i]+(d*2-1)*k)%M

   # 인접한 같은 숫자 있는지 찾기
    flag = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0: continue

            q = []
            # 우선 시작점을 기준으로 네방향보기
            for dx, dy in dxdy:
                nx = i+dx
                if not(0<=nx<N): continue
                ny = (j-idx[i]+idx[nx]+dy)%M
                if arr[nx][ny]==0: continue
                if arr[nx][ny]==arr[i][j]:
                    q.append((arr[nx][ny], nx, ny))
                    totcnt -= 1
                    totsum -= arr[nx][ny]
                    arr[nx][ny] = 0
            # 네방향 중 같은게 하나라도 있으면
            # flag true, 시작점 업데이트하기
            if len(q)!=0:
                flag = 1
                totcnt -= 1
                totsum -= arr[i][j]
                arr[i][j] = 0
            # 같은 것 다 찾기
            # Q를 그냥 배열로 써서 사실 bfs는 아님
            while q:
                num, x, y = q.pop()
                for dx, dy in dxdy:
                    nx = x + dx
                    if not (0 <= nx < N): continue
                    ny = (y - idx[x] + idx[nx] + dy) % M
                    if arr[nx][ny] == num:
                        q.append((arr[nx][ny], nx, ny))
                        totcnt -= 1
                        totsum -= arr[nx][ny]
                        arr[nx][ny]=0

    # 숫자가 하나도 안남았으면 멈추기
    if totcnt==0 : break
    # 같은 칸 없앴으면 넘어가고
    # 아니면 숫자 바꾸기
    if flag: continue

    avg = totsum/totcnt
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0: continue
            if arr[i][j]>avg:
                arr[i][j]-=1
                totsum -= 1

            elif arr[i][j]<avg:
                arr[i][j] += 1
                totsum += 1

print(totsum)
'''
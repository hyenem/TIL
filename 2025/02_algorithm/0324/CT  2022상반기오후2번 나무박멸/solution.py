'''
제출횟수 : 2회
풀이시간 : 1시간 13분

실행시간 : 204ms
메모리 : 23MB

[ 명심할 것 ]
* 예제로 디버깅하고, 코드만 보고 디버깅도 하기

[ 엣지 케이스 ]
5 3 100 5
-1 0 0 0 0
0 30 23 0 0
0 0 -1 0 0
0 0 17 46 77
0 0 0 12 0

5 2 2 1
-1 0 -1 0 -1
0 -1 0 -1 0
-1 0 -1 0 -1
0 -1 0 -1 10
-1 0 -1 0 -1

구상 : 5분
구현 : 23분
디버깅 및 검증 : 45분
* 죽는 나무 개수 셀 때 1부터 K까지 해야하는데
    for문 돌 때 0부터 K+1까지 해서 디버깅을 오래함
* 자기위치 제초제 심기 인덱스를 ky가 아니라 ny로 설정해서 수정
* 틀렸습니다 1회
    -> 0인 경우 값 갱신 되도록 처리하다가 0일때도 제초제 대각선 다 가게 만들었음
    -> 수정하고 맞았습니다

'''

def grow():
    # 우,하만 보면서 나랑 쟤랑 다 1씩 더해주기
    for i in range(N):
        for j in range(N):
            if arr[i][j] in {0, -1}: continue
            for dx, dy in ((1, 0), (0, 1)):
                nx, ny = i+dx, j+dy
                if not(0<=nx<N and 0<=ny<N): continue
                if arr[nx][ny] in {0, -1}: continue
                arr[i][j]+=1
                arr[nx][ny]+=1

def spread():
    # 나무가 있는 곳 네방향 보면서
    # 나무가 없는 곳을 stack에 쌓아두고
    # 개수가 확정되면 arr에 업데이트하기

    tmp = [ele[:] for ele in arr]
    stack = []
    for i in range(N):
        for j in range(N):
            if tmp[i][j] in {0, -1}: continue
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nx, ny = i+dx, j+dy
                if not(0<=nx<N and 0<=ny<N): continue
                if invalid[nx][ny]>=time: continue
                if tmp[nx][ny]==0:
                    stack.append((nx, ny))
            if stack:
                amount = tmp[i][j]//len(stack)
                while stack:
                    x, y = stack.pop()
                    arr[x][y] += amount

def kill():
    kx, ky, kamount, klst = 0, 0, -1, []
    for i in range(N):
        for j in range(N):
            # 0인경우 다 걸러야한다고 생각해놓고,,, 특정 케이스만 거르기 심각,,,,,

            tmpamount = arr[i][j]
            tmplst = [(i, j)]
            # 나무가 있는 경우 대각선으로 뻗어나가기
            if arr[i][j] not in {0, -1}:
                for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                    for k in range(1, K + 1):
                        nx, ny = i + k * dx, j + k * dy
                        if not (0 <= nx < N and 0 <= ny < N): break
                        tmplst.append((nx, ny))
                        if arr[nx][ny] in {0, -1}: break
                        tmpamount += arr[nx][ny]
            # 최댓값 갱신
            if kamount < tmpamount:
                kx, ky, kamount, klst = i, j, tmpamount, tmplst

    if kamount <= 0:
        invalid[kx][ky] = time + C
        return 0

    # 나무들 죽이고 제초제 뿌리기
    for x, y in klst:
        if arr[x][y]!=-1: arr[x][y]=0
        invalid[x][y] = time+C

    return kamount



N, M, K, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
invalid = [[-1]*N for _ in range(N)]        # 제초제 지속시간 저장용

ans = 0
for time in range(M):
    grow()
    spread()
    ans += kill()
print(ans)

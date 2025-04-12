'''2회독
제출횟수 : 1회
풀이시간 : 11분

* 별다른 피드백 없음
'''

N = int(input())
arr = [[0]*N for _ in range(N)]
data = [list(map(int, input().split())) for _ in range(N*N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
dic = {}
for n, n1, n2, n3, n4 in data:
    like = {n1, n2, n3, n4}
    dic[n]=like

    x, y, cnt, ecnt = -1, -1, -1, -1
    for i in range(N):
        for j in range(N):
            if arr[i][j]: continue
            tmpcnt, tmpecnt= 0, 0
            for dx, dy in dxdy:
                nx, ny= i+dx, j+dy
                if not(0<=nx<N and 0<=ny<N): continue
                if arr[nx][ny] in like:
                    tmpcnt+=1
                elif arr[nx][ny]==0:
                    tmpecnt += 1

            if cnt<tmpcnt:
                cnt = tmpcnt
                ecnt = tmpecnt
                x, y = i, j
            elif cnt==tmpcnt and ecnt<tmpecnt:
                ecnt = tmpecnt
                x, y = i, j

    arr[x][y]=n

ans = 0
for i in range(N):
    for j in range(N):

        cnt = 0
        like = dic[arr[i][j]]
        for dx, dy in dxdy:
            nx, ny = i+dx, j+dy
            if not(0<=nx<N and 0<=ny<N): continue
            if arr[nx][ny] in like:
                cnt += 1

        ans += int(10**(cnt-1))

print(ans)

'''
제출횟수 : 2회
풀이시간 : 18분

실행시간 : 164ms
메모리 : 112156KB

! 명심할 것 !
* nx, ny 쓸 때 무지성 x+dx, y+dy하지 말것
* i+dx, j+dy인 경우도 있음
* 초기 조건 설정 잘할것

구상 : 3분
* 매 숫자를 넣을 때 마다 이중 포문 돌면서 주변의 빈칸과 좋아하는 학생 수 세기
* 시간복잡도 : O(N**3) N이 최대 20이므로 가능

구현 : 9분
디버깅 : 3분
* i,j좌표에서 nx, ny 만들어야하는데, x, y 중심으로 만들어서 수정
* x, y, like, empty 를 전부 0으로 잡고 시작해서 문제가 발생
* 아래와 같은 반례가 발생가능
* 그래서 전부다 -1로 두도록 수정함

반례
3
4 2 5 1 7
3 1 9 4 5
9 8 1 2 3
8 1 9 3 4
7 2 3 4 8
1 9 2 5 7
6 5 2 3 4
5 1 9 2 8
2 9 5 1 4
정답 : 53


N = int(input())
dxdy = ((0,1),  (0, -1), (1, 0), (-1, 0))
arr = [[0]*N for _ in range(N)]
# n번 학생의 좋아하는 사람을 저장할 배열(마지막 점수 계산용)
lst = [[] for _ in range(N*N+1)]
for _ in range(N*N):
    num, *surround = map(int, input().split())
    lst[num]=surround
    #이걸 처음에 0, 0으로 했다가 오류가 생김(마지막 숫자 넣을 때)
    x, y = -1, -1
    # 인접하는 좋아하는 사람과 빈칸의 최대를 저장
    like = -1
    empty = -1
    for i in range(N):
        for j in range(N):
            # 이미 숫자가 들어가있으면 continue
            if arr[i][j]!=0:continue
            tmplike = 0
            tmpempty = 0
            for dx, dy in dxdy:
                nx, ny = i+dx, j+dy
                if not(0<=nx<N and 0<=ny<N): continue
                #네 방향에 대해서 좋아하는 사람 수, 빈칸 수 세기
                if arr[nx][ny] in surround:
                    tmplike += 1
                elif arr[nx][ny]==0:
                    tmpempty += 1

            # 아직 좌표가 한번도 업데이트 안되었거나,
            # 좋아하는 사람 수가 기존 것 보다 많아지면 좌표 업데이트
            if like<tmplike:
                like = tmplike
                empty = tmpempty
                x, y = i, j
            # 좋아하는 사람의 수는 같은데 빈칸이 더 많으면 좌표 업데이트
            elif like ==tmplike and empty<tmpempty:
                empty = tmpempty
                x, y = i, j
    # 그 자리에 그 숫자 넣기
    arr[x][y]=num

ans=0
# 모든 점에 대해서 사방돌면서 좋아하는 사람 수 세서 답에 더해주기
for i in range(N):
    for j in range(N):
        cnt = 0
        surround = lst[arr[i][j]]
        for dx, dy in dxdy:
            nx, ny = i + dx, j + dy
            if not (0 <= nx < N and 0 <= ny < N): continue
            if arr[nx][ny] in surround:
                cnt += 1
        ans += int(10**(cnt-1))

print(ans)

'''
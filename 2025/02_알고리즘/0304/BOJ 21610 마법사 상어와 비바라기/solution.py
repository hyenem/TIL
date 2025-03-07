'''
제출횟수 : 2회
풀이시간 : 23분

실행시간 : 152ms
메모리 : 112060KB

! 명심할 것 !
사이즈 작다고 시간 복잡도를 무시하지 말것!
구현이라고 최적화를 너무 던져버리지 말 것
이 문제의 경우 첫 코드에선 시간복잡도 50^4 이었음

구상 : 2분
빡 구현이므로 별 고민없이 문제에서 주어진 순서대로 구현 시작
다만 구름이 모두 사라진다에서 이전 구름의 정보를 다 지워버리면
복사 버그 좌표를 찾기가 어려우므로 구름 정보는 유지

구현 : 9분
디버깅1 : 3분
* ** 물의 양이 2 줄어든다. ** 이 부분을 간과함
* 해당 내용 추가

* 시간초과
디버깅 2: 6분
* 이중 for문 안에서 [i, j] in cloud 해서
* 리스트에서 리스트 찾기. 즉 n^4 으로 돌아가고 있었음
* visited 배열 만들어서 n^2 안에서 해결할 수 있도록 수정
'''

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

# 초기 구름 생성
cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
command = [list(map(int, input().split())) for _ in range(K)]

for d, s in command:
    d = d-1

    # 구름 이동
    for i in range(len(cloud)):
        cloud[i][0]=(cloud[i][0]+s*dxdy[d][0])%N
        cloud[i][1]=(cloud[i][1]+s*dxdy[d][1])%N

    # 비내리기
    for x, y in cloud:
        arr[x][y]+=1

    # 물 복사 버그
    visited = [[0]*N for _ in range(N)]
    for x, y in cloud:
        visited[x][y]=1
        for i in range(4):
            dx, dy = dxdy[2*i+1]
            nx, ny = x+dx, y+ dy
            if not (0<=nx<N and 0<=ny<N): continue
            if arr[nx][ny]>0:
                arr[x][y]+=1

    # 다음 구름 생성
    ncloud = []
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            if arr[i][j]>=2:
                ncloud.append([i,j])
                arr[i][j]-=2

    cloud = ncloud


ans = sum(map(sum, arr))
print(ans)
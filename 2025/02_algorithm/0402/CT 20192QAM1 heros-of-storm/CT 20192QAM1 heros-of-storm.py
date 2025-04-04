'''2회독
제출횟수 : 1회
풀이시간 : 11분

* 1회독 : 틀렸습니다 1회 ( 공청기 가동 아랫부분 인덱스 잘못 지정 )
* 혜민이 다컸다 미세먼지 안녕을 인덱스 한번을 안틀리고 맞았구나

'''

def spread():
    tmp = [ele[:] for ele in arr]
    for i in range(N):
        for j in range(M):
            if tmp[i][j] in {0, -1}: continue
            for dx, dy in dxdy:
                nx, ny = i+dx, j+dy
                if not(0<=nx<N and 0<=ny<M): continue
                if arr[nx][ny]==-1: continue
                arr[nx][ny]+=tmp[i][j]//5
                arr[i][j]-=tmp[i][j]//5

def clean():
    for i in range(wind_u-1, 0, -1):
        arr[i][0]=arr[i-1][0]
    for j in range(M-1):
        arr[0][j] = arr[0][j+1]
    for i in range(wind_u):
        arr[i][M-1]=arr[i+1][M-1]
    for j in range(M-1, 1, -1):
        arr[wind_u][j]=arr[wind_u][j-1]
    arr[wind_u][1]=0

    for i in range(wind_d+1, N-1):
        arr[i][0]=arr[i+1][0]
    for j in range(M-1):
        arr[N-1][j]=arr[N-1][j+1]
    for i in range(N-1, wind_d, -1):
        arr[i][M-1]=arr[i-1][M-1]
    for j in range(M-1, 1, -1):
        arr[wind_d][j]=arr[wind_d][j-1]
    arr[wind_d][1]=0


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
for i in range(N):
    if arr[i][0]==-1:
        wind_u = i
        wind_d = i+1
        break

for _ in range(T):
    spread()
    clean()

ans = 2 + sum(map(sum, arr))
print(ans)

'''
제출횟수 : 2회
풀이시간 : 61분

실행시간 : 136ms
메모리 : 111796KB
코드길이 : 1307B

구상시간 : 3분
* 단순 구현 + 이전에 풀었던 기억이 나서 바로 코드 작성 시작
첫번쨰 제출 : 30분
* 아랫 방향 도는 cleand의 아래에서 위로 올라가는 방향을 잘못 작성
* 계속 사이즈가 작은 테스트 케이스를 넣어봐서 오류를 발견하지 못함
* 공기청정기 아래로 세칸 이상 있으면 무조건 틀리는 코드였음
두번쨰 제출 : 61분

# 고전한 이유
1. 미세먼지가 돌아가는 방향을 착각함(시계반시계)
2. 미세먼지 돌아가는 코드를 잘못 작성

* 명심할 것
1. 사이즈카 큰 테스트케이스를 만들어보기 힘들어도 꼭 하나 만들어볼 것
2. 처음에 틀릴 위험 높겠다고 생각한건 꼭 재점검 필수(아예 새로운 마음가짐으로 볼 것)


# 확산
def spread():
    # 원래칸의 먼지 수를 기준으로 확산해야하므로 기존 먼지 양을 임시 배열에 저장
    tmp = [ele[:] for ele in arr]
    for i in range(N):
        for j in range(M):
            # 공기 청정기가 있는 칸에서는 확산 일어나지 않음
            if arr[i][j]==-1: continue
            for dx, dy in dxdy:
                nx, ny = i+dx, j+dy
                # 바깥으로 나가는 경우, 공기청정기인 경우 제외하고 확산
                if not(0<=nx<N and 0<=ny<M): continue
                if arr[nx][ny]==-1: continue
                arr[nx][ny]+=tmp[i][j]//5
                arr[i][j]-=tmp[i][j]//5

# 위쪽 순환
def cleanu():
    for i in range(windu-1, 0, -1):
        arr[i][0]=arr[i-1][0]
    for j in range(0, M-1):
        arr[0][j]=arr[0][j+1]
    for i in range(0, windu):
        arr[i][M-1]=arr[i+1][M-1]
    for j in range(M-1, 1, -1):
        arr[windu][j]=arr[windu][j-1]
    arr[windu][1]=0

# 아래쪽 순환
def cleand():
    for i in range(windd+1, N-1):
        arr[i][0]=arr[i+1][0]
    for j in range(0, M-1):
        arr[N-1][j]=arr[N-1][j+1]
    for i in range(N-1, windd, -1):
        arr[i][M-1]=arr[i-1][M-1]
    for j in range(M-1, 1, -1):
        arr[windd][j]=arr[windd][j-1]
    arr[windd][1]=0

dxdy = ((0,1), (0,-1), (1, 0), (-1, 0))
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 공기청정기의 행 저장
for i in range(N):
    if arr[i][0]==-1:
        windu = i
        windd = i+1
        break

# T초동안 시행
for t in range(T):
    spread()
    cleanu()
    cleand()

# 전체 합에서 공기청정기때문에 빠진 2 제외하고 더해주기
print(sum([sum(ele) for ele in arr])+2)
'''
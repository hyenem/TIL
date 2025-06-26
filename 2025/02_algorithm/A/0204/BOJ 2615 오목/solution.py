# 제출 횟수 : 4회
# 풀이시간 : 40분
# 실행시간 : 92ms
# 메모리 : 109544 KB

# Review
# 인덱스 채크 잘 할것
# 문제 꼼꼼히 읽을 것
# 연속된 돌이 최대 6개인 줄 착각함

# 현재의 좌표와 검사하고 있는 방향, 검사중인 돌의 색, 그리고 누적된 오목의 개수
def dfs(x, y, direction, color, cnt):
    nx = x+dx[direction]
    ny = y+dy[direction]
    # 오목이면 육목인지 확인하고
    if cnt == 5:
        # 육목이 아니면
        if not(0<=nx<19 and 0<=ny<19) or arr[nx][ny]!=color:
            print(color)
            # 좌하향인경우 자신 출력
            if direction==3:
                print(x+1, y+1)
            # 나머지 경우엔 출발점 찾아서 출력
            else:
                print(x-4*dx[direction]+1, y-4*dy[direction]+1)
            # 결과 나왔다고 리턴
            return True
        # 육목이니까 결판 아직 안남
        # 가면서 방문처리만
        visited[nx][ny][direction]=True
        return dfs(nx, ny, direction, color, cnt+1)
    # 아직 5가 쌓이기 전에는
    # 다음칸이 이어지면
    if 0<=nx<19 and 0<=ny<19 and arr[nx][ny]==color:
        # 방문표시하고
        visited[nx][ny][direction]=True
        # 다음칸에 한칸 늘려서 dfs
        return dfs(nx, ny, direction, color, cnt+1)
    # 다음칸이 이어지지 않으면
    # 이번판에 결판 안남
    return False

# 중첩반복문 종료를 위한 함수
def solution():
    for i in range(19):
        for j in range(19):
            if arr[i][j] != 0:
                for k in range(4):
                    # 이미 방문했으면 검사하지 않음
                    if visited[i][j][k]:
                        continue
                    nx = i + dx[k]
                    ny = j + dy[k]
                    #범위 채크
                    if not(0<=nx<19 and 0<=ny<19):
                        continue
                    # 연결되어있으면, 연결된 두개 방문표시하고,
                    # 주번째 좌표, 방향, 색, 두개 누적 담아서
                    # dfs 진행
                    if arr[nx][ny] == arr[i][j]:
                        visited[i][j][k] = True
                        visited[nx][ny][k] = True
                        flag = dfs(nx, ny, k, arr[i][j], 2)
                        # 이미 결판 났으면 멈추기
                        if flag:
                            return
    print(0)


# 가로, 세로, 우하향, 좌하향
dx = (0, 1, 1, 1)
dy = (1, 0, 1, -1)

arr = [list(map(int, input().split())) for _ in range(19)]
# 네가지 방향에 대한 채크여부 방문 표시
visited = [[[False] * 4 for _ in range(19)] for _ in range(19)]
solution()

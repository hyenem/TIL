'''
제출횟수 : 1회
풀이시간 : 1시간 10분

실행시간 : 128 ms
메모리 : 111416 KB

[ 헷갈릴 만한 것 ]
* 상어 칸에 물고기가 복제돼서 생겼을 때 먹고 넘어가나? -> 아니요!(테케에 나옴)
* 상어는 왔던 곳을 다시 갈 수 있나? -> 네!
* 물고기의 냄새는 그 칸에 물고기가 여러마리일 때 누적이 된다거나 그런가? -> 아니요!

[ 고전 한 것 ]
-> 격자 위에 있는 물고기의 수가 항상 1,000,000 이하인 입력만 주어진다.
* 이 조건보고 그냥 물고기 한마리한마리 다 보고 다 옮겨도 시간 안터지겠거니 했는데
* 한마리한마리 옮기는게 아니라 위치, 방향 같은 애들 개수로 저장해서 동시에 옮기는게 더 빠를 것이라고 생각
* 알단 물고기 하나하나 옮기는걸로 짰는데 계속 찜찜,,, 한 마음이 들어서,,,,,,
* 그냥 짜고싶은 대로 짜
* 괜히 중간에 뭐 안되면 그냥 처음 생각한 코드로 짤껄하고 어차피 회귀

[ 시간복잡도 ]
S 번동안 물고기 옮기기, 상어 옮기기, 배열 복사
(4*4*8 + 4*4*4 + 4*4*8)*S의 상수배
시간 아무 걱정 없음

[ 엣지 케이스 ] : 상어가 있는 칸에 물고기가 복제되는 경우
1 2
2 2 2
4 2
정답 : 2
오답 : 1

구상 : 8분
* 예제 보면서 어떻게 돌아가는지 파악
* 복제를 한다는 개념을 그냥 이번턴에 새로운 배열로 관리하고, 이전거에 더해가기로함
* 물고기 수 보고 fish 리스트와 newfish 리스트로 관리하면 되겠다고 생각함
* 그런데 3차원 배열 만들어서 물고기 수로 관리하는게 더 유리하다고 생각함
* 상어는 백트레킹으로 갈지 bfs로 갈지 고민 -> 백트래킹으로 가기로함

구현 : 26분
디버깅 : 36분
[1] 상어가 가는 길에 물고기가 없는 곳이어도 냄새를 뿌려서 수정
[2] 원래 nfish의 인덱스를 저장해두고 삭제하게 만들었는데, 실제로 삭제하니까 인덱스 깨져서 삭제 안된애들만 옮기기함
[3] 8방탐색에서 탐색 방향 안바꿔줌 ㅋㅅㅋ
[4] 뭔가 답이 안나오는데 디버깅이 안돼서 그냥 처음 생각했던 아이디어(더 효율적)로 수정
    -> 맞았습니다.

'''

def smove(nsx, nsy, acc):
    global racc, root

    # 3칸 다 이동했으면, 먹은 물고기 개수 보고,
    # 이번에 더 많이 먹었으면, 먹는 물고기수랑 갈 길 다 갱신
    # 우선순위를 위해서 <= 가 아니라 <로 처리
    if len(tmproot)==3:
        if racc<acc:
            racc = acc
            root = tmproot[:]
        return

    # 네 방향 다 보면서 백트래킹
    for d in range(4):
        dx, dy = sdxdy[d]
        nnsx, nnsy = nsx+dx, nsy+dy
        if not(0<=nnsx<4 and 0<=nnsy<4): continue

        tmp = nfish[nnsx][nnsy]
        nfish[nnsx][nnsy] = [0]*8         # 이 길 다시 오면 물고기 없어져야함
        tmproot.append((nnsx, nnsy))

        smove(nnsx, nnsy, acc+sum(tmp))

        nfish[nnsx][nnsy] = tmp
        tmproot.pop()                   # 백트래킹을 위한 원복

M, S = map(int, input().split())
fish = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
sdxdy = ((-1, 0), (0, -1), (1, 0), (0, 1))                                      # 상어 움직임
fdxdy = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))  # 물고기 움직임
smell = [[0]*4 for _ in range(4)]                                               # 냄새가 끝나는 시간
sx, sy = map(lambda x: int(x)-1, input().split())
arr = [[[0]*8 for _ in range(4)] for _ in range(4)]                             # 좌표의 각 뱡향을 보고있는 물고기 수
for fx, fy, fd in fish:
    arr[fx][fy][fd]+=1

time = 0
for _ in range(S):
    time += 1

    # 복제하는 로직을 그냥 이번에 움직인 배열을 이용해서 처리하고,
    # 이 배열을 마지막에 원래 배열로 더해주는 스타일로
    nfish = [[[0]*8 for _ in range(4)] for _ in range(4)]


    # 전체를 다 보면서
    for fx in range(4):
        for fy in range(4):
            for fd in range(8):
                if arr[fx][fy][fd]==0: continue     # 물고기가 없으면 건너뛰기

                nfd = fd
                for _ in range(8):
                    dx, dy = fdxdy[nfd]
                    nx, ny = fx + dx, fy + dy
                    # 갈 수 있는 칸인지 채크하고 물고기 옮기기, 못가면 반시계방향으로 돌기
                    if 0 <= nx < 4 and 0 <= ny < 4 and smell[nx][ny] < time and (sx, sy) != (nx, ny):
                        nfish[nx][ny][nfd] += arr[fx][fy][fd]
                        break
                    nfd = (nfd - 1) % 8
                else:
                    # 아예 못가면 그자리에 그대로 있기
                    nfish[fx][fy][fd]+=arr[fx][fy][fd]


    tmproot = []        # 백트래킹용
    racc = -1           # 최대 잡아먹을 수 있는 물고기
    root = []           # 실제로 상어가 지나갈 길
    smove(sx, sy, 0)    # 상어 움직이기



    sx, sy = root[-1]       # 상어 좌표 이동
    while root:
        dfx, dfy = root.pop()
        # 길에서 물고기가 하나라도 있었으면, 냄새 남기고, 물고기 지우기
        if sum(nfish[dfx][dfy])==0: continue
        nfish[dfx][dfy]=[0]*8
        smell[dfx][dfy] = time+2


    # 복제하기 -> 기존 배열에 이번에 이동한 물고기들 더해주기
    for i in range(4):
        for j in range(4):
            for d in range(8):
                arr[i][j][d]+= nfish[i][j][d]

ans = 0
for i in range(4):
    for j in range(4):
        ans += sum(arr[i][j])
print(ans)
'''2회독
제출횟수 : 1회
풀이시간 : 20분

* 룩업테이블을 잘ㄹ 쓰게되었다
* 상황에 따라 패딩두를 수 있다는 것 잘 이용했다
* 별다른 피드백 없음
'''

N, K = map(int, input().split())
dxdy =((0,1), (0, -1), (-1, 0), (1, 0))
reverse_d = (1, 0, 3, 2)
arr = [[2]*(N+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(N)]+[[2]*(N+2)]
harr = [[[] for _ in range(N+2)] for _ in range(N+2)]
hlst = []
for i in range(K):
    x, y, d = map(int, input().split())
    hlst.append((x, y, d-1))
    harr[x][y].append(i)

ans = -1
for turn in range(1, 1001):

    for i in range(K):
        x, y, d = hlst[i]
        for idx in range(len(harr[x][y])):
            if harr[x][y][idx]==i:
                movelst = harr[x][y][idx:]
                harr[x][y]=harr[x][y][:idx]
                break

        dx, dy = dxdy[d]
        nx, ny = x+dx, y+dy
        if arr[nx][ny]==2:
            d = reverse_d[d]
            hlst[i]=(x, y, d)
            dx, dy = dxdy[d]
            nx, ny = x + dx, y + dy

        if arr[nx][ny]==0:
            for ni in movelst:
                hd = hlst[ni][2]
                hlst[ni] = (nx, ny, hd)
            harr[nx][ny]+=movelst
        elif arr[nx][ny]==1:
            for ni in movelst:
                hd = hlst[ni][2]
                hlst[ni] = (nx, ny, hd)
            harr[nx][ny]+=movelst[::-1]
        else:
            nx, ny = x, y
            harr[x][y]+=movelst

        if len(harr[nx][ny])>=4:
            ans = turn
            break
    if ans!=-1:
        break
print(ans)

'''
제출횟수 : 1회
풀이시간 : 43분

실행시간 : 140ms
메모리 : 112564KB

!! 명심할 것 !!
문제 완벽히 이해될 때 까지 꼼꼼히 읽기

[오해할만한 것]
* 파랑을 만나면 나보다 위에있는 것들 방향을 다 바꾸는건가?
* 처음엔 파랑을 만나면 뒤로 돌기만 하는 줄 알았음
[시간 복잡도]
최악의 경우 1000*K^2 정도?
[엣지 케이스]: 죄다 파랑으로 막혀있는 경우
4 6
0 2 2 0
2 0 2 2
2 2 2 0
0 2 0 2
1 1 1
1 3 2
2 2 3
3 4 4
4 1 1
4 3 2

구상 : 5분
* 말의 층수를 어떻게 다루지?
* N^2 순회 안하려면 정보를 어떻게 관리해야하지?
-> 말의 좌표와 방향을 하나의 lst로 관리하고
-> 말의 층수를 알 수 있게 N^2 짜리 배열에 말의 인덱스를 쌓자
-> 어차피 4층보다 작을테니까 말 층수 순회정도는 괜찮을 듯

구현 : 21분
* 원래는 loc에 인덱스 + 방향을 같이 관리하려했는데, 그럴 필요가 없다는걸 깨닫고 수정

디버깅 : 17분
[1] 빨강간으로 이동하고 이동한 아이들 남아있어서 수정
[2] 파랑칸 만나면 뒤로 돌기만 하고 끝냈었는데,
    다 잘 움직이는데 답이 안나와서 문제 다시 읽어보고
    파랑과 oob 주어진대로 정확하게 다시 구현
[3] 디버깅 과정에서 정답 출력이 너무 많이 돼서 인덴트를 바꿨는데
    그게 인덴트를 바꿀게 아니라 위치는 거기가 맞고, 반복문을 두번 끝내줬어야하는 거였음
    opentc에 걸려서 해당 부분 수정


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
horse = [list(map(int, input().split())) for _ in range(K)]
loc = [[[] for _ in range(N)] for _ in range(N)]
dxdy = ((0, 1), (0, -1), (-1, 0), (1, 0))

# horse에는 각 인덱스 별 말의 정보를 저장하고
# loc에는 어떤 칸에 몇번 인덱스 말이 있는지를 저장
for i in range(K):
    x, y, d = horse[i][0], horse[i][1], horse[i][2]
    horse[i] = [x-1, y-1, d-1]
    loc[x-1][y-1].append(i)

flag = 0
for ans in range(1, 1000):
    for i in range(K):
        x, y, d = horse[i]
        dx, dy = dxdy[d][0], dxdy[d][1]
        nx, ny = x+dx, y+dy


        # 다음 칸이 판을 벗어나거나 파랑칸이면
        if not(0<=nx<N and 0<=ny<N) or arr[nx][ny]==2:
            if d<2: nd = 1-d
            else : nd = 5-d
            horse[i][2] = nd
            d = nd
            dx, dy = dxdy[d][0], dxdy[d][1]
            nx, ny = x + dx, y + dy

        # 방향 바꿨는데도 범위 벗어나거나 파란칸이면 변화없음
        if not (0 <= nx < N and 0 <= ny < N) or arr[nx][ny] == 2:
            continue


        # 하양칸이면 나보다 위에 있는 애들 다같이 이동
        if arr[nx][ny]==0:
            for j in range(len(loc[x][y])):
                # 해당 칸에 나를 만난 순간
                if loc[x][y][j]==i:
                    # 나보다 위에 있는 애들에 대해서
                    # 다음 칸으로 이동하기
                    for k in range(j, len(loc[x][y])):
                        ni = loc[x][y][k]
                        horse[ni][0], horse[ni][1]=nx, ny
                        loc[nx][ny].append(ni)
                    # 이동한 애들 다 삭제하기
                    del loc[x][y][j:]
                    break

        # 빨간 칸을 만나면 뒤에서부터 다음 칸으로 옮기고
        elif arr[nx][ny]==1:
            while loc[x][y]:
                ni = loc[x][y].pop()
                horse[ni][0], horse[ni][1] = nx, ny
                loc[nx][ny].append(ni)
                # 나를 만나면 멈추기
                if ni==i: break


        # 4개가 되는 순간 끝내기
        if len(loc[horse[i][0]][horse[i][1]])>=4:
            print(ans)
            flag =1
            break
    if flag:
        break


# 한번도 출력이 안되었으면 -1 출력하기
else :
    print(-1)
'''
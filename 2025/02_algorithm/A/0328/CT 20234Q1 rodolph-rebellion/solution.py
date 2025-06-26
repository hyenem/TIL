'''
제출횟수 : 1회
풀이시간 : 2시간 35분

[ 오해한 것 ]
어이가 아리마셍입니다!?!?!?;;;;;;;;;;;;;;;
다아아아아앙연히 택시 거리라고 생각하고!?!?!?!!??!?!?!?
열심히 코드를 짰는데요?!?!?
예제가 이상하게 움직이길래?1??!
엥!?!?!?!? 선배들이 이 문제 이상하다고 했는데?!?! 그러면 혹시 얘네 8방다 한칸으로 세나!??!
하고 수정했는데
또 예제랑 다르게 움직이는거에요!?1??!
그래서 산타만 8방 한칸으로 치나?@?!?!!??!?!!!!?!????  하고 짜보고
다음엔 루돌프만 8방 한칸으로 치나?!?!?!?!?!?!?!?!?!?? 하고 짜봤는데요1?!?!?
뭐 어쨰저쨰하다가 테케가 다 맞아서 제출 전에 마지막으로 문제를 한 번 더 읽었는데요1!??!?!?!?!?!?
거리가 제곱 더하기 제곱인거죠?!?!!??!?!?!
이건 수학전공자로서 대 수치이고? 나가죽어야합니다!!?!?!?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


구상 : 12분
* 이차원에 산타 위치 관리해야겠다(산타 이동할때도 산타있으면 못가는 거 처리, 밀릴 때도 인덱스로 처리)
* 죽은 산타 배열 따로 관리해야지
* BFS를 돌 필요가 없는 문제네

구현 : 50분
* 모듈별로 검증하면서 진행

디버깅 및 검증 : 93분
* 별로 디버깅 한 것도 없습니다
* 계속 삽질하다가 마지막 5분에 수정하고 제출,,,

[ 엣지 케이스 ]
5 3 4 2 2
1 1
1 3 3
4 2 2
2 4 4
3 5 5
-> 연쇄 잘 되나?


3 3 1 2 2
1 1
1 2 2
-> 종료조건 잘 되나?
'''

def rodolph_move():
    global rx, ry, cnt

    selected_santa = (2*N**2+1, -1, -1)
    for i,(x, y) in enumerate(santa):
        if die[i]: continue
        selected_santa = min(selected_santa, (abs(x-rx)**2+abs(y-ry)**2, -x, -y))

    sx, sy = -selected_santa[1], -selected_santa[2]

    dx, dy = 0, 0
    if sx>rx: dx=1
    elif sx<rx: dx=-1

    if sy>ry: dy=1
    elif sy<ry: dy=-1

    rx, ry = rx+dx, ry+dy

    if santa_exist[rx][ry]!=-1:
        sidx = santa_exist[rx][ry]
        santa_exist[rx][ry]=-1

        ans[sidx]+=C
        stun[sidx]=turn+1
        nsx, nsy = rx+C*dx, ry+C*dy
        while True:
            if not(0<=nsx<N and 0<=nsy<N):
                cnt+=1
                die[sidx]=1
                santa[sidx]=(-1, -1)

                if cnt==P: return 1
                break

            if santa_exist[nsx][nsy]==-1:
                santa_exist[nsx][nsy]=sidx
                santa[sidx] = (nsx, nsy)
                break

            santa[sidx]=(nsx, nsy)
            sidx, santa_exist[nsx][nsy] = santa_exist[nsx][nsy], sidx
            nsx, nsy = nsx+dx, nsy+dy
    return 0

def santa_move():
    global cnt
    for i in range(P):
        if die[i] or stun[i]>=turn: continue

        sx, sy = santa[i]
        santa_exist[sx][sy]=-1

        nsx, nsy = sx, sy
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nnsx, nnsy = sx+dx, sy+dy
            if not (0<=nnsx<N and 0<=nnsy<N): continue
            if santa_exist[nnsx][nnsy]!=-1 : continue
            if abs(nsx-rx)**2+abs(nsy-ry)**2 > abs(nnsx-rx)**2+abs(nnsy-ry)**2:
                nsx, nsy = nnsx, nnsy
                rdx, rdy = dx, dy
        sx, sy = nsx, nsy
        santa_exist[sx][sy]=i
        santa[i]=(sx, sy)
        if (rx, ry)!=santa[i]: continue

        sidx = i
        santa_exist[rx][ry] = -1

        ans[sidx] += D
        stun[sidx] = turn + 1
        nsx, nsy = rx - D * rdx, ry - D * rdy
        while True:
            if not (0 <= nsx < N and 0 <= nsy < N):
                cnt+=1
                die[sidx] = 1
                santa[sidx]=(-1, -1)
                if cnt==P:
                    return 1
                break

            if santa_exist[nsx][nsy] == -1:
                santa_exist[nsx][nsy] = sidx
                santa[sidx] = (nsx, nsy)
                break

            santa[sidx] = (nsx, nsy)
            sidx, santa_exist[nsx][nsy] = santa_exist[nsx][nsy], sidx
            nsx, nsy = nsx - rdx, nsy - rdy
    return 0



N, M, P, C, D = map(int, input().split())
rx, ry = map(lambda x:int(x)-1, input().split())
santa_data = [list(map(lambda x:int(x)-1, input().split())) for _ in range(P)]
santa = [0]*P

santa_exist = [[-1]*N for _ in range(N)]
for idx, x, y in santa_data:
    santa[idx]=(x, y)
    santa_exist[x][y]=idx

die = [0]*P
ans = [0]*P
stun = [-1]*P

cnt = 0
for turn in range(1, M+1):
    end = rodolph_move()
    if end: break

    end = santa_move()
    if end: break

    for i in range(P):
        if die[i]: continue
        ans[i]+=1

print(*ans)

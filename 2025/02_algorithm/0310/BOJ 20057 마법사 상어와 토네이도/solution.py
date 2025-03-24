'''
제출횟수 : 1회
풀이시간 : 31분

메모리 : 113560KB
실행시간 : 264ms

구상 : 5분
* 모래 퍼지는 것 방향처리 어떻게 해줄까 고민함
* 내가 가던 방향에서 상대적으로 어떻게 이동해야하나 기록해두기로함

구현 : 17분

디버깅 : 9분
* 디버거로 먼지가 잘 퍼져나가는 지 봄
* 100인 겅우를 보면 잘 퍼졌는지 확인할 수 있을 것 같아서 봤는데
* 2%가 영 이상함

* 방향 설정을 잘못해둬서 문제가 생김
* dic을 수정함

[시간복잡도]
대강 N^2의 상수배

[엣지케이스] : N이 3인 경우 인덱스 에러 안나는지
3
0 0 0
100 0 0
0 0 0

'''

# 내가 가던 방향에서 오른쪽으로 얼만큼 회전한만큼 더 가면 비율이 어떠한지
dic = {(0,0): 5, (0,1):10, (0, -1): 10, (1, 1): 2, (1,): 7, (-1,): 7, (-1, -1): 2, (2, -1): 1, (2, 1): 1}
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
x, y = N//2, N//2

dxdy = ((0, -1), (1, 0), (0, 1), (-1, 0))
d = -1
ans = 0
end = 0
# 1, 1, 2, 2, 3, 3, 이렇게 전진
# 해당 방향으로 전진하는 칸의 수
for repeat in range(1, N+1):
    # 같은 숫자만큼 두번씩 감
    for _ in range(2):
        # 반시계 방향으로 회전
        d = (d+1)%4
        # 그 방향으로 가야하는 만큼 쭉 감
        for _ in range(repeat):
            x, y = x+dxdy[d][0], y+dxdy[d][1]
            # 마지막에 알파값을 결정해주기 위해서
            alpha = arr[x][y]

            # 지금 가던 방향에서 어떻게 더 갔을때 그 칸의 비율이 어떠한지
            for root, ratio in dic.items():
                # 이 길로 갔을 때 그 칸의 양
                amount = (arr[x][y]*ratio)//100
                if amount == 0: continue

                alpha -= amount
                nx, ny = x, y
                # 해당 칸 좌표를 찾아감
                for nd in root:
                    nx += dxdy[(d+nd)%4][0]
                    ny += dxdy[(d+nd)%4][1]
                # 범위 바깥이면 정답에 더해주고
                # 범위 안이면 해당 칸에 더해줌
                if not(0<=nx<N and 0<=ny<N):
                    ans += amount
                    continue
                arr[nx][ny]+=amount

            # 마지막으로 알파 업데이트
            nx, ny = x+dxdy[d][0], y+dxdy[d][1]
            if not (0 <= nx < N and 0 <= ny < N):
                ans += alpha
            else:
                arr[nx][ny]+= alpha

            # 지금 칸 0으로 만들어주고(사실 필요 없을듯)
            # arr[x][y]=0

            # 제일 왼쪽 위에 도착하면 끝
            if x==y==0:
                end=1
                break

        if end: break
    if end: break

print(ans)
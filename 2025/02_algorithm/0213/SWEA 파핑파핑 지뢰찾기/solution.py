from collections import deque

dxdy = ((0,1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 전체에서 다른 칸을 눌러서 터트릴 수 있는 경우와
    # 폭탄인 경우를 제외
    ans = N*N
    arr = [list(input()) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 폭탄인 경우 제외
            if arr[i][j]=='*':
                ans-=1
            else :
                # 폭탄이 아닌 경우
                # 8방을 돌면서 폭탄이 하나도 없으면 큐에 넣기
                for dx, dy in dxdy:
                    nx, ny = i+dx, j+dy
                    if not (0 <= nx < N and 0 <= ny < N): continue
                    if arr[nx][ny]=='*':
                        break
                else :
                    q = deque()
                    q.append((i, j))
                    visited[i][j]=True
                    while q:
                        # 큐에서 뽑히는 아이템마다 팔방 채크
                        x, y = q.popleft()
                        stack = []
                        for dx, dy in dxdy:
                            nx, ny = x+dx, y+dy
                            if not(0<=nx<N and 0<=ny<N): continue
                            if visited[nx][ny]: continue
                            if arr[nx][ny]=='*':
                                break
                            # 폭탄이 아닌 좌표를 stack에 넣기
                            stack.append((nx, ny))
                        else :
                            # 폭탄이 하나도 안나와서 반복문 break가 안되면
                            # stack 전체를 비우면서 안눌러도 되는칸이므로 답 줄이고, 방문표시
                            while stack:
                                nx, ny = stack.pop()
                                q.append((nx, ny))
                                visited[nx][ny]=True
                                ans -=1
    print(f'#{tc} {ans}')




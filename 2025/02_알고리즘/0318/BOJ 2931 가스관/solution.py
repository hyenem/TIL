dic = {'|': (0, 2), '-': (1, 3), '+': (0, 1, 2, 3), '1': (1, 2), '2': (0, 1), '3':(0, 3), '4':(2, 3)}
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
x, y, s = -1, -1, set()
for i in range(N):
    for j in range(M):
        if arr[i][j] in dic:
            for d in dic[arr[i][j]]:
                dx, dy = dxdy[d]
                nx, ny = i+dx, j+dy
                if 0<=nx<N and 0<=ny<M and arr[nx][ny]=='.':
                    x, y = nx, ny
                    s.add((d+2)%4)

for key, value in dic.items():
    if value == tuple(sorted(list(s))):
        print(x+1, y+1, key)
        break
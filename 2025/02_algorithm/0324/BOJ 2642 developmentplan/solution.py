from collections import deque
dic = {
    1: ((0, 1), (1, 2, 3, 0, 4, 5)),
    2: ((0, -1), (3, 0, 1, 2, 4, 5)),
    3: ((-1, 0), (0, 4, 2, 5, 3, 1)),
    4: ((1, 0), (0, 5, 2, 4, 1, 3))
}

cube = [[0] for _ in range(6)]
arr = [list(map(int, input().split())) for _ in range(6)]
for i in range(6):
    for j in range(6):
        if arr[i][j]!=0:
            ncube = [ele for ele in cube]
            ncube[3][0] = arr[i][j]
            q = deque([(i, j, ncube)])
            break
ans = 7
while q:
    x, y, cube = q.popleft()
    for d in range(1, 5):
        (dx, dy), change = dic[d]
        nx, ny = x+dx, y+dy
        if not(0<=nx<6 and 0<=ny<6): continue
        if arr[nx][ny]==0: continue
        ncube = []
        for i in range(6):
            ncube.append(cube[change[i]])

        if ncube[3][0]==arr[nx][ny]: continue
        elif ncube[3][0]==0:
            ncube[3][0]=arr[nx][ny]
            q.append((nx, ny, ncube))
        else :
            ans = 0
            break
    if not ans: break

flip = (2, 3, 0, 1, 5, 4)
if ans!=0:
    for i in range(6):
        if cube[i][0]==1:
            ans = cube[flip[i]][0]
            break
print(ans)


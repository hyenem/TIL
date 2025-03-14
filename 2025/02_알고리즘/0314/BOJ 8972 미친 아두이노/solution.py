N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
dxdy = (0, (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1))
robot = []

cmd = list(map(int, input()))
for i in range(N):
    for j in range(M):
        if arr[i][j]=='I':
            x, y = i, j
            arr[i][j]='.'
        elif arr[i][j]=='R':
            arr[i][j]='.'
            robot.append([i, j])

cnt = 0
ans = 0
for c in cmd:
    cnt += 1
    dx, dy = dxdy[c]
    x, y = x+dx, y+dy

    boom = set()
    robotexist = [[0]*M for _ in range(N)]
    for i in range(len(robot)):
        rx, ry = robot[i][0], robot[i][1]

        rdx, rdy = 0, 0
        if rx<x: rdx += 1
        elif rx>x: rdx -= 1
        if ry<y: rdy += 1
        elif ry>y: rdy -= 1

        rx, ry = rx+rdx, ry+rdy
        if rx==x and ry==y:
            ans = cnt
            break

        robot[i][0], robot[i][1]=rx, ry
        if robotexist[rx][ry]:
            boom.add(robotexist[rx][ry]-1)
            boom.add(i)
        else :
            robotexist[rx][ry]=i+1


    if ans:
        print('kraj', ans)
        break

    boom = list(boom)
    boom.sort(reverse=True)
    for idx in boom:
        del robot[idx]

else :
    arr[x][y]='I'
    for rx, ry in robot:
        arr[rx][ry]='R'

    for ele in arr:
        print(''.join(ele))
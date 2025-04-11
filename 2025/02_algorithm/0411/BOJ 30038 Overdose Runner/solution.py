level = 1
exp = 0
speed = 1
attack_bound = 1
attack_point = 5
overdose = 0
dcnt = 0
active = 0

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

K = int(input())
mhp = list(map(int, input().split()))
mdf = list(map(int, input().split()))
mexp = list(map(int, input().split()))
midx = 0

for i in range(N):
    for j in range(M):
        if arr[i][j]=='p':
            px, py = i, j
            arr[i][j]='.'
        elif arr[i][j]=='m':
            arr[i][j]=[mhp[midx], mdf[midx], mexp[midx]]
            midx += 1

S = int(input())
cmds = list(input().split())

dxdy = {'u':(-1, 0), 'd':(1, 0), 'l':(0, -1), 'r': (0, 1)}

for cmd in cmds:

    if cmd=='w':
        active += 1
        if overdose: overdose -= 1

    elif cmd in {'u', 'd', 'l', 'r'}:
        dx, dy = dxdy[cmd]
        nx, ny = px+dx*speed, py+dy*speed
        if not(0<=nx<N and 0<=ny<M): continue
        if arr[nx][ny]=='*' or (arr[nx][ny]!='.' and arr[nx][ny]!='g'): continue

        active += 1
        if overdose: overdose -= 1
        px, py = nx, ny

    else:
        if overdose: continue

        if cmd[0]=='a':
            dx, dy = dxdy[cmd[1]]
            active += 3

            for k in range(1, attack_bound+1):
                nx, ny = px+dx*k, py+dy*k
                if arr[nx][ny]=='*': break

                if arr[nx][ny]=='.' or arr[nx][ny]=='g': continue
                monster = arr[nx][ny]
                monster[0]-=max(0, attack_point - monster[1])
                if monster[0]<=0:
                    exp += monster[2]
                    arr[nx][ny]='.'

            while exp>=level*10:
                exp -= level*10
                attack_point += level
                attack_bound += 1
                level += 1

        elif cmd =='dd':
            active += 2
            dcnt+=1
            if dcnt==5:
                dcnt=0
                overdose = 10
            if speed: speed -= 1

        elif cmd =='du':
            active += 2
            dcnt+=1
            if dcnt==5:
                dcnt=0
                overdose = 10
            speed += 1

        elif cmd=='c':
            if arr[px][py]=='g':
                break

print(level, exp)
print(active)
moster_result = []
for i in range(N):
    for j in range(M):
        if arr[i][j]!='.' and arr[i][j]!='g' and arr[i][j]!='*':
            moster_result.append(arr[i][j][0])
            arr[i][j]='m'
arr[px][py]='p'
for ele in arr:
    print(''.join(ele))
print(*moster_result)

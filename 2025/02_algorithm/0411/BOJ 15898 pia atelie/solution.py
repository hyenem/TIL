def btk(cnt):
    global ans, power, color
    if ans==1008: return
    if cnt==3:
        tmpans = 0
        for i in range(5):
            for j in range(5):
                tmpans += power[i][j]*score[color[i][j]]
        ans = max(ans, tmpans)
        return

    tmpp = [ele[:] for ele in power]
    tmpc = [ele[:] for ele in color]

    for idx in range(N):
        if visited[idx]: continue

        visited[idx]=1

        ipower = ingredients[idx][0]
        icolor = ingredients[idx][1]
        for si, sj in ((0, 0), (0, 1), (1, 0), (1, 1)):
            for _ in range(4):
                for i in range(4):
                    for j in range(4):
                        x, y= si+i, sj+j
                        power[x][y]= min(9, max(0, power[x][y]+ipower[i][j]))
                        if ingredients[idx][1][i][j]!='W':
                            color[x][y]=icolor[i][j]
                btk(cnt+1)
                power = [ele[:] for ele in tmpp]
                color = [ele[:] for ele in tmpc]
                ipower = list(map(list, zip(*ipower)))[::-1]
                icolor = list(map(list, zip(*icolor)))[::-1]
        visited[idx]=0


N = int(input())
ingredients = []
for _ in range(N):
    power = [list(map(int, input().split())) for _ in range(4)]
    color = [list(input().split()) for _ in range(4)]
    ingredients.append([power, color])

score = {'R':7, 'B':5, 'G':3, 'Y':2, 'W':0}
power = [[0]*5 for _ in range(5)]
color = [['W']*5 for _ in range(5)]
visited = [0]*N
ans = 0
btk(0)
print(ans)
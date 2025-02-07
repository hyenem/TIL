dic = {}
for i in range(5):
    tmp = list(map(int, input().split()))
    for j in range(5):
        dic[tmp[j]]=(i, j)

row = [0]*5
col = [0]*5
rightdown = 0
rightup = 0
ans = 0
bingo = 0

for i in range(5):
    tmp = list(map(int, input().split()))
    for j in range(5):
        ans += 1
        x, y = dic[tmp[j]]

        if row[x]==4:
            bingo+=1
        else :
            row[x]+=1

        if col[y]==4:
            bingo+=1
        else :
            col[y]+=1

        if x+y==4:
            if rightup==4:
                bingo+=1
            else :
                rightup+=1

        if x==y:
            if rightdown==4:
                bingo+=1
            else :
                rightdown+=1

        if bingo>=3: break
    if bingo >=3: break
print(ans)

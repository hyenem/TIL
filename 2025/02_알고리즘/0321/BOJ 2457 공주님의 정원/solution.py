N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort()
flower = []
for sm, sd, em, ed in lst:
    flower.append(((sm, sd), (em, ed)))
ans = 0
start, end = (0, 0), (3, 2)
tmpstart, tmpend = 0, 0
for i in range(N):
    print(start, end)
    if flower[i][0]==start:
        end = flower[i][1]
        if end>(11, 30):
            print(ans)
            break
    else :
        print(start<flower[i][0]<end)
        if start<flower[i][0]<end:
            if tmpend!=0 and flower[i][1]>=tmpend:
                tmpstart = flower[i][0]
                tmpend = flower[i][1]
        else :
            if tmpstart!=0:
                start, end = tmpstart, tmpend
                tmpstart, tmpend = 0, 0
                ans += 1
                if end>(11, 30):
                    print(ans)
                    break
else :
    if tmpstart!=0:
        start, end = tmpstart, tmpend
        tmpstart, tmpend = 0, 0
        ans += 1
        if end > (11, 30):
            print(ans)
        else :
            print(-1)
    else: print(-1)

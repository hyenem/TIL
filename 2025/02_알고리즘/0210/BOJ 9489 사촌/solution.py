N, K = map(int, input().split())
while N+K !=0:
    depthnode = [[] for _ in range(N)]
    thiscnt = 0
    depth = 1
    ansdepth = N
    ansidx = 0
    arr = list(map(int, input().split()))
    depthcnt = [0]*N
    if K==arr[0]:
        print(0)
    else :
        depthnode[0].append([arr[0]])
        depthnode[1].append([])
        depthcnt[0]+=1
        for i in range(1, N):
            if i!=1:
                if arr[i-1]+1 != arr[i]:
                    thiscnt+=1
                    if thiscnt == depthcnt[depth-1]:
                        thiscnt = 0
                        depth +=1
                        if depth > ansdepth:
                            break
                    depthnode[depth].append([])
            depthnode[depth][-1].append(arr[i])
            depthcnt[depth]+=1
            if arr[i]==K:
                ansdepth = depth
                ansidx = len(depthnode[depth])-1
        fromm = 0
        too = 0
        ans = 0
        for ele in depthnode[ansdepth-1]:
            if fromm+len(ele)>ansidx:
                too = fromm+len(ele)
                break
            else :
                fromm+=len(ele)
        for i in range(fromm, min(len(depthnode[ansdepth]),too)):
            if i!=ansidx:
                ans+=len(depthnode[ansdepth][i])
        print(ans)
    N, K = map(int, input().split())

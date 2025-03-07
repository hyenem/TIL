def comb2(idx):
    global ans
    if idx==10:
        ans +=1
        return
    if tf[idx] and (len(compute)<2 or not(compute[-1]==arr[idx] and compute[-2]==arr[idx])):
        compute.append(arr[idx])
        comb2(idx+1)
        compute.pop()
    elif not tf[idx]:
        for i in range(1,6):
            if i==arr[idx]: continue
            if len(compute)<2 or not(compute[-1]==i and compute[-2]==i):
                compute.append(i)
                comb2(idx+1)
                compute.pop()
def comb(idx, cnt):
    if cnt>=5:
        comb2(0)
    for i in range(idx+1, 10):
        tf[i]=True
        comb(i, cnt+1)
        tf[i]=False


arr=list(map(int, input().split()))
tf = [False]*10
compute =[]
ans = 0
comb(-1, 0)
print(ans)
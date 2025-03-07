def solution(cnt):
    if cnt==36:
        if sum(arr[-1])!=0:
            return False
        return True

    i, j = cnt//6, cnt%6
    if i!=0 and j==0 and arr[i-1][0]+arr[i-1][1]+arr[i-1][2]!=0:
        return False

    if i==j : return solution(cnt+1)
    if solution(cnt+1): return True

    if arr[i][0]>0 and arr[j][2]>0:
        arr[i][0]-=1
        arr[j][2]-=1
        if solution(cnt+1): return True
        arr[i][0]+=1
        arr[j][2]+=1

    if arr[i][1]>0 and arr[j][1]>0:
        arr[i][1]-=1
        arr[j][1]-=1
        if solution(cnt+1): return True
        arr[i][1]+=1
        arr[j][1]+=1

    if arr[i][2]>0 and arr[j][0]>0:
        arr[i][2]-=1
        arr[j][0]-=1
        if solution(cnt+1): return True
        arr[i][2]+=1
        arr[j][0]+=1

    return False

ans = []
for _ in range(4):
    lst = list(map(int, input().split()))
    arr = [[0]*3 for _ in range(6)]
    for i in range(18):
        arr[i//3][i%3]=lst[i]
    for i in range(6):
        if sum(arr[i])!=5:
            ans.append(0)
            break
    else :
        if solution(0):
            ans.append(1)
        else :
            ans.append(0)

print(*ans)
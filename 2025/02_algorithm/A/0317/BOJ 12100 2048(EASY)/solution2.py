def delete(tmp):
    for i in range(len(tmp)):
        for j in range(len(tmp[i])-1, -1, -1):
            if tmp[i][j]==0:
                del tmp[i][j]

def pop(tmp):
    global ans
    cnt = 0
    for i in range(len(tmp)):
        idx = 0
        while idx < len(tmp[i]) - 1:
            if tmp[i][idx] == tmp[i][idx + 1]:
                tmp[i][idx] *= 2
                cnt +=1
                ans = max(tmp[i][idx], ans)

                del tmp[i][idx + 1]
            idx += 1
    return cnt

def btk(cnt, arr):
    if cnt==5: return

    # 좌
    tmp = [ele[:] for ele in arr]
    if cnt==0:
        delete(tmp)
    if cnt!=0 and pop(tmp)!=0:
        btk(cnt+1, tmp)

    # 우
    tmp = [ele[::-1] for ele in arr]
    if cnt==0:
        delete(tmp)
    pop(tmp)
    btk(cnt+1, tmp)

    # 상
    tmp = [[] for _ in range(N)]
    ttmp = [[] for _ in range(N)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            tmp[j].append(arr[i][j])
            ttmp[j].append(arr[i][j])
    if cnt==0:
        delete(tmp)
    pop(tmp)
    btk(cnt+1, tmp)

    # 하
    tmp = [ele[::-1] for ele in ttmp]
    if cnt==0:
        delete(tmp)
    pop(tmp)
    btk(cnt+1, tmp)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, arr[i][j])
btk(0, arr)

print(ans)



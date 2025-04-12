def check():
    if K==1: return True
    for j in range(M):
        acc = 1
        for i in range(1, N):
            if arr[i-1][j]==arr[i][j]:
                acc+=1
                if acc>=K:
                    break
            else:
                acc = 1
        else:
            return False
    return True
def btk(idx, cnt):
    global ans
    if cnt>=ans: return
    if check():
        ans = cnt
        return

    for i in range(idx, 2*N):
        tmp = arr[i//2][:]

        arr[i//2]=[i%2]*M
        btk((i//2)*2+2, cnt+1)
        arr[i//2]=tmp

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = K-1
    btk(0, 0)
    print(f'#{tc} {ans}')
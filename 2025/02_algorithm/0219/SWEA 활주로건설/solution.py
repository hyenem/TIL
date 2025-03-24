def check(i):
    visited = [False] * N
    flag = True
    acc = 1
    for j in range(N - 1):
        if arr[i][j] == arr[i][j + 1]:
            acc += 1
        else:
            if arr[i][j + 1] == arr[i][j] + 1:
                if acc<X: return False
                acc = 1
                for k in range(X):
                    if visited[j-k]: return False
                    visited[j-k]=True
            elif arr[i][j+1]!=arr[i][j]-1: return False
    acc=1
    for j in range(N-1, 0, -1):
        if arr[i][j-1]==arr[i][j]:
            acc+=1
        else :
            if arr[i][j-1] == arr[i][j]+1:
                if acc<X: return False
                acc=1
                for k in range(X):
                    if visited[j+k]: return False
                    visited[j+k]=True
            elif arr[i][j - 1] != arr[i][j] - 1:
                return False
    return True

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for _ in range(2):
        for i in range(N):
            if check(i): ans +=1

        arr = list(zip(*arr))

    print(f'#{tc} {ans}')
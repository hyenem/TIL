L, N, T = map(int, input().split())
arr = []
for _ in range(N):
    num, direction = input().split()
    arr.append([int(num), 1 if direction=='R' else -1])

ans = 0
for _ in range(T):
    # 이동하기
    for i in range(N):
        arr[i][0]+=arr[i][1]

    # 부딪히면 방향 바꾸기
    for i in range(N):
        if arr[i][0] in {0, L}:
            arr[i][1]*=-1
    for i in range(N):
        for j in range(i+1, N):
            if arr[i][0]==arr[j][0]:
                arr[i][1]*=-1
                arr[j][1]*=-1
                ans += 1
print(ans)
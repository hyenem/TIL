T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    for i in range(N//2):
        data = input()
        for j in range(N//2-i, N//2+1+i):
            ans += int(data[j])
    for i in range(N // 2, -1, -1):
        data = input()
        for j in range(N//2-i, N//2+1+i):
            ans += int(data[j])
    print(f'#{tc} {ans}')
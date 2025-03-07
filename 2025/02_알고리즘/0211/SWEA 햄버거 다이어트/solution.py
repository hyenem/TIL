#DP

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    # i 번째 인덱스는 칼로리를 k이하로 먹었을 때 점수의 최댓값
    DP = [0]*(K+1)
    for ele in arr:
        score, cal = ele
        for i in range(K, cal-1, -1):
            DP[i]=max(DP[i], DP[i-cal]+score)
    print(f'#{tc} {DP[K]}')
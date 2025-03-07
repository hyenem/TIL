T = int(input())
for _ in range(T):
    N = int(input())

    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort()

    # 서류 점수는 계속 낮아지니까,
    # 면접 점수가 높은 사람을 찾아가기
    ans = 1
    minn = arr[0][1]
    for s, m in arr:
        if minn>m:
            ans +=1
            minn=m
    print(ans)
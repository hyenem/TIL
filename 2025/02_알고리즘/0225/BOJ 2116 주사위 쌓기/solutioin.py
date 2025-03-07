# 옆면 중 최댓값을 찾는 함수
def check_side_max(j, u, d):
    if 6 in {arr[j][u], arr[j][d]}:
        if 5 in {arr[j][u], arr[j][d]}:
            return 4
        else:
            return 5
    else:
        return 6


N = int(input())
dtou = [5, 3, 4, 1, 2, 0]
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
# 첫번째 주사위의 아랫면이 결정되면 모든 주사위의 위, 아래가 결정됨
# 옆면은 위, 아래가 아닌 것들 중 가장 큰 것으로 맞추면 됨

# 첫번째 주사위의 아랫면 인덱스
for i in range(6):
    d = i
    u = dtou[d]
    tmp = check_side_max(0, u, d)

    for j in range(1, N):
        # 각 주사위에서 이전의 윗면과 같은 아랫면 위치 찾기
        for k in range(6):
            if arr[j - 1][u] == arr[j][k]:
                d = k
                break
        u = dtou[d]

        tmp += check_side_max(j, u, d)

    ans = max(ans, tmp)

print(ans)
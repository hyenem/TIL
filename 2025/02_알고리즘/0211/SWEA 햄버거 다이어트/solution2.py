# 재귀
def solution(idx, cal, score):
    global ans
    # 최대 칼로리 넘치면 리턴
    if cal>L: return
    ans = max(ans, score)
    # i번째 재료 가져가기
    for i in range(idx+1, N):
        solution(i, cal+arr[i][1], score+arr[i][0])

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    solution(-1, 0, 0)
    print(f'#{tc} {ans}')
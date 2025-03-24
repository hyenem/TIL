T = int(input())

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
# 끝나는 시간 순으로 정렬
arr.sort(key = lambda x:(x[1], x[0]))
ans = 1
# 이전 회의가 끝난 시간
end = arr[0][1]
for i in range(1, N):
    # 이전 회의가 끝나고 나서 이번 일을 시작할 수 있으면
    if end<=arr[i][0]:
        ans +=1
        end = arr[i][1]
print(ans)
N, M = map(int,input().split())
arr = [0]+list(map(int, input().split()))
# 누적합 만들기
for i in range(1, N+1):
    arr[i]+=arr[i-1]

# e까지의 합에서 s-1까지의 합을 빼면
# s부터 e까지의 합
for _ in range(M):
    s, e = map(int, input().split())
    print(arr[e]-arr[s-1])
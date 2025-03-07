N = int(input())
arr = list(map(int, input().split()))
# 이전까지의 최대에 나를 더한 것과 나 중 큰것
for i in range(1, N):
    arr[i]=max(arr[i-1]+arr[i], arr[i])
print(max(arr))
N = int(input())
arr = list(map(int, input().split()))

ans = []
for i in range(0, N):
    if arr[i]==0:
        ans.append(i+1)
    else :
        ans.insert(i-arr[i], i+1)
print(*ans)
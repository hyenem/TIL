N = int(input())
arr = list(map(int, input().split()))
ans = max(arr)
for i in range(1,N):
    arr[i]+=arr[i-1]
ans = max(ans, max(arr))
stack = []
for i in range(N):
    if stack and stack[-1]<arr[i]:
        stack.append(arr[i])
        if len(stack)>1:
            ans = max(ans, stack[-1]-stack[0])
    else :
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        stack.append(arr[i])
print(ans)
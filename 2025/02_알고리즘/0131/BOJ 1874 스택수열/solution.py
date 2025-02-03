N = int(input())
ans = []
num = [(N-i) for i in range(N)]
stack = []
for _ in range(N):
    data = int(input())
    if stack and data==stack[-1]:
        ans.append('-')
        stack.pop()
        continue
    while num:
        ans.append('+')
        stack.append(num.pop())
        if stack and data == stack[-1]:
            ans.append('-')
            stack.pop()
            break
if stack:
    print('NO')
else :
    for ele in ans:
        print(ele)

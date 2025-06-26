for tc in range(1, 11):
    N, data = input().split()
    stack = []
    for ele in data:
        if stack and stack[-1]==ele:
            stack.pop()
        else :
            stack.append(ele)
    print(f'#{tc} {"".join(stack)}')
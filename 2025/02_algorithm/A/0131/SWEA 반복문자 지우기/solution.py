T = int(input())
for tc in range(1, T+1):
    data = input()
    stack = []

    for ele in data:
        #비어있거나, 이전 원소가 이번 원소와 같지 않은경우, stack에 원소 넣기
        if not stack or stack[-1]!=ele:
            stack.append(ele)
       	# 꼭대기 원소가 이번 원소와 같은 경우 꼭대기 원소 없애기
        else :
            stack.pop()
    #남은 원소 개수
    print(f'#{tc} {len(stack)}')
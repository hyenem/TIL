# print(ord('{')) 123
# print(ord('}')) 125
# print(ord('(')) 40
# print(ord(')')) 41

T = int(input())
for tc in range(1, T+1):
    data = input()
    stack = []
    for ele in data:
        if ele in {'{', '}', '(', ')'}:  #괄호인 경우
            #이전 괄호가 짝이 맞으면 pop
            if stack and ord(stack[-1]) - ord(ele) in {-1, -2}:
                stack.pop()
            # 팝되는 경우가 아니면 그냥 쌓아두기
            else :
                stack.append(ele)
    print(f'{tc}', end =' ')
    #괄호가 다 짝이 맞아서 나갔으면 1, 아니면 0
    if stack:
        print(0)
    else :
        print(1)

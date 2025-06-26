def solution(cnt):
    global result
    if len(com)+(5-cnt)>10:
        return
    if len(com)==10:
        if cnt>=5:
            result += 1
        return
    for i in range(1, 6):
        if len(com)<2 or not (com[-1] == i and com[-2] == i):
            com.append(i)
            if arr[len(com) - 1]==i:
                solution(cnt+1)
            else :
                solution(cnt)
            com.pop()

arr = list(map(int, input().split()))
com =[]
result = 0
solution(0)
print(result)
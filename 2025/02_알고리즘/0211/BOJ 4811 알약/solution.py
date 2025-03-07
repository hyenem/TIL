def solution(w, h):
    if arr[w][h]!=-1:
        return arr[w][h]
    if w==0:
        ans = 1
    elif h==0:
        ans = solution(w-1, h+1)
    else :
        ans = solution(w-1, h+1)+solution(w, h-1)
    arr[w][h]=ans
    return ans

arr = [[-1]*31 for _ in range(31)]
while True:
    data = int(input())
    if data ==0: break
    print(solution(data, 0))

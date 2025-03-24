def solution(idx, res):
    global maximum, minimum
    if idx==N:
        maximum = max(maximum, res)
        minimum = min(minimum, res)
    for i in range(4):
        if cal[i]==0: continue
        cal[i]-=1
        if i == 0:
            solution(idx+1, res+arr[idx])
        elif i==1:
            solution(idx+1, res-arr[idx])
        elif i == 2:
            solution(idx+1, res * arr[idx])
        elif i == 3:
            if res<0:
                solution(idx + 1, (-1)*(((-1)*res) // arr[idx]))
            else : solution(idx + 1, res // arr[idx])
        cal[i]+=1

N = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))
maximum = -1000000000
minimum = 1000000000
solution(1, arr[0])
print(maximum)
print(minimum)
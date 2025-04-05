def btk(idx, acc):
    global minimum, maximum
    if idx==N:
        minimum = min(acc, minimum)
        maximum = max(acc, maximum)
        return

    if operator[0]!=0:
        operator[0]-=1
        btk(idx+1, acc+lst[idx])
        operator[0]+=1

    if operator[1]!=0:
        operator[1]-=1
        btk(idx+1, acc-lst[idx])
        operator[1]+=1

    if operator[2]!=0:
        operator[2]-=1
        btk(idx+1, acc*lst[idx])
        operator[2]+=1

N = int(input())
lst = list(map(int, input().split()))
operator = list(map(int, input().split()))
minimum = 1000000000
maximum = -1000000000
btk(1, lst[0])
print(minimum, maximum)
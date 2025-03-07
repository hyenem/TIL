from collections import deque

def solution():
    arr = [0]+list(map(int, input().split()))
    if len(set(list(arr[1:5])))==1 and len(set(list(arr[9:13])))==1:
        l1 = [13, 14, 5, 6, 17, 18, 21, 22]
        l2 = [15, 16, 7, 8, 19, 20, 23, 24]
    elif len(set(list(arr[13:17])))==1 and len(set(list(arr[17:21])))==1:
        l1 = [1, 3, 5, 7, 9, 11, 22, 24]
        l2 = [2, 4, 6, 8, 10, 12, 21, 23]
    elif len(set(list(arr[5:9])))==1 and len(set(list(arr[21:25])))==1:
        l1 = [3, 4, 17, 19, 10, 9, 16, 14]
        l2 = [1, 2, 18, 20, 11, 12, 13, 15]
    else:
        print(0)
        return

    q1=deque([arr[i] for i in l1])
    q2=deque([arr[i] for i in l2])

    q2.rotate(2)
    if q1==q2: print(1)
    else :
        q2.rotate(4)
        if q1==q2:
            print(1)
        else : print(0)

solution()
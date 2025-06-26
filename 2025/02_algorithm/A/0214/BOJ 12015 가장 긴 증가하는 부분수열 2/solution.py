def binarysearch(x):
    left = 0
    right = len(increase)-1
    while left<=right:
        mid = (left+right)//2
        if increase[mid]==x:
            return
        elif increase[mid]<x:
            left = mid + 1
        else :
            right = mid - 1
    if left==len(increase):
        increase.append(x)
    else :
        increase[left]=x

N = int(input())
arr = list(map(int, input().split()))

increase = [arr[0]]
for i in range(1, N):
    binarysearch(arr[i])
print(len(increase))

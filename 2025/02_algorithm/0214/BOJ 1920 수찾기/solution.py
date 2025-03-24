def binarysearch(ele):
    left = 0
    right = N-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==ele:
            print(1)
            return
        elif arr[mid]>ele:
            right = mid-1
        else:
            left = mid+1
    print(0)

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
for ele in map(int, input().split()):
    binarysearch(ele) # 이진탐색 함수화
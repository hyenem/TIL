N = int(input())
arr1 = list(enumerate(map(int, input().split())))
sort1 =sorted(arr1, reverse=True, key=lambda x:(x[1], -x[0]))
M = int(input())
arr2 = list(enumerate(map(int, input().split())))
sort2 =sorted(arr2, reverse=True, key=lambda x:(x[1], -x[0]))

pointer1 = 0
pointer2 = 0
idx1 = -1
idx2 = -1
ans = []
while pointer1<N and pointer2<M:
    if sort1[pointer1][1]==sort2[pointer2][1]:
        if idx1<sort1[pointer1][0] and idx2<sort2[pointer2][0]:
            ans.append(sort1[pointer1][1])
            idx1 = sort1[pointer1][0]
            idx2 = sort2[pointer2][0]
            pointer1 += 1
            pointer2 += 1
        elif idx1<sort1[pointer1][0]:
            pointer2+=1
        else: pointer1+=1
    elif sort1[pointer1][1]<sort2[pointer2][1]:
        pointer2 += 1
    else :
        pointer1 += 1
print(len(ans))
print(*ans)

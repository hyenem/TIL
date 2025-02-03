import sys
sys.setrecursionlimit(10000)
def binary(p):
    global maxi
    if p not in dic:
        return 0
    if len(dic[p])==1:
        w = binary(dic[p][0][0])+dic[p][0][1]
        maxi = max(maxi, w)
        return w
    elif len(dic[p])>=2:
        weights = []
        for ele in dic[p]:
            weights.append(binary(ele[0])+ele[1])
        weights.sort(reverse=True)
        w1 = weights[0]
        w2 = weights[1]
        maxi = max(maxi, w1+w2)
        return max(w1, w2)


N = int(input())
dic = {}
maxi = 0
for _ in range(N-1):
    p, c, w = map(int, input().split())
    if p in dic:
        dic[p].append((c, w))
    else :
        dic[p]=[(c, w)]

binary(1)
print(maxi)
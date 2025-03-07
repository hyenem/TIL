import sys
input = sys.stdin.readline

N, T = map(int, input().split())
turn = list(map(int, input().split()))
have = [[] for _ in range(N+1)]
num = {}
visited = []
ans=[]

for i in range(T):
    if have[turn[i]]:
        card = have[turn[i]]
        have[turn[i]] = []
    else:
        card = list(input().split())

    ans.append(card[0])
    if card[1]=='acquire':
        if card[2] not in num:
            num[card[2]]=len(visited)
            visited.append(0)
        if visited[num[card[2]]]:
            have[turn[i]] = card
        else:
            visited[num[card[2]]]=1
    elif card[1]=='release' :
        visited[num[card[2]]]=0

for ele in ans:
    print(ele)
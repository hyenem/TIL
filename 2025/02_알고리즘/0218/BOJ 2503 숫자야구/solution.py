N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(123, 1000):
    s= set([i//100, (i//10)%10, i%10])
    # 서로다른 세 수가 아니거나 0을 포함하는 경우는 지나가기
    if len(s)!=3 or 0 in s: continue

    #나머지 경우에서 조건 채크
    flag=False
    for num, s, b in arr:
        scnt, bcnt = 0,0
        #일, 십, 백의 자리수 쪼개기
        n1 = [i//100, (i//10)%10, i%10]
        n2 = [num//100, (num//10)%10, num%10]
        # 스트라이크, 볼 세기
        for k in range(3):
            for j in range(3):
                if n1[k]==n2[j]:
                    if k==j: scnt+=1
                    else : bcnt+=1
        # 안맞으면 break
        if scnt!=s or bcnt!=b:
            flag = True
            break
    if flag: continue

    # 안맞는 경우가 하나도 없었으면 정답 하나 올리기
    ans+=1
print(ans)
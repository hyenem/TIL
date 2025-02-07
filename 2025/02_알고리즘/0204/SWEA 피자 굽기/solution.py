T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 각 피자에 번호 붙여주기
    pizza = list(enumerate(map(int, input().split()), start=1))
    q = []

    # 화덕에 피자 꽉 채우기
    for i in range(N):
        q.append(pizza.pop(0))

    # 다 구워진 피자의 개수를 세는 것
    cnt = 0
    while cnt!=M:
        item = q.pop(0)
        # 빈칸이 나오면 그냥 다음칸 보기
        if item[0]==0:
            q.append(item)
            continue
        # 빈칸이 아닐 때
        # 치즈가 다 녹았으면 빼고
        if item[1]//2==0:
            poppizza = item
            cnt+=1
            # 다른 피자를 넣거나
            if pizza:
                q.append(pizza.pop(0))
            # 아직 안넣은 피자가 없으면 빈칸을 넣기
            else :
                q.append((0, 0))
        # 다 안녹았으면 절반으로 만들어서 넣기
        else :
            q.append((item[0], item[1]//2))
    print(f'#{tc} {poppizza[0]}')
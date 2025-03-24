T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cont = list(map(int,input().split()))
    truck = list(map(int, input().split()))
    cont.sort()
    truck.sort()

    ans = 0
    while truck and cont:
        # 제일 큰 컨테이너를 옮길 수 있으면
        c=cont.pop()
        # 트럭 없애고 옮기기
        if truck[-1]>=c:
            truck.pop()
            ans+=c
        # 옮길 수 없으면 그냥 컨테이너 버리기
    print(f'#{tc} {ans}')
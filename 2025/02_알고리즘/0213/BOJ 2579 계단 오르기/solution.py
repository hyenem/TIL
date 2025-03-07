N = int(input())
arr = [[0,0]]+[[int(input())]*2 for _ in range(N)]
if N==1: print(arr[1][0])
else :
    # 한칸으로 올라온 최대, 두칸으로 올라온 최대를 저장
    for i in range(2, N+1):
        # 한칸을 두번 연속 밟을 수는 없음
        # 즉 이번 한칸은 이전 두칸으로 업데이트
        arr[i][0]+=arr[i-1][1]
        # 두칸은 두칸 전의 어떤 것에서도 올 수 있음
        arr[i][1]+=max(arr[i-2])
    print(max(arr[N]))
def solution(x, y, k):
    for i in range(x, x+k):
        for j in range(y, y+k):
            # 지금 보고있는 색종이를 쪼개야하는 상황
            if arr[i][j]!=arr[x][y]:
                # 4등분해서 다시보기
                solution(x,y,k//2)
                solution(x+k//2,y,k//2)
                solution(x,y+k//2, k//2)
                solution(x+k//2,y+k//2, k//2)
                return
    # 안쪼개도 되면 색에 맞춰서 색종이 하나씩 추가
    ans[arr[x][y]]+=1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [0,0]
solution(0,0,N)
for ele in ans:
    print(ele)
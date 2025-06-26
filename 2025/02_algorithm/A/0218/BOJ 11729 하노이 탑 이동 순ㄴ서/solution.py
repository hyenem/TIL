# 몇번 원판을 어디에서 어디로 올릴건지
def solution(N, s, e):
    # 하나짜리면 그냥 옮기기
    if N==1:
        ans.append((s, e))
        return
    # 맨 밑에거 제외하고 올기려는 칸 말고 다른 칸으로 옮기기
    solution(N-1, s, 6-s-e)
    # 맨 밑에거 옮기기
    ans.append((s, e))
    #옮겨놨던거 다시 내 위로 올리기
    solution(N-1, 6-s-e, e)


N = int(input())
ans = []
solution(N, 1, 3)
print(len(ans))
for s, e in ans:
    print(s, e)
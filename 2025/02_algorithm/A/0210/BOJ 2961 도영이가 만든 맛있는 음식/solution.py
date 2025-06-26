# 제출횠수 : 2회
# 풀이시간 : 7분
# 실행시간 : 88ms
# 메모리 : 108384KB

def solution(idx, S, B):
    global ans
    # 하나도 안 고른 경우 제외하는 방법
    # S로는 처리 못할 것 같아요. 신맛이 1일수도 있어서
    if B!=0:
        if ans == -1:
            ans = abs(S-B)
        else :
            ans = min(abs(S-B), ans)
    # 자꾸 i가 아니라 idx+1을 넘기는 실수를 하네요 ㅠㅜ
    for i in range(idx+1, N):
        solution(i, S*arr[i][0], B+arr[i][1])


N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
ans = -1
# 합은 기본이 0 곱은 기본이 1임을 신경써야합니다.
solution(-1, 1, 0)
print(ans)
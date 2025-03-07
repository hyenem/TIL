'''
제출횟수 : 1회
풀이시간 : 19분

* 명심할 것!
인덱스 맞춰서 입력 주어지는지 확인하기

구상 : 5분
* 문제 꼼꼼히 읽고 이해하기
* 합을 미리 뽑아둘지, 볼때마다 채크할지 고민해봄
* 결 외칠 때 합 다 외쳤는지 채크해야해서 미리 뽑아두는게 낫다고 판단

구현 : 10분
디버깅 : 4분
* 합이 되는 조건을 잘못 작성함(같같같, 다다다 이것만 합이 된다고함 ㅠ)
* 주어지는 인덱스가 1번부턴데 0번부터로 풂
* 입력 str으로 받아놓고 int 연산 하려고함
'''

arr = [tuple(input().split()) for _ in range(9)]

H = []
# 세개 속성 조합하기
for i in range(9):
    for j in range(i+1, 9):
        for k in range(j+1, 9):
            # 각 속성이 다 같거나 다 다른 경우를 찾아서 합인 경우 저장하기
            if arr[i][0]==arr[j][0]==arr[k][0] or (arr[i][0]!=arr[j][0] and arr[i][0]!=arr[k][0] and arr[j][0]!=arr[k][0]):
                if arr[i][1]==arr[j][1]==arr[k][1] or (arr[i][1] != arr[j][1] and arr[i][1] != arr[k][1] and arr[j][1] != arr[k][1]):
                    if arr[i][2] == arr[j][2] == arr[k][2] or(arr[i][2] != arr[j][2] and arr[i][2] != arr[k][2] and arr[j][2] != arr[k][2]):
                        H.append((i, j, k))

visited = [0]*len(H)        # 해당 합을 이미 봤는지 안봤는지 채크
cnt = len(H)                # 합의 개수
G = False                   # 결을 맞게 외쳤는지 여부
ans = 0

K = int(input())
for _ in range(K):
    data = list(input().split())
    if data[0]=='G':
        # 아직 결을 성공 못했고, 합의 개수가 0이면
        # 이번 결 성공
        if not G and cnt==0:
            G = True
            ans += 3
        # 경 실패
        else : ans -=1
    else :
        # i, j, k 순서대로
        i, j, k = sorted(list(data[1:]))
        # 합을 쭉 돌면서 일치하는 것 있는지 찾기
        for h in range(len(H)):
            if H[h]==(int(i)-1,int(j)-1,int(k)-1):
                # 아직 안 찾은 합이면 합 성공
                if not visited[h]:
                    visited[h]=True
                    ans += 1
                    cnt -= 1
                    break
        # 합 실패
        else : ans -= 1

print(ans)
def matrix_mul(M1, M2):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] = (result[i][j] + M1[i][k]*M2[k][j])%1000
    return result

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ans = [[0]*N for _ in range(N)]
for i in range(N):
    ans[i][i]=1

while B>0:
    if B%2!=0:
        ans = matrix_mul(ans, A)
    A = matrix_mul(A, A)
    B//=2

for ele in ans:
    print(*ele)
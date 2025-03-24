def pre(node):
    print(node, end='')
    if left.get(node):
        pre(left[node])
    if right.get(node):
        pre(right[node])

def inord(node):
    if left.get(node):
        inord(left[node])
    print(node, end='')
    if right.get(node):
        inord(right[node])

def post(node):
    if left.get(node):
        post(left[node])
    if right.get(node):
        post(right[node])
    print(node, end='')

N = int(input())
# 이진트리이므로 left, right만 존재
# 인덱스 따로 저장하지 않고 딕셔너리로 관리
left = {}
right = {}
for i in range(N):
    p, l, r = input().split()
    if l!='.':
        left[p]=l
    if r!='.':
        right[p]=r
pre('A')
print()
inord('A')
print()
post('A')
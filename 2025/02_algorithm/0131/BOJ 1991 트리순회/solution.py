N = int(input())
tree = [0]*(2*N)
tree[1]='A'
tree_left = {}
tree_right = {}
for _ in range(N):
    p, l, r = input().split()
    tree_left[p]=l
    tree_right[p] = r

def pre(start):
    global ans1
    ans1+=start
    if tree_left.get(start) and tree_left.get(start)!='.':
        pre(tree_left.get(start))
    if tree_right.get(start) and tree_right.get(start) != '.':
        pre(tree_right.get(start))

def inord(start):
    global ans2
    if tree_left.get(start) and tree_left.get(start) != '.':
        inord(tree_left.get(start))
    ans2+=start
    if tree_right.get(start) and tree_right.get(start) != '.':
        inord(tree_right.get(start))
def pos(start):
    global ans3
    if tree_left.get(start) and tree_left.get(start)!='.':
        pos(tree_left.get(start))
    if tree_right.get(start) and tree_right.get(start) != '.':
        pos(tree_right.get(start))
    ans3+=start

ans1 = ''
ans2 = ''
ans3 = ''

pre('A')
inord('A')
pos('A')
print(ans1)
print(ans2)
print(ans3)

import sys

n=int(sys.stdin.readline().rstrip())
tree={}
for i in range(n):
    root,left,right=sys.stdin.readline().rstrip().split()
    tree[root]=[left,right]

def pre(root):
    if root=='.':
        return
    print(root,end='')
    pre(tree[root][0])
    pre(tree[root][1])

def in_order(root):
    if root=='.':
        return
    in_order(tree[root][0])
    print(root,end='')
    in_order(tree[root][1])
def post(root):
    if root=='.':
        return
    post(tree[root][0])
    post(tree[root][1])
    print(root,end='')

pre('A')
print()
in_order('A')
print()
post('A')
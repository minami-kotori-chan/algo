import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
board={}
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())
    board[arr[i]]=i+1

for i in range(m):
    j=sys.stdin.readline().rstrip()
    if ord(j[0])>ord('0') and ord(j[0])<=ord('9'):
        print(arr[int(j)-1])
        continue
    print(board[j])
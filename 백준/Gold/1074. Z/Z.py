import sys

n,r,c=map(int,sys.stdin.readline().rstrip().split())
result=0
def dfs(row,col,n):
    global r,c,result
    if n==1:
        print(result)
        return
    if r<row+n//2:
        if c<col+n//2:
            dfs(row,col,n//2)
        else:
            result+=(n//2*n//2)
            dfs(row,col+n//2,n//2)
    else:
        if c<col+n//2:
            result+=((n//2*n//2)*2)
            dfs(row+n//2,col,n//2)
        else:
            result+=((n//2*n//2)*3)
            dfs(row+n//2,col+n//2,n//2)
    
dfs(0,0,pow(2,n))
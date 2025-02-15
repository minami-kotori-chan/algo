import sys
n=int(sys.stdin.readline().rstrip())
graph=[]
total=[0,0]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

def check_all(start_row,start_col,size):
    for i in range(start_row,start_row+size):
        for j in range(start_col,start_col+size):
            if graph[i][j]!=graph[start_row][start_col]:
                return 0
    return 1

def divide(start_row,start_col,size):
    if size==1:
        if graph[start_row][start_col]==1:
            total[1]+=1
        else:
            total[0]+=1
        return
    if check_all(start_row,start_col,size)==1:
        total[graph[start_row][start_col]]+=1
        return
    divide(start_row,start_col,size//2)
    divide(start_row+size//2,start_col,size//2)
    divide(start_row,start_col+size//2,size//2)
    divide(start_row+size//2,start_col+size//2,size//2)
divide(0,0,n)
print(total[0])
print(total[1])
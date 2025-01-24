import sys

n = int(sys.stdin.readline().rstrip())
board=[]

for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

def count_board():
    max_value=0

    for i in range(n):
        row_count=1
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                row_count+=1
                max_value=max(max_value,row_count)
            else:
                row_count=1
        col_count=1
        for j in range(1,n):
            if board[j][i] == board[j-1][i]:
                col_count+=1
                max_value=max(max_value,col_count)
            else:
                col_count=1
    
    return max_value

result=0
for i in range(n):
    for j in range(n):
        dc=[0,1,0,-1]
        dr=[-1,0,1,0]
        for k in range(4):
            if i+dr[k]>=0 and j+dc[k]>=0 and i+dr[k]<n and j+dc[k]<n and board[i+dr[k]][j+dc[k]] != board[i][j]:
                temp = board[i+dr[k]][j+dc[k]]
                board[i+dr[k]][j+dc[k]]=board[i][j]
                board[i][j]=temp

                result=max(count_board(),result)

                temp = board[i+dr[k]][j+dc[k]]
                board[i+dr[k]][j+dc[k]]=board[i][j]
                board[i][j]=temp
            if result==n:
                break
        if result==n:
            break
    if result==n:
        break

print(result)
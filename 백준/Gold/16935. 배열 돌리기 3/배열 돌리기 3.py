import sys

n,m,r=map(int,sys.stdin.readline().rstrip().split())
board=[]
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

def move_board(type):
    global board
    n=len(board)
    m=len(board[0])
    if type==1:
        for i in range(n//2):
            board[i],board[n-1-i]=board[n-1-i],board[i]

    elif type==2:
        for i in range(n):
            for j in range(m//2):
                board[i][j],board[i][m-1-j]=board[i][m-1-j],board[i][j]

    elif type==3:
        stack=[]
        for i in range(m):
            stack_row=[]
            for j in range(n):
                stack_row.append(board[n-1-j][i])
            stack.append(stack_row)
        board=stack

    elif type==4:
        stack=[]
        for i in range(m):
            stack_row=[]
            for j in range(n):
                stack_row.append(board[j][m-1-i])
            stack.append(stack_row)
        board=stack

    else:
        sub_stack1,sub_stack2,sub_stack3,sub_stack4=[],[],[],[]
        for i in range(n//2):
            sub1=[]
            sub2=[]
            for j in range(m//2):
                sub1.append(board[i][j])
            for j in range(m//2,m):
                sub2.append(board[i][j])
            sub_stack1.append(sub1)
            sub_stack2.append(sub2)
        for i in range(n//2,n):
            sub3=[]
            sub4=[]
            for j in range(m//2):
                sub3.append(board[i][j])
            for j in range(m//2,m):
                sub4.append(board[i][j])
            sub_stack3.append(sub3)
            sub_stack4.append(sub4)
        if type==5:
            result=[]
            for i in range(n//2):
                sub_stack=[]
                for j in range(m//2):
                    sub_stack.append(sub_stack3[i][j])
                for j in range(m//2):
                    sub_stack.append(sub_stack1[i][j])
                result.append(sub_stack)
            for i in range(n//2):
                sub_stack=[]
                for j in range(m//2):
                    sub_stack.append(sub_stack4[i][j])
                for j in range(m//2):
                    sub_stack.append(sub_stack2[i][j])
                result.append(sub_stack)
            board=result
        elif type==6:
            result=[]
            for i in range(n//2):
                sub_stack=[]
                for j in range(m//2):
                    sub_stack.append(sub_stack2[i][j])
                for j in range(m//2):
                    sub_stack.append(sub_stack4[i][j])
                result.append(sub_stack)
            for i in range(n//2):
                sub_stack=[]
                for j in range(m//2):
                    sub_stack.append(sub_stack1[i][j])
                for j in range(m//2):
                    sub_stack.append(sub_stack3[i][j])
                result.append(sub_stack)
            board=result


for i in map(int,sys.stdin.readline().rstrip().split()):
    move_board(i)
for i in board:
    print(*i)
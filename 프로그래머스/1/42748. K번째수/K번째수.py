def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        stack=[]
        for j in range(commands[i][0]-1,commands[i][1]):
            stack.append(array[j])
        stack.sort()
        answer.append(stack[commands[i][2]-1])
    return answer
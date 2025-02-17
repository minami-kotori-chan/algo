import sys
import heapq
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    max_h=[]
    min_h=[]
    dic={}
    size=0
    for i in range(n):
        opcode,num=sys.stdin.readline().rstrip().split()
        num=int(num)
        if opcode=='I':
            heapq.heappush(min_h,num)
            heapq.heappush(max_h,num*-1)
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        else:
            if num==1:
                while len(max_h)!=0 and  dic[(max_h[0])*-1]==0:
                    heapq.heappop(max_h)
                if len(max_h)>0:
                    dic[(heapq.heappop(max_h))*-1]-=1
                
            else:
                while len(min_h)!=0 and dic[min_h[0]]==0:
                    heapq.heappop(min_h)
                if len(min_h)>0:
                    dic[heapq.heappop(min_h)]-=1
    
    while len(max_h)!=0 and  dic[(max_h[0])*-1]==0:
        heapq.heappop(max_h)
    while len(min_h)!=0 and dic[min_h[0]]==0:
        heapq.heappop(min_h)
    if len(min_h)<1 or len(max_h)<1:
        print("EMPTY")
    else:
        print(max_h[0]*-1,min_h[0])
import sys

time_sum=0
score_sum=0
for i in range(20):
    name,time,grade=sys.stdin.readline().rstrip().split()
    time=int(float(time))

    if grade=='A+':
        score=4.5
    elif grade=='A0':
        score=4.0
    elif grade=='B+':
        score=3.5
    elif grade=='B0':
        score=3.0
    elif grade=='C+':
        score=2.5
    elif grade=='C0':
        score=2.0
    elif grade=='D+':
        score=1.5
    elif grade=='D0':
        score=1.0
    elif grade=='F':
        score=0
    
    if grade!='P':
        time_sum+=time
        score_sum+=score*time
print(score_sum/time_sum)

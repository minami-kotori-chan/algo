import sys

e,s,m = map(int,sys.stdin.readline().rstrip().split())

year=1
year_e,year_s,year_m=1,1,1
while not (year_e==e and year_s==s and year_m==m):
    year_e+=1
    year_s+=1
    year_m+=1
    if year_e==16:
        year_e=1
    if year_s==29:
        year_s=1
    if year_m==20:
        year_m=1
    year+=1
print(year)
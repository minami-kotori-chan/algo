h,m,s=map(int,input().split())
n=int(input())
s+=n
m+=s//60
s=s%60
h+=m//60
m=m%60
h=h%24
print(f"{h} {m} {s}")
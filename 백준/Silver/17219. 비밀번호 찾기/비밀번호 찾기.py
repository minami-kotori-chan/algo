import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
dic={}
for i in range(n):
    site,pw=sys.stdin.readline().rstrip().split()
    dic[site]=pw
for i in range(m):
    print(dic[sys.stdin.readline().rstrip()])
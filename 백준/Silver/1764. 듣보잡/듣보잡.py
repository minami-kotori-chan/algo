import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
n_hash=set()
m_hash=set()
for i in range(n):
    n_hash.add(sys.stdin.readline().rstrip())
for i in range(m):
    m_hash.add(sys.stdin.readline().rstrip())

search_hash=n_hash
list_hash=m_hash
if m<n:
    search_hash,list_hash=list_hash,search_hash
result=[]
for i in search_hash:
    if i in list_hash:
        result.append(i)
result.sort()
print(len(result))
for i in result:
    print(i)
import sys

n=sys.stdin.readline().rstrip()
if n=='M':
    print('MatKor')
elif n=='W':
    print('WiCys')
elif n=='C':
    print('CyKor')
elif n=='A':
    print('AlKor')
else:
    print('$clear')
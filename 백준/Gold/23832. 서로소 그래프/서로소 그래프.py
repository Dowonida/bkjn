import sys
input=sys.stdin.readline

def func(n):
    m=n
    for i in range(2,int(n**(0.5)+1)):
        if m%i==0:
            while m%i==0:
                m//=i
            n=(n//i)*(i-1)
    if m>1:
        n=(n//m)*(m-1)
    return n


N=int(input())
rst=0
for i in range(2,N+1):
    rst+=func(i)
print(rst)

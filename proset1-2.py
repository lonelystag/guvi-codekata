a=input().split()
d=int(a[0])
b=int(a[1])
c=list(str(d))
e=b
while e>0:
    e=e-1
    del(c[e])
c.sort()
print(''.join(c))

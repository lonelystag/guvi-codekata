a=input().split()
b=int(a[0])
c=int(a[1])
d=("%d %d"%(b,c))
a1=input().split()
b1=int(a1[0])
c1=int(a1[1])
d1=("%d %d"%(b1,c1))
if a>a1:
  e1=b-b1
  e2=c-c1
  print("%d %d"%(e1,e2))
if a==a1:
  print('0','0')
if a<a1:
  f1=b1-b
  f2=c1-c
  print("%d %d"%(f1,f2))

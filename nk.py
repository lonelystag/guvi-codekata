sum=0
a=[]
n=int(input())
k=int(input())
for i in range(0,n):
  m=input()
  a.append(m)
print(a)
for j in range(0,k,1):
  sum=(sum+a[j])
print(sum)

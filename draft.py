a=int(input())
b =input().split(' ')
b= [int(num) for num in b]
c=len(b)
if a==c:
  b.sort()
e=list(str(b))
f=c-1
print(e[c])

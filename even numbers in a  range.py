a=input().split()
b=int(a[0])
c=int(a[1])
list=[]
for i in range(b+1,c):
    if(i%2==0):
    	list.append(i)
print(" ".join(map(str,list)))

n=input().split()
p=int(n[0])
q=int(n[1])
list=[]
for i in range(p+1,q):
    if(i%2!=0):
  	  list.append(i)
print(" ".join(map(str,list)))

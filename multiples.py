a=int(input())
list=[]
for i in range(1,6):
	multi=a*i
	list.append(multi)
print(" ".join(map(str,list)))

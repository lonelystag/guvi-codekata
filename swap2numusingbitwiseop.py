x=input().split()
a=int(x[0])
b=int(x[1])
a = a ^ b
b = a ^ b
a = a ^ b
print('',a,'',b)

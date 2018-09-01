sum=0
a=[]
n=int(input("Enter the number of elements in array"))
k=int(input("How many elements do u want to sum"))
for i in range(0,n):
  m=input("enter the value of array")
  a.append(m)
print(a)
for j in range(0,k,1):
  sum=(sum+a[j])
print(sum)

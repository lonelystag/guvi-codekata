a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
if(a>b and a>c):
  print(a)
elif(b>a and b>c):
  print(b)
elif(c>a and c>b):
  print(c)
else:
  print("Invalid")

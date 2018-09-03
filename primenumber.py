n=int(input("Enter the value"))
if(n<=1000):
  if(n>0):
    for i in range(2,n):
      if(n%i==0):
        print("No")
    else:
      print("Yes")
  else:
    print("No")
else:
  print("No")

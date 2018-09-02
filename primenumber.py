a=int(input("Enter the value"))
if(a>0):
  for i in range(2,a):
    if(a%i==0):
      print("Not a prime number")
  else:
    print("Prime number")
else:
  print("Not a prime number")

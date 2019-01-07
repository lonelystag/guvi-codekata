N=int(input())
print("Input:")
print(N)
if N<=100000:
  sum = 0
  temp = N
  while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
  print('Output:')
  if N == sum:
    print("Yes")
  else:
    print("No")

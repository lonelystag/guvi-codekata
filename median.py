#Ramesh 
a=int(input())
b =input().split(' ')
b= [int(num) for num in b]
c=len(b)
if a==c:
  b.sort()
  mid=int((c-1)/2)
  print(b[mid])
# This program is for sorting a list and finding its median element

#prgram to represent the given number as hour and minutes
a = int(input())
hour = a //60
a %= 60
minutes = a // 1
print("%d %d" % (hour,minutes))

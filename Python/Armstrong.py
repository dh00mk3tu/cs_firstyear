# Made By Anirudh Rath | dh00mk3tu
# Visit anirudhrath.tech to know more
# Find the Armstrong Number

num = int(input("Enter a number: "))
sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"\n is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
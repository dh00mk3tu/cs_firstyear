# Made By Anirudh Rath | dh00mk3tu
# Visit anirudhrath.tech to know more
# Print number in decreasing order from the input number
n = int(input("Enter the value of n: "))

if (n<=1):
	print ("n should be greater than 1")
	exit()

print ("value of n: ",n)

print ("numbers from {0} to {1} are: ".format(n,1))


for i in range(n,0,-1):
	print (i)

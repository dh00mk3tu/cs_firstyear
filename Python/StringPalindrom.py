# Made By Anirudh Rath | dh00mk3tu
# Visit anirudhrath.tech to know more
# Check if a string is a Palindrome or not
my_str = str(input("\n Enter the String: "))

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
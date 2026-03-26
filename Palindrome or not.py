#Palindrome or not:
n=int(input("Enter a number:"))
temp=n
while n!=0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if rev==n:
    print("Palindrome Number:")
else:
    print("Not a Palindrome number:")

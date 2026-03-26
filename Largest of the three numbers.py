#Largest of the two numbers:
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=int(input("Enter another number:"))
if a>b&a>c:
    print(f"{a} is big")
elif b>c:
    print(f"{b} is big")
else:
    print(f"{c} is big")

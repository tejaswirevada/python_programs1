#if:
number=5
if number>4:
    sum=number*number
    print(sum)
#if else:
t=10
if t%2==0:
    print("Even")
else:
    print("Odd")
#if-elif:
def usercheck(choice):
    if(choice==1):
            print("Admin")
    elif(choice==2):
            print("Guest")
    elif(choice==3):
            print("Administrator")
    else:
        print("Enter valid choice:")
usercheck(1)
usercheck(2)
usercheck(3)
usercheck(4)
#nested decision:
#nested if:
#nested if-else
a=int(input("Enter a number:"))
b=int(input("Enter another number"))
if a>=b:
    if a==b:
        print("a is equal to b")
    else:
        print("a is greater than b")
else:
    print("a is smaller than b")

        

















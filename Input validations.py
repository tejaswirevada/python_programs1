#INPUT VALIDATION:

#Data validation:
age=input("Enter age:")
if age.isdigit():
    age=int(age)
    print("Valid age")
else:
    print("Invalid age")
    

#Range validation:
n=int(input("Enter a number:"))
if 1<n<10:
    print("Valid")
else:
    print("Invalid")


#Format validation:
p=input("Enter password:")
if len(p)>=6:
    print("Strong")
else:
    print("Too Weak")

#
email=input("Enter email:")
if '@' in email and '.' in email:
    print("Valid email")
else:
    print("Invalid email")
    

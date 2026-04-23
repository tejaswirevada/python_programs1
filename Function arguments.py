#Function arguments:
#Required arguments:
def sum(a,b):
    c=a+b
    print(c)
sum(10,20)

#Default arguments:
def sum(x=10,y=30,z=20):
    add=x+y+z
    print(add)
sum(x=10,y=90,z=20)
sum(x=10)

#Keyword arguments:
def sum(x,y=30,z=40):
    addition=x+y+z
    print(addition)
sum(10,50,100)
sum(190)

#Variable length arguments[Kargs]:
def display(*no):
    print(no)
display(10,20,40)

#Positional arguments:
def greet(name="Hello",age=24):
    print(f"My name is {name} and I am {age}years old")
greet("Hello",24)
greet(24,"Hello")

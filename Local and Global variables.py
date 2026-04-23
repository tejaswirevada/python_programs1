#Local and Global Variables:


#Local variable:
def display():
    a=10
    print("inside value is:",a) 
display()


#Global variable:
x=10
def display():
    print("Inside fun:",x)
display()
print("Outside fun:",x)


#Global vs Local:
x=100
def display():
    x=10
    print("The value for inside:",x)
display()
print("The value for outside:",x)


#Change Global variable value:
y=20
def change():
    global y
    y=40
change()
print(y)



